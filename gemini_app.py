#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modul gemini_app.py:
Enthält:
- Hilfsfunktionen (z. B. ensure_pil_image)
- Logging-Konfiguration und Umgebungsvariablen
- Definition der Hauptklasse GeminiApp
- Definition der Klassen Connection, Node und ImageNode
"""

import os
import io
import numpy as np
import logging
import tempfile
from PIL import Image, ImageEnhance, UnidentifiedImageError
from dotenv import load_dotenv
from google import genai
from google.genai import types
from openai import OpenAI # Expliziter Import von OpenAI Client
import requests
import torch
import random
import cv2
import time
from requests.exceptions import RequestException
from typing import Optional, Union, List, Tuple

# -------------------------------------------------------------------------------
# Logging-Konfiguration
# -------------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO, # Von DEBUG zu INFO geändert! Die Hölle braucht keine unnötigen Details.
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
logger.info("Modul gemini_app.py geladen.")

# -------------------------------------------------------------------------------
# Hilfsfunktion: ensure_pil_image
# -------------------------------------------------------------------------------
def ensure_pil_image(image: Union[Image.Image, np.ndarray]) -> Image.Image:
    """
    Stellt sicher, dass das gegebene Bild ein PIL.Image-Objekt ist.

    Verwendet strukturelles Pattern Matching (Python 3.12):
    """
    match image:
        case Image.Image():
            return image
        case np.ndarray():
            return Image.fromarray(image)
        case _:
            raise ValueError("Input ist weder ein PIL.Image noch ein numpy.ndarray.")

# -------------------------------------------------------------------------------
# Laden der .env-Datei (API-Keys)
# -------------------------------------------------------------------------------
load_dotenv()
API_KEY: Optional[str] = os.getenv("API_KEY")
if API_KEY is None:
    logger.error("API_KEY nicht in der .env-Datei gefunden!")
    raise ValueError("API_KEY nicht gefunden! Bitte in der .env-Datei definieren.")

OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    logger.error("OPENAI_API_KEY nicht in der .env-Datei gefunden!")
    raise ValueError("OPENAI_API_KEY nicht gefunden! Bitte in der .env-Datei definieren.")


# -------------------------------------------------------------------------------
# Initialisierung des Gemini Clients und OpenAI API-Key
# -------------------------------------------------------------------------------
client = genai.Client(api_key=API_KEY)
logger.info("Gemini Client initialisiert.")
client_openai = OpenAI(api_key=OPENAI_API_KEY) # OpenAI Client initialisieren für DALL-E, korrekte Initialisierung für OpenAI API


sys_instruct = "Du bist Cipher ein Assistent unseres Untermehmens CipherCore, wir stehen für Sicherheit in der Programmierung. Deine Antworten immer in Deutsch! Erwähne niemals die beigefügte Textdatei!."


# -------------------------------------------------------------------------------
# Geräteauswahl (CUDA falls verfügbar)
# -------------------------------------------------------------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Verwendetes Gerät: {device}")

# ===============================================================================
# Klasse GeminiApp: Enthält alle Methoden zur Interaktion mit der Gemini API
# ===============================================================================
class GeminiApp:
    def __init__(self):
        """
        Initialisiert die GeminiApp mit dem Gemini Client und dem ausgewählten Gerät.
        """
        self.client = client
        self.device = device
        self.client_openai = client_openai # OpenAI Client für DALL-E, korrekter Client Name
        

    def generate_dalle_image(self, prompt: str = "a white siamese cat", size: str = "576x1024") -> Optional[Image.Image]:
        """
        Generiert ein Bild mittels DALL·E 3.
        """
        try:
            response = self.client_openai.images.generate( # Korrigierte Zeile: self.client_openai.images.generate, verwende den OpenAI Client
                model="dall-e-3",
                prompt=prompt,
                size=size,
                n=1
            )
            image_url = response.data[0].url
            print(f"DALL·E Bild-URL: {image_url}")
            r = requests.get(image_url)
            r.raise_for_status()
            image_data = io.BytesIO(r.content)
            image = Image.open(image_data).convert("RGB")
            return image
        except Exception as e:
            logger.exception("Fehler bei der DALL·E Bildgenerierung:")
            return None



    def validate_prompt(self, prompt: str) -> bool:
        """
        Validiert die Länge des Prompts.
        """
        if len(prompt) > 1000000:
            raise ValueError("Der Prompt ist zu lang. Bitte maximal 1000000 Zeichen verwenden.")
        return True

    def validate_file_size(self, file_path: str, max_size: int) -> bool:
        """
        Validiert die Dateigröße.
        """
        file_size = os.path.getsize(file_path)
        if file_size > max_size:
            raise ValueError(f"Die Datei ist zu groß ({file_size} Bytes). Bitte eine kleinere Datei wählen.")
        return True

    def process_audio(self, prompt: str, audio_file: str) -> str:
        """
        Verarbeitet eine Audiodatei mit einem Prompt.
        """
        try:
            self.validate_prompt(prompt)
            allowed_audio = {".mp3", ".wav", ".aiff", ".aif", ".aac", ".ogg", ".flac"}
            _, ext = os.path.splitext(audio_file)
            ext = ext.lower()
            if ext not in allowed_audio:
                raise ValueError(f"Unsupported audio file type: {ext}")
            self.validate_file_size(audio_file, 6_000_000)
            with open(audio_file, "rb") as f:
                audio_bytes = f.read()
            logger.debug(f"Audiodatei '{audio_file}' wurde eingelesen ({len(audio_bytes)} Bytes).")
            mime_map = {
                ".mp3": "audio/mp3",
                ".wav": "audio/wav",
                ".aiff": "audio/aiff",
                ".aif": "audio/aiff",
                ".aac": "audio/aac",
                ".ogg": "audio/ogg",
                ".flac": "audio/flac"
            }
            mime_type = mime_map.get(ext, "audio/mp3")
            logger.debug(f"Verwendeter MIME-Typ: {mime_type}")
            audio_part = types.Part.from_bytes(data=audio_bytes, mime_type=mime_type)
            response = self.client.models.generate_content(
                model='gemini-2.0-flash-thinking-exp-01-21',
                contents=[sys_instruct, prompt, audio_part]
            )
            logger.info("Anfrage (Audio) gesendet.")
            return response.text
        except ValueError as ve:
            logger.exception("Wertfehler bei Audiodatei:")
            return f"Fehler: {str(ve)}"
        except Exception as e:
            logger.exception("Allgemeiner Fehler in process_audio:")
            return f"Fehler: {str(e)}"


    def process_chat(self, prompt: str, image_file: Optional[Union[str, np.ndarray]] = None) -> str:
        """
        Verarbeitet einen Chat-Prompt mit optionalem Bild.
        """
        try:
            self.validate_prompt(prompt)
            contents: List[Union[types.Part, str]] = [sys_instruct, prompt]
            if image_file is not None:
                if isinstance(image_file, np.ndarray):
                    if image_file.max() <= 1.0:
                        image_pil = Image.fromarray((image_file * 255).astype(np.uint8))
                    else:
                        image_pil = Image.fromarray(image_file.astype(np.uint8))
                    with io.BytesIO() as output:
                        image_pil.save(output, format="PNG")
                        image_bytes = output.getvalue()
                    mime_type = "image/png"
                    logger.debug("Bild (Array) wurde in Bytes konvertiert (MIME-Typ: image/png).")
                    contents.append(types.Part.from_bytes(data=image_bytes, mime_type=mime_type))
                elif isinstance(image_file, str) and image_file != "":
                    allowed_img = {".jpg", ".jpeg", ".png", ".gif"}
                    _, ext = os.path.splitext(image_file)
                    ext = ext.lower()
                    if ext not in allowed_img:
                        raise ValueError(f"Unsupported image file type: {ext}")
                    with open(image_file, "rb") as f:
                        image_bytes = f.read()
                    logger.debug(f"Bilddatei '{image_file}' wurde eingelesen ({len(image_bytes)} Bytes).")
                    mime_map = {
                        ".jpg": "image/jpeg",
                        ".jpeg": "image/jpeg",
                        ".png": "image/png",
                        ".gif": "image/gif"
                    }
                    mime_type = mime_map.get(ext, "image/jpeg")
                    contents.append(types.Part.from_bytes(data=image_bytes, mime_type=mime_type))
                    logger.debug(f"Bild als Part-Objekt hinzugefügt (MIME-Typ: {mime_type}).")
            response = self.client.models.generate_content(
                model='gemini-2.0-flash-thinking-exp-01-21',
                contents=contents
            )
            logger.info("Anfrage(Chat & Bild) gesendet.")
            return response.text
        except FileNotFoundError as fe:
            logger.exception("Datei nicht gefunden:")
            return "Die Bilddatei wurde nicht gefunden. Bitte überprüfen Sie den Dateipfad."
        except UnidentifiedImageError as ue:
            logger.exception("Das Bild konnte nicht identifiziert werden:")
            return "Das Bildformat wird nicht unterstützt oder die Datei ist beschädigt."
        except ValueError as ve:
            logger.exception("Wertfehler bei der Bildverarbeitung:")
            return f"Fehler: {str(ve)}"
        except Exception as e:
            logger.exception("Allgemeiner Fehler in process_chat:")
            return f"Fehler: {str(e)}"

    def process_video(self, prompt: str, video_file: str) -> str:
        """
        Verarbeitet eine Videodatei mit einem Prompt.
        """
        try:
            self.validate_prompt(prompt)
            allowed_video = {".mp4", ".avi", ".mov", ".webm"}
            _, ext = os.path.splitext(video_file)
            ext = ext.lower()
            if ext not in allowed_video:
                raise ValueError(f"Unsupported video file type: {ext}")
            self.validate_file_size(video_file, 20_000_000)
            with open(video_file, "rb") as f:
                video_bytes = f.read()
            logger.debug(f"Videodatei '{video_file}' wurde eingelesen ({len(video_bytes)} Bytes).")
            mime_map = {
                ".mp4": "video/mp4",
                ".avi": "video/x-msvideo",
                ".mov": "video/quicktime",
                ".webm": "video/webm"
            }
            mime_type = mime_map.get(ext, "video/mp4")
            logger.debug(f"Verwendeter MIME-Typ für Video: {mime_type}")
            video_part = types.Part.from_bytes(data=video_bytes, mime_type=mime_type)
            response = self.client.models.generate_content(
                model='gemini-2.0-flash',
                contents=[sys_instruct, prompt, video_part]
            )
            logger.info("Anfrage(Video) gesendet.")
            return response.text
        except ValueError as ve:
            logger.exception("Wertfehler bei Video:")
            return f"Fehler: {str(ve)}"
        except Exception as e:
            logger.exception("Allgemeiner Fehler in process_video:")
            return f"Fehler: {str(e)}"


    def process_file(self, prompt: str, file_path: Union[str, tempfile._TemporaryFileWrapper]) -> str:
        """
        Verarbeitet eine Datei mit einem Prompt.
        """
        try:
            self.validate_prompt(prompt)

            # Wenn es sich um ein temporäres Dateiobjekt handelt, hole den Dateipfad
            if isinstance(file_path, tempfile._TemporaryFileWrapper):
                file_path = file_path.name

            allowed_docs = {
                ".txt", ".c", ".cpp", ".py", ".java", ".php", ".sql", ".html",
                ".doc", ".docx", ".pdf", ".rtf", ".dot", ".dotx", ".hwp", ".hwpx",
                ".csv", ".tsv", ".xls", ".xlsx"
            }

            _, ext = os.path.splitext(file_path)
            ext = ext.lower()
            if ext not in allowed_docs:
                raise ValueError(f"Unsupported document file type: {ext}")

            self.validate_file_size(file_path, 7_000_000)

            with open(file_path, "rb") as f:
                file_bytes = f.read()

            logger.debug(f"Datei '{file_path}' wurde eingelesen ({len(file_bytes)} Bytes).")

            mime_map = {
                ".txt": "text/plain",
                ".c": "text/plain",
                ".cpp": "text/plain",
                ".py": "text/x-python",
                ".java": "text/plain",
                ".php": "text/plain",
                ".sql": "text/plain",
                ".html": "text/html",
                ".doc": "application/msword",
                ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                ".pdf": "application/pdf",
                ".rtf": "application/rtf",
                ".dot": "application/msword",
                ".dotx": "application/vnd.openxmlformats-officedocument.wordprocessingml.template",
                ".hwp": "application/octet-stream",
                ".hwpx": "application/octet-stream",
                ".csv": "text/csv",
                ".tsv": "text/tab-separated-values",
                ".xls": "application/vnd.ms-excel",
                ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            }

            mime_type = mime_map.get(ext, "application/octet-stream")

            logger.debug(f"Verwendeter MIME-Typ für Datei: {mime_type}")

            contents = [prompt, types.Part.from_bytes(data=file_bytes, mime_type=mime_type)]
            response = self.client.models.generate_content(
                model='gemini-2.0-flash-thinking-exp-01-21',
                contents=contents
            )

            logger.info("Anfrage(Datei) gesendet.")
            return response.text
        except ValueError as ve:
            logger.exception("Wertfehler bei Datei:")
            return f"Fehler: {str(ve)}"
        except Exception as e:
            logger.exception("Allgemeiner Fehler in process_file:")
            return f"Fehler: {str(e)}"


    def process_create(self, prompt: str, export_format: str) -> str:
        """
        Erstellt Inhalte basierend auf einem Prompt und exportiert sie in ein gewünschtes Format.
        """
        try:
            self.validate_prompt(prompt)
            response = self.client.models.generate_content(
                model='gemini-2.0-flash-thinking-exp-01-21',
                contents=[prompt]
            )
            content_text = response.text
            logger.info("Inhalt erstellt.")
            if export_format == "Word":
                temp = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
                from docx import Document
                doc = Document()
                doc.add_paragraph(content_text)
                doc.save(temp.name)
            elif export_format == "Excel":
                import pandas as pd
                df = pd.DataFrame({"Inhalt": [content_text]})
                temp = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
                df.to_excel(temp.name, index=False)
            elif export_format == "CSV":
                import pandas as pd
                df = pd.DataFrame({"Inhalt": [content_text]})
                temp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
                df.to_csv(temp.name, index=False)
            elif export_format == "PDF":
                temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
                from fpdf import FPDF
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.multi_cell(0, 10, content_text)
                pdf.output(temp.name)
            else:
                raise ValueError(f"Unbekanntes Exportformat: {export_format}")
            logger.info(f"Inhalt wurde als {export_format} gespeichert: {temp.name}")
            return temp.name
        except ValueError as ve:
            logger.exception("Wertfehler bei Export:")
            return f"Fehler: {str(ve)}"
        except Exception as e:
            logger.exception("Allgemeiner Fehler in process_create:")
            return f"Fehler: {str(e)}"

    def extract_main_colors(self, image: Image.Image) -> List[Tuple[int, int, int]]:
        """
        Extrahiert die Hauptfarben aus einem Bild.
        """
        try:
            image_array = np.array(image)
        except Exception as e:
            logger.exception("Fehler beim Konvertieren des Bildes in ein Array:")
            raise ValueError("Das Bild konnte nicht in ein Array konvertiert werden.")
        colors = {}
        for i in range(image_array.shape[0]):
            for j in range(image_array.shape[1]):
                color = tuple(image_array[i, j])
                if sum(color) > 30:
                    colors[color] = colors.get(color, 0) + 1
        sorted_colors = sorted(colors.items(), key=lambda item: item[1], reverse=True)
        main_colors = [color for color, count in sorted_colors[:12]]
        scaled_colors = [(min(c[0] + 50, 255), min(c[1] + 50, 255), min(c[2] + 50, 255)) for c in main_colors]
        return scaled_colors

    def create_neural_network(self, main_colors: List[Tuple[int, int, int]]) -> List['Node']:
        """
        Erstellt ein einfaches neuronales Netzwerk basierend auf den Hauptfarben.
        """
        color_labels = ["Rot", "Grün", "Blau", "Gelb", "Cyan", "Magenta", "Orange", "Violett", "Braun", "Rosa", "Schwarz", "Weiß"]
        category_nodes = [Node(label) for label in color_labels]
        for node in category_nodes:
            for target_node in category_nodes:
                if node != target_node:
                    node.add_connection(target_node, weight=random.uniform(0.01, 8.0))
        return category_nodes

    def save_image(self, image_tensor: torch.Tensor, filename: str, resolution: str, original_size: Optional[Tuple[int, int]] = None) -> None:
        """
        Speichert ein Bild mit der angegebenen Auflösung.
        """
        try:
            resolutions = {
                "HD": (1280, 720),
                "Full HD": (1920, 1080),
                "2K (Standard)": (2048, 1080),
                "2K (Quad HD)": (2560, 1440),
                "2K (3840x1080)": (3840, 1080),
                "2K (3840x2160) Scaled": (3840, 2160),
                "2K (3840x3840)": (3840, 3840),
                "Original (2K)": (2048, 2048),
                "4K (Standard)": (3840, 2160),
                "4K (Full Aperture)": (4096, 3112),
                "4K (DCI)": (4096, 2160),
                "4K (3840x1600)": (3840, 1600),
                "4K (3840x2400)": (3840, 2400),
                "4K (3840x3840)": (3840, 3840),
                "4K": (5760, 3240),
                "8K (Standard)": (7680, 4320),
                "8K (Full Aperture)": (8192, 6224),
                "8K (3840x3840) Scaled": (7680, 7680),
                "8K (7680x3200)": (7680, 3200),
                "8K (7680x4800)": (7680, 4800),
                "8K (7680x7680)": (7680, 7680),
                "8K": (10670, 6000),
                "Cover": (1024, 1024),
                "TikTok": (1080, 1920),
                "Facebook Post": (1200, 630),
                "Facebook Story": (1080, 1920),
                "YouTube Thumbnail": (1280, 720),
                "YouTube Short": (1080, 1920),
                "Instagram Post": (1080, 1080),
                "Instagram Story": (1080, 1920),
            }
            if resolution == "Original (2K)" and original_size:
                width, height = original_size
            else:
                width, height = resolutions.get(resolution, (1920, 1080))
            image = Image.fromarray((image_tensor.cpu().numpy().transpose(1, 2, 0) * 255).astype(np.uint8))
            image = image.resize((width, height), Image.Resampling.LANCZOS)
            image.save(filename, format='webp', lossless=True, quality=80, dpi=(300, 300))
            print(f"Bild erfolgreich gespeichert als {filename} mit Auflösung {resolution} und 300 DPI")
        except OSError as ose:
            logger.exception("Fehler beim Speichern des Bildes:")
            raise OSError("Das Bild konnte nicht gespeichert werden. Überprüfen Sie Schreibrechte und freien Speicherplatz.")

    def sharpen_image(self, image: Image.Image) -> Image.Image:
        """
        Schärft ein Bild.
        """
        try:
            enhancer = ImageEnhance.Sharpness(image)
            return enhancer.enhance(1.5)
        except Exception as e:
            logger.exception("Fehler beim Schärfen des Bildes:")
            raise ValueError("Das Bild konnte nicht geschärft werden.")

    def match_histogram(self, source: Image.Image, template: Image.Image) -> Image.Image:
        """
        Passt das Histogramm eines Bildes an ein anderes an.
        """
        try:
            source = cv2.cvtColor(np.array(source), cv2.COLOR_RGB2LAB).astype("float32")
            template = cv2.cvtColor(np.array(template), cv2.COLOR_RGB2LAB).astype("float32")
            (l, a, b) = cv2.split(source)
            (lH, aH, bH) = cv2.split(template)
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            l = clahe.apply((l * 255).astype(np.uint8)) / 255.0
            a = cv2.equalizeHist((a * 255).astype(np.uint8)) / 255.0
            b = cv2.equalizeHist((b * 255).astype(np.uint8)) / 255.0
            result = cv2.merge((l, a, b))
            result = cv2.cvtColor(result.astype("uint8"), cv2.COLOR_LAB2RGB)
            return Image.fromarray(result)
        except Exception as e:
            logger.exception("Fehler beim Histogramm-Matching:")
            raise ValueError("Das Histogramm konnte nicht angepasst werden.")

    def calculate_brightness(self, image: Image.Image) -> float:
        """
        Berechnet die durchschnittliche Helligkeit eines Bildes.
        """
        try:
            image_array = np.array(image).astype(float)
            mean_brightness = np.mean(image_array) / 255.0
            return (mean_brightness * 2) - 1
        except Exception as e:
            logger.exception("Fehler bei der Berechnung der Helligkeit:")
            raise ValueError("Die Helligkeit konnte nicht berechnet werden.")

    def calculate_contrast(self, image: Image.Image) -> float:
        """
        Berechnet den Kontrast eines Bildes.
        """
        try:
            image_array = np.array(image).astype(float)
            std_dev = np.std(image_array)
            contrast = (std_dev / 128.0) + 1.0
            return max(0.5, min(2.0, contrast))
        except Exception as e:
            logger.exception("Fehler bei der Berechnung des Kontrasts:")
            raise ValueError("Der Kontrast konnte nicht berechnet werden.")

    def generate_and_display_image(self, image: Optional[Image.Image], brightness_factor: float, contrast_factor: float, resolution: str) -> Tuple[Optional[Image.Image], Optional[str]]:
        """
        Generiert und zeigt ein Bild basierend auf den Eingabeparametern.
        """
        try:
            if image is None:
                return None, None
            image = ensure_pil_image(image)
            start_time = time.time()
            main_colors = self.extract_main_colors(image)
            print(f"Hauptfarbwerte: {main_colors}")
            if len(main_colors) < 12 or all(sum(color) < 150 for color in main_colors):
                print("Hauptfarben zu dunkel oder zu wenige Farben, Standardfarben werden verwendet.")
                main_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
                               (0, 255, 255), (255, 0, 255), (255, 165, 0), (128, 0, 128),
                               (165, 42, 42), (255, 192, 203), (0, 0, 0), (255, 255, 255)]
            main_colors = [(r / 255.0, g / 255.0, b / 255.0) for r, g, b in main_colors]
            category_nodes = self.create_neural_network(main_colors)
            for node, color in zip(category_nodes, main_colors):
                node.activation = sum(color) / 3
                print(f"Knoten {node.label}: Aktivierung = {node.activation}, Farbe = {color}")
            from gemini_app import ImageNode  # Import innerhalb der Methode, um zyklische Abhängigkeiten zu vermeiden
            image_node = ImageNode("Image")
            image_node.generate_image(category_nodes, image, brightness_factor, contrast_factor)
            generated_image = Image.fromarray((image_node.image.cpu().numpy().transpose(1, 2, 0) * 255).astype(np.uint8))
            generated_image = self.sharpen_image(generated_image)
            generated_image = self.match_histogram(generated_image, image)
            resolutions_dict = {
                "HD": (1280, 720),
                "Full HD": (1920, 1080),
                "2K (Standard)": (2048, 1080),
                "2K (Quad HD)": (2560, 1440),
                "2K (3840x1080)": (3840, 1080),
                "2K (3840x2160) Scaled": (3840, 2160),
                "2K (3840x3840)": (3840, 3840),
                "Original (2K)": (2048, 2048),
                "4K (Standard)": (3840, 2160),
                "4K (Full Aperture)": (4096, 3112),
                "4K (DCI)": (4096, 2160),
                "4K (3840x1600)": (3840, 1600),
                "4K (3840x2400)": (3840, 2400),
                "4K (3840x3840)": (3840, 3840),
                "4K": (5760, 3240),
                "8K (Standard)": (7680, 4320),
                "8K (Full Aperture)": (8192, 6224),
                "8K (3840x3840) Scaled": (7680, 7680),
                "8K (7680x3200)": (7680, 3200),
                "8K (7680x4800)": (7680, 4800),
                "8K (7680x7680)": (7680, 7680),
                "8K": (10670, 6000),
                "Cover": (1024, 1024),
                "TikTok": (1080, 1920),
                "Facebook Post": (1200, 630),
                "Facebook Story": (1080, 1920),
                "YouTube Thumbnail": (1280, 720),
                "YouTube Short": (1080, 1920),
                "Instagram Post": (1080, 1080),
                "Instagram Story": (1080, 1920),
            }
            if resolution == "Original (2K)" and image.size:
                width, height = image.size
            else:
                width, height = resolutions_dict.get(resolution, (1920, 1080))
            generated_image = generated_image.resize((width, height), Image.Resampling.LANCZOS)
            end_time = time.time()
            print(f"Bild erfolgreich generiert und angezeigt. Generierungszeit: {end_time - start_time:.2f} Sekunden")
            self.save_image(image_node.image, "kunst.webp", resolution, original_size=image.size if resolution == "Original (2K)" else None)
            return image, "kunst.webp"
        except Exception as e:
            logger.exception("Fehler in generate_and_display_image:")
            return None, f"Fehler: {str(e)}"

    def process_inputs(self, image: Optional[Image.Image], brightness: float, contrast: float, resolution: str) -> Tuple[Optional[Image.Image], Optional[str]]:
        """
        Verarbeitet die Eingabeparameter für die Bildgenerierung.
        """
        try:
            if image is not None:
                return self.generate_and_display_image(image, brightness, contrast, resolution)
            else:
                return None, None
        except Exception as e:
            logger.exception("Fehler in process_inputs:")
            return None, f"Fehler: {str(e)}"

    def load_image_from_file(self, file_path: str) -> Optional[Image.Image]:
        """
        Lädt ein Bild aus einer Datei.
        """
        try:
            if os.path.exists(file_path):
                return Image.open(file_path)
            else:
                return None
        except Exception as e:
            logger.exception("Fehler beim Laden des Bildes:")
            return None

# ===============================================================================
# Definition der Klassen Connection, Node und ImageNode
# ===============================================================================
class Connection:
    def __init__(self, target_node: 'Node', weight: Optional[float] = None):
        self.target_node = target_node
        self.weight = weight if weight is not None else random.uniform(0.1, 1.0)
        self.weight_history = []

class Node:
    def __init__(self, label: str):
        self.label = label
        self.connections: List[Connection] = []
        self.activation = 0.0
        self.activation_history = []

    def add_connection(self, target_node: 'Node', weight: Optional[float] = None):
        self.connections.append(Connection(target_node, weight))

    def propagate_signal(self, input_signal: float):
        self.activation = max(0, input_signal)
        self.activation_history.append(self.activation)
        for connection in self.connections:
            connection.target_node.activation += self.activation * connection.weight
            connection.weight_history.append(connection.weight)

class ImageNode(Node):
    def __init__(self, label: str):
        super().__init__(label)
        self.image: Optional[torch.Tensor] = None
        self.device = device

    def generate_image(self, category_nodes: List[Node], original_image: Image.Image, brightness_factor: float, contrast_factor: float):
        self.image = self.generate_image_from_categories(category_nodes, original_image, brightness_factor, contrast_factor)

    def generate_image_from_categories(self, category_nodes: List[Node], original_image: Image.Image, brightness_factor: float, contrast_factor: float) -> torch.Tensor:
        image_array = np.array(original_image) / 255.0
        image_tensor = torch.tensor(image_array, dtype=torch.float32).permute(2, 0, 1).to(self.device)
        modified_image_tensor = self.process_image(image_tensor, category_nodes, brightness_factor, contrast_factor)
        return modified_image_tensor

    def process_image(self, image_tensor: torch.Tensor, category_nodes: List[Node], brightness_factor: float, contrast_factor: float) -> torch.Tensor:
        modified_image_tensor = image_tensor.clone()
        for x in range(modified_image_tensor.shape[1]):
            for y in range(modified_image_tensor.shape[2]):
                pixel = modified_image_tensor[:, x, y]
                brightness = float(brightness_factor)
                contrast = float(contrast_factor)
                for node in category_nodes:
                    brightness += node.activation * 0.1
                    contrast += node.activation * 0.1
                pixel = torch.clamp((pixel - 0.5) * contrast + 0.5 + brightness, 0, 1)
                modified_image_tensor[:, x, y] = pixel
        return modified_image_tensor

    def get_color_from_label(self, label: str) -> torch.Tensor:
        color_map = {
            "Rot": torch.tensor([1, 0, 0], device=self.device),
            "Grün": torch.tensor([0, 1, 0], device=self.device),
            "Blau": torch.tensor([0, 0, 1], device=self.device),
            "Gelb": torch.tensor([1, 1, 0], device=self.device),
            "Cyan": torch.tensor([0, 1, 1], device=self.device),
            "Magenta": torch.tensor([1, 0, 1], device=self.device),
            "Orange": torch.tensor([1, 0.5, 0], device=self.device),
            "Violett": torch.tensor([0.5, 0, 0.5], device=self.device),
            "Braun": torch.tensor([0.5, 0.25, 0.125], device=self.device),
            "Rosa": torch.tensor([1, 0.75, 0.8], device=self.device),
            "Schwarz": torch.tensor([0, 0, 0], device=self.device),
            "Weiß": torch.tensor([1, 1, 1], device=self.device)
        }
        return color_map.get(label, torch.tensor([1, 1, 1], device=self.device))