#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modul: tab_audio.py
Dieses Modul enthält die Klasse AudioTab, die den UI-Block für die Audio-Interaktion
sowohl als eigenständige Gradio-Anwendung als auch als Tab für eine modulare Oberfläche bereitstellt.
Entwickelt von CipherCore.
"""

import gradio as gr
from gemini_app import GeminiApp

class AudioTab:
    def __init__(self, app: GeminiApp):
        """
        Initialisiert den AudioTab mit einer Instanz der GeminiApp.
        """
        self.app = app

    def build_tab(self):
        """
        Baut den UI-Block für den Audio-Interaktionstab, der in ein übergeordnetes Tabs-Interface eingebunden werden kann.
        """
        with gr.TabItem("Audio-Interaktion"):
            gr.Markdown(
                "## Audio-Interaktion\n"
                "Entwickelt von CipherCore für sichere Programmierung.\n\n"
                "Lade eine Audiodatei hoch und gib eine ANFRAGE ein.\n\n"
                "**Hinweis:** Die Audiodatei darf maximal 4 MB groß sein."
            )
            with gr.Row():
                prompt_audio = gr.Textbox(label="ANFRAGE", placeholder="z.B. 'Erstelle ein Transkript des Audioclips'")
                audio_input = gr.Audio(label="Audiodatei hochladen", type="filepath")
            output_audio = gr.Textbox(label="Antwort der KI", interactive=False)
            btn_audio = gr.Button("Senden")
            btn_audio.click(fn=self.app.process_audio, inputs=[prompt_audio, audio_input], outputs=output_audio)

    def run(self):
        """
        Startet die Audio-Interaktionsschnittstelle als eigenständige Gradio-Anwendung.
        """
        demo = gr.Blocks(title="Audio-Interaktion - Standalone - CipherCore")
        with demo:
            gr.Markdown(
                "## Audio-Interaktion (Standalone)\n"
                "Entwickelt von CipherCore für sichere Programmierung.\n\n"
                "Lade eine Audiodatei hoch und gib eine ANFRAGE ein.\n\n"
                "**Hinweis:** Die Audiodatei darf maximal 4 MB groß sein."
            )
            with gr.Row():
                prompt_audio = gr.Textbox(label="ANFRAGE", placeholder="z.B. 'Erstelle ein Transkript des Audioclips'")
                audio_input = gr.Audio(label="Audiodatei hochladen", type="filepath")
            output_audio = gr.Textbox(label="Antwort der KI", interactive=False)
            btn_audio = gr.Button("Senden")
            btn_audio.click(fn=self.app.process_audio, inputs=[prompt_audio, audio_input], outputs=output_audio)
        demo.launch()

if __name__ == "__main__":
    app = GeminiApp()
    audio_tab = AudioTab(app)
    audio_tab.run()