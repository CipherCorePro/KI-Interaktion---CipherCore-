#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.py
Hauptprogramm zur Ausführung der modularisierten Gradio App mit mehreren Tabs.
Jeder Tab ist als eigenständiges Modul implementiert und kann auch separat ausgeführt werden.
Erstellt von CipherCore.
"""

import gradio as gr
from gemini_app import GeminiApp
from tabs.tab_audio import AudioTab
from tabs.tab_chat import ChatTab
from tabs.tab_video import VideoTab
from tabs.tab_file import FileTab
from tabs.tab_create import CreateTab
from tabs.tab_dalle import DalleTab
from tabs.tab_info import InfoTab
from tabs.tab_training import TrainingTabs
from tabs.tab_mitarbeitertest import MitarbeiterTestEUAIAct
from tabs.tab_pdf_scan import PdfScanTab
from tabs.tab_agent_convo import AgentConversationTab # Importiere den neuen Tab!


def main():
    app = GeminiApp()
    demo = gr.Blocks(title="KI Interaktion - CipherCore")
    with demo:
        gr.Markdown("# KI Interaktion - CipherCore\nWähle einen Modus zur Interaktion mit der KI:")
        with gr.Tabs():
            AudioTab(app).build_tab()
            ChatTab(app).build_tab()
            VideoTab(app).build_tab()
            FileTab(app).build_tab()
            CreateTab(app).build_tab()
            DalleTab(app).build_tab()
            InfoTab().build_tab()
            TrainingTabs().build_tab()
            MitarbeiterTestEUAIAct().build_tab()
            PdfScanTab().build_tab()
            AgentConversationTab().build_tab() # Füge den AgentConversationTab hier hinzu!
    demo.launch(share=True)

if __name__ == "__main__":
    main()