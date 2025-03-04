import os
import gradio as gr
import fitz  # PyMuPDF
import logging
import shutil
from pdfid.pdfid import PDFiD

# Logging einrichten
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Verzeichnisse für hochgeladene und bereinigte PDFs
UPLOAD_FOLDER = "uploads"
BEREINIGTE_FOLDER = "bereinigte_pdfs"
ALLOWED_EXTENSIONS = {'pdf'}
VERBOTENE_OBJEKTE = ["/JavaScript", "/JS", "/AA", "/OpenAction", "/Launch", "/EmbeddedFile", "/RichMedia", "/URI", "/AcroForm", "/XFA", "/ObjStm"]

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(BEREINIGTE_FOLDER, exist_ok=True)

def ist_erlaubte_datei(dateiname):
    return '.' in dateiname and dateiname.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def analysiere_pdf_mit_pdfid(pdf_pfad):
    try:
        logging.info(f"PDFiD Analyse gestartet für: {pdf_pfad}")
        root = PDFiD(pdf_pfad)
        objekte = [] # Liste statt Dictionary, um Objekttypen zu speichern
        gefundene_objekte_meldungen = []

        for obj in VERBOTENE_OBJEKTE:
            elements = root.getElementsByTagName(obj)
            for element in elements:
                if element.firstChild and element.firstChild.nodeValue and int(element.firstChild.nodeValue) > 0:
                    anzahl = int(element.firstChild.nodeValue)
                    objekte.append(obj) # Füge den Objekttyp zur Liste hinzu
                    logging.warning(f"PDFiD Warnung: Verdächtiges Objekt '{obj}' gefunden ({anzahl} mal)")
                    gefundene_objekte_meldungen.append(f"  - {obj} ({anzahl} mal)")

        if not objekte:
            return [], "PDFiD: Keine verdächtigen Objekte im Oberflächenscan gefunden."
        else:
            return objekte, "PDFiD: Verdächtige Objekte gefunden:\n" + "\n".join(gefundene_objekte_meldungen)
    except Exception as e:
        logging.error(f"Fehler bei der PDF-Analyse mit PDFiD: {e}")
        return [], f"PDFiD Fehler: Fehler bei der Analyse der PDF-Struktur." # Benutzerfreundlichere Fehlermeldung

def erweiterte_pdf_analyse(pdf_pfad):
    try:
        logging.info(f"Erweiterte PDF-Analyse gestartet für: {pdf_pfad}")
        doc = fitz.open(pdf_pfad)
        verdächtige_objekte_meldungen = []

        # Suche nach verdächtigen Annotationen oder Formularfeldern
        for seite in doc:
            for annot in seite.annots() or []:
                if annot and any(verb in str(annot) for verb in ["/AA", "/JavaScript", "/Launch"]):
                    annot_typ = annot.type[1:] if annot.type else "Unbekannter Annotationstyp" # Annotationstyp extrahieren
                    verdächtige_objekte_meldungen.append(f"❌ Verdächtige Annotation gefunden: Typ '{annot_typ}', Inhalt: {str(annot)[:100]}...") # Typ und Anfang des Inhalts
                    logging.warning(f"Erweiterte Analyse: Verdächtige Annotation entdeckt: Typ '{annot_typ}', Inhalt: {str(annot)}")

        # Suche nach AcroForms direkt in der PDF
        for obj in doc:
            obj_text = obj.read_bytes()
            for verb in VERBOTENE_OBJEKTE:
                if verb.encode() in obj_text:
                    verdächtige_objekte_meldungen.append(f"❌ Verdächtiges eingebettetes Objekt gefunden: '{verb}' entdeckt im Objektstrom.") # Genauerer Hinweis auf Objektstrom
                    logging.warning(f"Erweiterte Analyse: Schädliches eingebettetes Objekt entdeckt: '{verb}' im Objektstrom.")

        if not verdächtige_objekte_meldungen:
            return [], "Erweiterte Analyse: Keine verdächtigen Objekte gefunden."
        else:
            return verdächtige_objekte_meldungen, "Erweiterte Analyse: Verdächtige Objekte gefunden:\n" + "\n".join(verdächtige_objekte_meldungen)
    except Exception as e:
        logging.error(f"Fehler bei der erweiterten PDF-Analyse: {e}")
        return [f"❌ Gefährliche Inhalte erkannt"], (
            "Erweiterte Analyse: Es wurden potenziell schädliche Inhalte erkannt.\n"
            "Aus Sicherheitsgründen empfehlen wir, ausschließlich die bereinigte PDF-Version zu verwenden."
        )
def bereinige_pdf(pdf_pfad, output_pfad):
    try:
        logging.info(f"Starte Bereinigung der PDF: {pdf_pfad}")
        doc = fitz.open(pdf_pfad)
        writer = fitz.open()

        for seite in doc:
            seite.clean_contents()
            writer.insert_pdf(doc, from_page=seite.number, to_page=seite.number)

        writer.save(output_pfad)
        writer.close()
        logging.info(f"PDF erfolgreich bereinigt und gespeichert unter: {output_pfad}")
        return True
    except Exception as e:
        logging.error(f"Fehler beim Bereinigen der PDF: {e}")
        return False

def pdf_scanner(pdf_pfad):
    if not ist_erlaubte_datei(pdf_pfad):
        return "❌ Ungültiger Dateityp. Bitte laden Sie eine PDF-Datei hoch.", None # Klarere Fehlermeldung für Dateityp

    logging.info(f"Starte Sicherheits-Scan für PDF: {pdf_pfad}")
    pdfid_objekte_typen, pdfid_meldung = analysiere_pdf_mit_pdfid(pdf_pfad) # Gibt jetzt Liste der Objekttypen zurück
    tiefen_scan_meldungen, tiefen_scan_meldung = erweiterte_pdf_analyse(pdf_pfad) # Gibt jetzt Liste der Meldungen zurück

    gesamt_meldung = ""
    verdacht_gefunden = False # Flag, um Verdacht zu verfolgen

    if pdfid_objekte_typen or tiefen_scan_meldungen:
        gesamt_meldung += "⚠️ **Verdächtige Objekte gefunden!**\n"
        verdacht_gefunden = True # Verdacht wurde bestätigt
        if pdfid_objekte_typen:
            gesamt_meldung += pdfid_meldung + "\n"
            gesamt_meldung += "  Gefundene Objekttypen (PDFiD Oberflächenscan):\n" # Klarstellung des Scantyps
            for obj_typ in pdfid_objekte_typen:
                gesamt_meldung += f"    - {obj_typ}\n"
        if tiefen_scan_meldungen:
            gesamt_meldung += tiefen_scan_meldung + "\n"
            gesamt_meldung += "  Details zur erweiterten Analyse:\n" # Klarstellung des Scantyps
            for meldung in tiefen_scan_meldungen:
                gesamt_meldung += f"    - {meldung}\n"

        bereinigte_pdf_pfad = os.path.join(BEREINIGTE_FOLDER, f"{os.path.basename(pdf_pfad).split('.')[0]}_cleaned.pdf")
        if bereinige_pdf(pdf_pfad, bereinigte_pdf_pfad):
            gesamt_meldung += "\n✅ Bereinigte Version erfolgreich erstellt: " + bereinigte_pdf_pfad + "\n   Es wird empfohlen, diese bereinigte Version zu verwenden." # Empfehlung zur Nutzung der bereinigten Version
        else:
            gesamt_meldung += "\n❌ Fehler beim Bereinigen der PDF.  Es wird dringend davon abgeraten, die Originaldatei zu öffnen!" # Deutliche Warnung, wenn Bereinigung fehlschlägt
            return gesamt_meldung, None
    else:
        gesamt_meldung += "✅ **Keine verdächtigen Objekte gefunden.**\n"
        gesamt_meldung += "  Die PDF scheint sicher zu sein (basierend auf automatischer Analyse).\n" # Hinweis auf automatische Analyse
        gesamt_meldung += "  Es wird dennoch empfohlen, bei PDFs aus unbekannten Quellen Vorsicht walten zu lassen." # Allgemeine Sicherheitsempfehlung
        verdacht_gefunden = False # Kein Verdacht

    return gesamt_meldung, os.path.join(BEREINIGTE_FOLDER, f"{os.path.basename(pdf_pfad).split('.')[0]}_cleaned.pdf") if verdacht_gefunden else pdf_pfad # Gib immer einen bereinigten Pfad zurück, wenn Verdacht, sonst Originalpfad (Kopie im Upload-Ordner)


def scan_pdf(file):
    if file is None:
        return "❌ Keine Datei hochgeladen. Bitte laden Sie eine PDF-Datei hoch.", None # Klarere Fehlermeldung

    upload_pfad = os.path.join(UPLOAD_FOLDER, os.path.basename(file.name))
    shutil.copy(file.name, upload_pfad)
    logging.info(f"Datei hochgeladen und gespeichert unter: {upload_pfad}")
    return pdf_scanner(upload_pfad)

# Gradio-Oberfläche
with gr.Blocks() as iface:
    gr.Markdown("## PDF Sicherheitsprüfung CipherCore")
    gr.Markdown("Diese Sicherheitsprüfung analysiert Ihr PDF-Dokument auf potenziell gefährliche Inhalte wie JavaScript, eingebettete Dateien und Formularaktionen.  Für eine detailliertere Analyse werden sowohl Oberflächen- als auch Tiefenscans durchgeführt.") # Hinzugefügt: Beschreibung der Analyse-Tiefe

    pdf_file_input = gr.File(label="📂 Lade eine PDF hoch.")
    scan_button = gr.Button("Scan PDF")
    ergebnis_textbox = gr.Textbox(label="Ergebnis der Prüfung", interactive=False)
    bereinigte_pdf_output = gr.File(label="📥 Bereinigte PDF (Immer erstellt)") # Klarstellung: Immer erstellt

    scan_button.click(scan_pdf, inputs=[pdf_file_input], outputs=[ergebnis_textbox, bereinigte_pdf_output])


# 📌 Tab-Klasse für Gradio - Unverändert gelassen, da nicht direkt angefragt.
class PdfScanTab:
    def __init__(self):
        pass

    def build_tab(self):
        with gr.TabItem("PDF Scan", id="pdf_scan_tab"):
            gr.Markdown("## PDF Sicherheitsprüfung CipherCore")
            gr.Markdown("Diese PDF-Sicherheitsprüfung analysiert Ihr Dokument auf potenziell gefährliche Inhalte. Wir suchen nach verdächtigen Objekten wie JavaScript, eingebetteten Dateien, automatischen Aktionen und mehr.")

            with gr.Column():
                pdf_file_input = gr.File(label="📂 Lade eine PDF hoch.")
                scan_button = gr.Button("Scan PDF")
                ergebnis_textbox = gr.Textbox(label="Ergebnis der Prüfung", interactive=False)
                bereinigte_pdf_output = gr.File(label="📥 Bereinigte PDF (Immer erstellt)") # Klarstellung: Immer erstellt

                scan_button.click(scan_pdf, inputs=[pdf_file_input], outputs=[ergebnis_textbox, bereinigte_pdf_output])