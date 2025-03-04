#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modul: tab_dalle.py
Dieses Modul enthält die Klasse DalleTab, die die Schnittstelle für die DALL·E Bildgenerierung und -transformation
sowohl als eigenständige Anwendung als auch als Tab bereitstellt.
"""

import os
import gradio as gr
from PIL import Image
from gemini_app import GeminiApp

class DalleTab:
    def __init__(self, app: GeminiApp):
        self.app = app

    def build_tab(self):
        with gr.TabItem("Bildgenerierung (DALL·E)"):
            gr.Markdown("## DALL·E 3 Bildgenerierung\nErstellt von **CipherCore**\nErstelle ein Bild über OpenAI DALL·E und transformiere es.")
            with gr.Row():
                with gr.Column():
                    dalle_button = gr.Button("Generiere DALL·E Bild (1024x1024)")
                    prompt_input = gr.Textbox(label="ANFRAGE für DALL·E", value="Hier dein Text")
                    input_image = gr.Image(label="Eingabebild")
                    brightness_slider = gr.Slider(minimum=-1, maximum=1, value=0.0, step=0.05, label="Helligkeit")
                    contrast_slider = gr.Slider(minimum=0.5, maximum=2.0, value=1.3, step=0.05, label="Kontrast")
                    resolution_dropdown = gr.Dropdown(
                        choices=[
                            "HD", "Full HD", "2K (Standard)", "2K (Quad HD)", "2K (3840x1080)",
                            "2K (3840x2160) Scaled", "2K (3840x3840)", "Original (2K)",
                            "4K (Standard)", "4K (Full Aperture)", "4K (DCI)", "4K (3840x1600)",
                            "4K (3840x2400)", "4K (3840x3840)", "4K", "8K (Standard)",
                            "8K (Full Aperture)", "8K (3840x3840) Scaled", "8K (7680x3200)",
                            "8K (7680x4800)", "8K (7680x7680)", "8K", "Cover", "TikTok",
                            "Facebook Post", "Facebook Story", "YouTube Thumbnail", "YouTube Short",
                            "Instagram Post", "Instagram Story"
                        ],
                        value="Full HD", label="Auflösung"
                    )
                    generate_button = gr.Button("Transformiere Bild")
                with gr.Column():
                    original_output = gr.Image(label="Eingabebild")
                    generated_output = gr.Image(label="Generiertes Bild")
            def dalle_to_image(prompt: str):
                img = self.app.generate_dalle_image(prompt=prompt, size="1024x1024")
                if img is None:
                    return None
                return img
            dalle_button.click(fn=dalle_to_image, inputs=prompt_input, outputs=input_image)
            input_params = [input_image, brightness_slider, contrast_slider, resolution_dropdown]
            output_params = [original_output, generated_output]
            generate_button.click(fn=self.app.process_inputs, inputs=input_params, outputs=output_params)
            # Falls ein generiertes Bild bereits existiert, laden
            generated_image_path = "kunst.webp" # Korrekter Dateiname
            if os.path.exists(generated_image_path):
                loaded_img = self.app.load_image_from_file(generated_image_path)
                if loaded_img:
                    generated_output.value = loaded_img

    def run(self):
        demo = gr.Blocks(title="Bildgenerierung (DALL·E) - Standalone")
        with demo:
            gr.Markdown("## DALL·E 3 Bildgenerierung (Standalone)\nErstellt von **CipherCore**\nErstelle ein Bild über OpenAI DALL·E und transformiere es.")
            with gr.Row():
                with gr.Column():
                    dalle_button = gr.Button("Generiere DALL·E Bild (1024x1024)")
                    prompt_input = gr.Textbox(label="ANFRAGE für DALL·E", value="Hier dein Text")
                    input_image = gr.Image(label="Eingabebild")
                    brightness_slider = gr.Slider(minimum=-1, maximum=1, value=0.0, step=0.05, label="Helligkeit")
                    contrast_slider = gr.Slider(minimum=0.5, maximum=2.0, value=1.3, step=0.05, label="Kontrast")
                    resolution_dropdown = gr.Dropdown(
                        choices=[
                            "HD", "Full HD", "2K (Standard)", "2K (Quad HD)", "2K (3840x1080)",
                            "2K (3840x2160) Scaled", "2K (3840x3840)", "Original (2K)",
                            "4K (Standard)", "4K (Full Aperture)", "4K (DCI)", "4K (3840x1600)",
                            "4K (3840x2400)", "4K (3840x3840)", "4K", "8K (Standard)",
                            "8K (Full Aperture)", "8K (3840x3840) Scaled", "8K (7680x3200)",
                            "8K (7680x4800)", "8K (7680x7680)", "8K", "Cover", "TikTok",
                            "Facebook Post", "Facebook Story", "YouTube Thumbnail", "YouTube Short",
                            "Instagram Post", "Instagram Story"
                        ],
                        value="Full HD", label="Auflösung"
                    )
                    generate_button = gr.Button("Transformiere Bild")
                with gr.Column():
                    original_output = gr.Image(label="Eingabebild")
                    generated_output = gr.Image(label="Generiertes Bild")
            def dalle_to_image_standalone(prompt: str):
                img = self.app.generate_dalle_image(prompt=prompt, size="1024x1024")
                if img is None:
                    return None
                return img
            dalle_button.click(fn=dalle_to_image_standalone, inputs=prompt_input, outputs=input_image)
            input_params = [input_image, brightness_slider, contrast_slider, resolution_dropdown]
            output_params = [original_output, generated_output]
            generate_button.click(fn=self.app.process_inputs, inputs=input_params, outputs=output_params)
        demo.launch()

if __name__ == "__main__":
    app = GeminiApp()
    dalle_tab = DalleTab(app)
    dalle_tab.run()