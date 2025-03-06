#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modul: tab_prompt_optimization.py
Dieses Modul enthält die Klasse PromptOptimizationTab, die den UI-Block für die Prompt-Optimierung
als Tab für eine modulare Gradio-Oberfläche bereitstellt.
Entwickelt von CipherCore.
"""

import gradio as gr
import base64
import os  # Importiere das os-Modul
from dotenv import load_dotenv  # Importiere load_dotenv
from gemini_app import GeminiApp
import google.generativeai as genai  # Import genai hier

# Lade die Umgebungsvariablen aus der .env-Datei
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class PromptOptimizationTab:
    def __init__(self, app: GeminiApp):
        """
        Initialisiert den PromptOptimizationTab mit einer Instanz der GeminiApp.
        """
        self.app = app

    def build_tab(self):
        """
        Baut den UI-Block für den Prompt-Optimierungstab.
        """
        with gr.TabItem("KI-Prompt-Optimierung"):
            gr.Markdown("# 🤖 KI-Prompt-Optimierung mit Google Gemini - CipherCore App")
            gr.Markdown("#### *Diese App wurde von CipherCore entwickelt, um die im Buch 'Die Kunst des Prompting' erlernten Techniken direkt anzuwenden.*")
            gr.Markdown("[**Buch Download: Die Kunst des Prompting**](https://github.com/CipherCorePro/gemini-gradio-app/blob/main/Die%20Kunst%20des%20Prompting.pdf)")

            with gr.Column():
                gr.Markdown("### 🔍 Gib einen Prompt ein, den du optimieren möchtest:")
                user_prompt = gr.TextArea(label="Dein Prompt", value="Erkläre mir die Relativitätstheorie.")

                gr.Markdown("### 🎭 Wähle den Stil der Optimierung")
                style = gr.Radio(
                    ["Professionell", "Kreativ", "Detailliert", "Wissenschaftlich", "Storytelling", "FAQ-Stil", "Lehrbuch-Stil"],
                    value="Professionell", label="In welchem Stil soll die Optimierung erfolgen?"
                )

                # API-Key Feld entfernt, da er aus .env geladen wird
                # api_key_gemini = gr.Textbox(type="password", label="Google Gemini API-Key", placeholder="API-Key hier eingeben (optional, kann auch in Sidebar sein)")

                optimize_button = gr.Button("✨ KI-Prompt optimieren mit Gemini")

                with gr.Row():
                    with gr.Column():
                        original_prompt_output = gr.Markdown("📝 **Original-Prompt**")
                        original_prompt_text_output = gr.Textbox(label="Original Prompt Text", interactive=False)
                    with gr.Column():
                        optimized_prompt_output = gr.Markdown("✅ **Optimierter Prompt (durch Gemini)**")
                        optimized_prompt_text_output = gr.Textbox(label="Optimierter Prompt Text", interactive=False)

                evaluation_output = gr.Markdown("📊 KI-Bewertung der Optimierung")

                gr.Markdown("### 📤 Exportiere deinen optimierten Prompt")
                export_format = gr.Radio(
                    ["Markdown"],  # Zukünftig PDF hinzufügen
                    value="Markdown", label="Wähle das Exportformat:"
                )

                export_markdown_link = gr.HTML()

                def optimize_prompt_click(prompt, style_name): # API-Key Parameter entfernt
                    # Kein API-Key Input mehr notwendig, da er aus .env geladen wird
                    # if not api_key:
                    #     return "Bitte gib deinen Google Gemini API-Schlüssel ein.", "", "", "", ""

                    genai.configure(api_key=GEMINI_API_KEY) # Verwende den API-Key aus der Umgebungsvariable

                    style_instructions = {
                        "Professionell": "Verwende eine präzise, sachliche und formale Ausdrucksweise.",
                        "Kreativ": "Formuliere den Prompt mit einer kreativen, interessanten und einprägsamen Sprache.",
                        "Detailliert": "Erweitere den Prompt um zusätzliche Informationen, Details und Kontext.",
                        "Wissenschaftlich": "Optimiere den Prompt für eine wissenschaftliche Anfrage. Verwende Fachterminologie und einen objektiven Ton.",
                        "Storytelling": "Gestalte den Prompt so, dass er eine Geschichte erzählt oder eine narrative Antwort hervorruft.",
                        "FAQ-Stil": "Formuliere den Prompt als Frage im FAQ-Stil, um prägnante und informative Antworten zu erhalten.",
                        "Lehrbuch-Stil": "Optimiere den Prompt, um eine Antwort im Stil eines Lehrbuchs zu erhalten, mit klaren Erklärungen und Definitionen."
                    }

                    client = genai.GenerativeModel("gemini-2.0-flash")

                    def extract_text(response):
                        if response and response.candidates:
                            parts = response.candidates[0].content.parts
                            return "\n".join([p.text for p in parts if p.text])
                        return "Fehler: Keine Antwort erhalten."

                    def optimize_prompt_with_gemini(prompt_to_optimize, optimization_style):
                        response = client.generate_content(
                            f"Verbessere diesen Prompt, indem du ihn klarer, präziser und effektiver formulierst. "
                            f"Vermeide vage Begriffe und füge ggf. Kontext oder Formatierung hinzu. "
                            f"Hier ist der ursprüngliche Prompt: {prompt_to_optimize} "
                            f"Optimiere ihn im Stil: {optimization_style}. {style_instructions[optimization_style]}"
                        )
                        return extract_text(response)

                    def evaluate_prompt_with_gemini(original_prompt, optimized_prompt):
                        response = client.generate_content(
                            f"Vergleiche den folgenden Original-Prompt mit der optimierten Version. "
                            f"Bewerte die Verbesserungen hinsichtlich Klarheit, Struktur und Relevanz auf einer Skala von 1 bis 10. "
                            f"Original-Prompt: {original_prompt} "
                            f"Optimierter Prompt: {optimized_prompt}"
                        )
                        return extract_text(response)

                    optimized_prompt_text = optimize_prompt_with_gemini(prompt, style_name)
                    evaluation_text = evaluate_prompt_with_gemini(prompt, optimized_prompt_text)

                    markdown_text = f"""
                    # Optimierter Prompt

                    **Original Prompt:**
                    {prompt}

                    **Optimierter Prompt ({style_name}):**
                    {optimized_prompt_text}
                    """
                    b64 = base64.b64encode(markdown_text.encode()).decode()
                    href = f'<a href="data:file/markdown;base64,{b64}" download="optimierter_prompt.md">💾 Als Markdown herunterladen</a>'

                    return prompt, optimized_prompt_text, evaluation_text, href # Leere Warnung entfernt

                def update_export_link(format_name, original_prompt, optimized_prompt, style_name):
                    if format_name == "Markdown":
                        markdown_text = f"""
                        # Optimierter Prompt

                        **Original Prompt:**
                        {original_prompt}

                        **Optimierter Prompt ({style_name}):**
                        {optimized_prompt}
                        """
                        b64 = base64.b64encode(markdown_text.encode()).decode()
                        href = f'<a href="data:file/markdown;base64,{b64}" download="optimierter_prompt.md">💾 Als Markdown herunterladen</a>'
                        return href
                    return ""

                optimize_button.click(
                    optimize_prompt_click,
                    inputs=[user_prompt, style], # API-Key Input entfernt
                    outputs=[original_prompt_text_output, optimized_prompt_text_output, evaluation_output, export_markdown_link]
                )

                export_format.change(
                    update_export_link,
                    inputs=[export_format, original_prompt_text_output, optimized_prompt_text_output, style],
                    outputs=[export_markdown_link]
                )

    def run(self):
        """
        Startet die Prompt-Optimierungsschnittstelle als eigenständige Gradio-Anwendung.
        """
        demo = gr.Blocks(title="KI-Prompt-Optimierung - Standalone - CipherCore")
        with demo:
            PromptOptimizationTab(GeminiApp()).build_tab() # Erstelle eine GeminiApp Instanz für Standalone
        demo.launch()

if __name__ == "__main__":
    prompt_opt_tab = PromptOptimizationTab(GeminiApp()) # Erstelle eine GeminiApp Instanz
    prompt_opt_tab.run()