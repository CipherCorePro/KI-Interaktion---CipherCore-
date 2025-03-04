#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modul: tab_file.py
Dieses Modul enthält die Klasse FileTab, die die Dateianalyse-Schnittstelle
sowohl als eigenständige Anwendung als auch als Tab bereitstellt.
Entwickelt von CipherCore für höchste Sicherheitsstandards in der Programmierung.
"""

import gradio as gr
from gemini_app import GeminiApp

class FileTab:
    def __init__(self, app: GeminiApp):
        self.app = app

    def build_tab(self):
        with gr.TabItem("CipherCore Dateianalyse"):
            gr.Markdown(
                "## CipherCore Dateianalyse\n"
                "Entwickelt von CipherCore für höchste Sicherheitsstandards.\n\n"
                "Gib eine ANFRAGE ein und lade eine Datei hoch. Unterstützte Dateitypen sind:\n\n"
                "• Plain Text (TXT)\n"
                "• Code-Dateien (C, CPP, PY, JAVA, PHP, SQL, HTML)\n"
                "• Dokumente (DOC, DOCX, PDF, RTF, DOT, DOTX, HWP, HWPX) sowie Google Docs\n"
                "• Tabellarische Daten (CSV, TSV)\n"
                "• Tabellenkalkulationen (XLS, XLSX) sowie Google Sheets\n\n"
                "**Hinweis:** Die Dateigröße darf maximal 4 MB betragen."
            )
            with gr.Row():
                prompt_file = gr.Textbox(label="ANFRAGE", placeholder="z.B. 'Fasse den Inhalt der Datei zusammen'")
                file_input = gr.File(label="Datei hochladen")
            output_file = gr.Textbox(label="Antwort der Gemini KI", interactive=False)
            btn_file = gr.Button("Senden")
            btn_file.click(fn=self.app.process_file, inputs=[prompt_file, file_input], outputs=output_file)

    def run(self):
        demo = gr.Blocks(title="CipherCore Dateianalyse - Standalone")
        with demo:
            gr.Markdown(
                "## CipherCore Dateianalyse (Standalone)\n"
                "Entwickelt von CipherCore für höchste Sicherheitsstandards.\n\n"
                "Gib eine ANFRAGE ein und lade eine Datei hoch. Unterstützte Dateitypen sind:\n\n"
                "• Plain Text (TXT)\n"
                "• Code-Dateien (C, CPP, PY, JAVA, PHP, SQL, HTML)\n"
                "• Dokumente (DOC, DOCX, PDF, RTF, DOT, DOTX, HWP, HWPX)\n"
                "• Tabellarische Daten (CSV, TSV)\n"
                "• Tabellenkalkulationen (XLS, XLSX)\n\n"
                "**Hinweis:** Die Dateigröße darf maximal 4 MB betragen."
            )
            with gr.Row():
                prompt_file = gr.Textbox(label="ANFRAGE", placeholder="z.B. 'Fasse den Inhalt der Datei zusammen'")
                file_input = gr.File(label="Datei hochladen")
            output_file = gr.Textbox(label="Antwort der Gemini KI", interactive=False)
            btn_file = gr.Button("Senden")
            btn_file.click(fn=self.app.process_file, inputs=[prompt_file, file_input], outputs=output_file)
        demo.launch()

if __name__ == "__main__":
    app = GeminiApp()
    file_tab = FileTab(app)
    file_tab.run()