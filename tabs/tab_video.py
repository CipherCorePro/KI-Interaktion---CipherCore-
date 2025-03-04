#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modul: tab_video.py
Dieses Modul enthält die Klasse VideoTab für die Videoanalyse – eigenständig ausführbar und integrierbar.
Entwickelt von CipherCore für höchste Sicherheitsstandards in der Programmierung.
"""

import gradio as gr
from gemini_app import GeminiApp

class VideoTab:
    def __init__(self, app: GeminiApp):
        self.app = app

    def build_tab(self):
        with gr.TabItem("Videoanalyse"):
            gr.Markdown(
                "## Videoanalyse von CipherCore\n"
                "Gib eine ANFRAGE ein und lade ein Video hoch, das analysiert werden soll.\n\n"
                "**Hinweis:** Das Video darf maximal 20 MB groß sein."
            )
            with gr.Row():
                prompt_video = gr.Textbox(label="ANFRAGE", placeholder="z.B. 'Beschreibe den Inhalt dieses Videos'")
                video_input = gr.Video(label="Video hochladen")
            output_video = gr.Textbox(label="Antwort der KI", interactive=False)
            btn_video = gr.Button("Senden")
            btn_video.click(fn=self.app.process_video, inputs=[prompt_video, video_input], outputs=output_video)

    def run(self):
        demo = gr.Blocks(title="Videoanalyse - CipherCore")
        with demo:
            gr.Markdown(
                "## Videoanalyse (Standalone) von CipherCore\n"
                "Gib eine ANFRAGE ein und lade ein Video hoch, das analysiert werden soll.\n\n"
                "**Hinweis:** Das Video darf maximal 20 MB groß sein."
            )
            with gr.Row():
                prompt_video = gr.Textbox(label="ANFRAGE", placeholder="z.B. 'Beschreibe den Inhalt dieses Videos'")
                video_input = gr.Video(label="Video hochladen")
            output_video = gr.Textbox(label="Antwort der KI", interactive=False)
            btn_video = gr.Button("Senden")
            btn_video.click(fn=self.app.process_video, inputs=[prompt_video, video_input], outputs=output_video)
        demo.launch()

if __name__ == "__main__":
    app = GeminiApp()
    video_tab = VideoTab(app)
    video_tab.run()