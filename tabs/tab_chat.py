#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modul: tab_chat.py
Dieses Modul enthält die Klasse ChatTab, die den UI-Block für Chat & Bildanalyse
sowohl als eigenständige Anwendung als auch als Tab bereitstellt.
Erstellt von CipherCore.
"""

import gradio as gr
from gemini_app import GeminiApp

class ChatTab:
    def __init__(self, app: GeminiApp):
        self.app = app

    def build_tab(self):
        with gr.TabItem("Chat & Bildanalyse"):
            gr.Markdown("## CipherCore - Chat & Bildanalyse\nGib eine Chat-ANFRAGE ein und (optional) lade ein Bild hoch, das analysiert werden soll.")
            with gr.Row():
                prompt_chat = gr.Textbox(label="ANFRAGE", placeholder="Deine Frage an die KI")
                image_input = gr.Image(label="Bild hochladen (optional)")
            output_chat = gr.Textbox(label="Antwort der KI", interactive=False)
            btn_chat = gr.Button("Senden")
            btn_chat.click(fn=self.app.process_chat, inputs=[prompt_chat, image_input], outputs=output_chat)

    def run(self):
        demo = gr.Blocks(title="CipherCore - Chat & Bildanalyse - Standalone")
        with demo:
            gr.Markdown("## CipherCore - Chat & Bildanalyse (Standalone)\nGib eine Chat-ANFRAGE ein und (optional) lade ein Bild hoch, das analysiert werden soll.")
            with gr.Row():
                prompt_chat = gr.Textbox(label="ANFRAGE", placeholder="Deine Frage an die KI")
                image_input = gr.Image(label="Bild hochladen (optional)")
            output_chat = gr.Textbox(label="Antwort der KI", interactive=False)
            btn_chat = gr.Button("Senden")
            btn_chat.click(fn=self.app.process_chat, inputs=[prompt_chat, image_input], outputs=output_chat)
        demo.launch()

if __name__ == "__main__":
    app = GeminiApp()
    chat_tab = ChatTab(app)
    chat_tab.run()