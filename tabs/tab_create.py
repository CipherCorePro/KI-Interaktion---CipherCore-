#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modul: tab_create.py
Dieses Modul enthält die Klasse CreateTab, die die Schnittstelle für Inhaltserstellung
und Export sowohl als eigenständige Anwendung als auch als Tab bereitstellt.
Entwickelt von CipherCore - Sicherheit in der Programmierung.
"""

import gradio as gr
from gemini_app import GeminiApp

class CreateTab:
    def __init__(self, app: GeminiApp):
        self.app = app

    def build_tab(self):
        with gr.TabItem("Inhaltserstellung & Export"):
            gr.Markdown(
                "## Inhaltserstellung & Export\n"
                "von **CipherCore** - Sicherheit in der Programmierung\n\n"
                "Gib eine ANFRAGE ein, um mit der KI einen Inhalt zu erstellen. Wähle anschließend das gewünschte Exportformat aus, "
                "und der Inhalt wird als Datei gespeichert.\n\n"
                "Exportformate: Word, Excel, CSV, PDF."
            )
            with gr.Row():
                prompt_create = gr.Textbox(label="ANFRAGE", placeholder="z.B. 'Erstelle einen Bericht über ...'")
                export_format = gr.Dropdown(label="Exportformat", choices=["Word", "Excel", "CSV", "PDF"], value="Word")
            output_create = gr.File(label="Herunterladen")
            btn_create = gr.Button("Erstellen und Exportieren")
            btn_create.click(fn=self.app.process_create, inputs=[prompt_create, export_format], outputs=output_create)

    def run(self):
        demo = gr.Blocks(title="Inhaltserstellung & Export - Standalone")
        with demo:
            gr.Markdown(
                "## Inhaltserstellung & Export (Standalone)\n"
                "von **CipherCore** - Sicherheit in der Programmierung\n\n"
                "Gib eine ANFRAGE ein, um mit der KI einen Inhalt zu erstellen. Wähle anschließend das gewünschte Exportformat aus, "
                "und der Inhalt wird als Datei gespeichert.\n\n"
                "Exportformate: Word, Excel, CSV, PDF."
            )
            with gr.Row():
                prompt_create = gr.Textbox(label="ANFRAGE", placeholder="z.B. 'Erstelle einen Bericht über ...'")
                export_format = gr.Dropdown(label="Exportformat", choices=["Word", "Excel", "CSV", "PDF"], value="Word")
            output_create = gr.File(label="Herunterladen")
            btn_create = gr.Button("Erstellen und Exportieren")
            btn_create.click(fn=self.app.process_create, inputs=[prompt_create, export_format], outputs=output_create)
        demo.launch()

if __name__ == "__main__":
    app = GeminiApp()
    create_tab = CreateTab(app)
    create_tab.run()