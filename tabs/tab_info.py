
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modul: tab_info.py
Dieses Modul enthält die Klasse InfoTab, die den Informations-Tab mit Hinweisen und Warnungen zur Arbeit mit KI
sowie spezifische Informationen zum neuen AI Act Europa und zur Mitarbeiterschulung in Untertabs bereitstellt.
"""

import gradio as gr

class InfoTab:
    def build_tab(self):
        with gr.TabItem("Info"):
            gr.Markdown(
                """
                # Wichtige Hinweise und Warnungen zur Arbeit mit Künstlicher Intelligenz (KI)
                **Erstellt von CipherCore**

                **Haftungsausschluss:**
                - Die von der KI generierten Inhalte sind automatisiert und können Fehler oder Unstimmigkeiten enthalten.
                - Es wird dringend empfohlen, alle Ergebnisse kritisch zu prüfen und gegebenenfalls zu validieren.

                **Verantwortungsvoller Umgang:**
                - Verwende die KI-Tools ausschließlich für den vorgesehenen Zweck.
                - Vermeide den Einsatz von KI zur Erstellung von schädlichen, diskriminierenden oder illegalen Inhalten.
                - Denke daran: Die KI ist ein Hilfsmittel und kein Ersatz für menschliche Expertise.

                **Datenschutz und Sicherheit:**
                - Gib keine sensiblen oder personenbezogenen Daten in die KI-Systeme ein, sofern nicht ausdrücklich zugelassen.
                - Die Nutzung der APIs erfolgt auf eigenes Risiko. Achte darauf, dass alle Eingaben datenschutzkonform sind.

                **Rechtliche Hinweise:**
                - Die Nutzung der KI und der zugehörigen APIs unterliegt den Nutzungsbedingungen der jeweiligen Anbieter.
                - Beachte bei der Weitergabe von Inhalten stets die geltenden Urheberrechte und Lizenzbestimmungen.

                **Technische Hinweise:**
                - KI-Modelle können in manchen Fällen kontextbezogene oder fachlich korrekte Ergebnisse nicht garantieren.
                - Änderungen oder Anpassungen an den Ergebnissen sollten stets von Fachleuten überprüft werden.
                - Bei der Integration in produktive Umgebungen ist Vorsicht geboten, da unvorhergesehene Fehler auftreten können.

                **Zusätzliche Warnungen:**
                - Die KI ist ein Werkzeug, das bei unsachgemäßer Verwendung zu unerwünschten Ergebnissen führen kann.
                - Nutze die bereitgestellten Tools immer mit Bedacht und reflektiert.
                - Diese Hinweise dienen als allgemeiner Leitfaden und erheben keinen Anspruch auf Vollständigkeit oder Rechtsgültigkeit.

                ---
                *Hinweis: Diese Informationen sollen Dir helfen, die Risiken und Verantwortlichkeiten beim Einsatz von KI besser zu verstehen. Bitte informiere Dich regelmäßig über aktuelle Entwicklungen und Best Practices im Bereich der Künstlichen Intelligenz.*
                """
            )
            # Untertabs für spezifische Themen
            with gr.Tabs():
                with gr.TabItem("Allgemein"):
                    gr.Markdown(
                        """
                        ## Allgemeine Hinweise

                        Hier findest Du allgemeine Informationen zum verantwortungsvollen Umgang mit KI,
                        den Risiken bei der Nutzung von KI-Tools sowie grundlegende Sicherheitshinweise.

                        **Wichtige Punkte:**
                        - Überprüfe KI-Ergebnisse kritisch.
                        - Nutze die Systeme nur im vorgesehenen Rahmen.
                        - Informiere Dich regelmäßig über Neuerungen und Best Practices.
                        """
                    )
                with gr.TabItem("AI Act Europa"):
                    gr.Markdown(
                        """
                        ## Neuer AI Act Europa

                        Seit Februar in Kraft getreten, regelt der neue AI Act in Europa den Einsatz von Künstlicher Intelligenz.
                        **Wichtige Aspekte:**
                        - **Transparenz:** KI-Systeme müssen nachvollziehbar und transparent sein.
                        - **Sicherheit:** Es gelten strenge Anforderungen an die Sicherheit und Zuverlässigkeit der Systeme.
                        - **Risikomanagement:** Unternehmen sind verpflichtet, Risiken zu bewerten und geeignete Maßnahmen zur Risikominimierung zu ergreifen.
                        - **Compliance:** Es müssen Maßnahmen ergriffen werden, um sicherzustellen, dass alle KI-Anwendungen den gesetzlichen Vorgaben entsprechen.

                        **Empfehlungen:**
                        - Informiere Dich regelmäßig über Updates und Leitlinien des AI Act.
                        - Prüfe, ob Deine KI-Anwendungen den neuen Anforderungen entsprechen.
                        """
                    )
                with gr.TabItem("Mitarbeiterschulung"):
                    gr.Markdown(
                        """
                        ## Mitarbeiterschulung für KI

                        Angesichts der zunehmenden Bedeutung von KI im Unternehmen ist es essenziell, dass Mitarbeiter im Umgang mit KI geschult werden.
                        **Schulungsinhalte sollten umfassen:**
                        - Grundlagen der Künstlichen Intelligenz und maschinelles Lernen.
                        - Verantwortungsbewusster und sicherer Einsatz von KI-Systemen.
                        - Rechtliche Rahmenbedingungen (z. B. AI Act Europa) und ethische Aspekte.
                        - Praktische Anwendung und Interpretation von KI-Ergebnissen.

                        **Vorteile einer umfassenden Schulung:**
                        - Verbesserung der Fehlererkennung und -behebung.
                        - Erhöhung der Akzeptanz und des verantwortungsvollen Einsatzes von KI.
                        - Sicherstellung, dass das Unternehmen den gesetzlichen Anforderungen entspricht.

                        Es wird empfohlen, regelmäßige Schulungen und Weiterbildungen anzubieten, um alle Mitarbeiter stets auf dem neuesten Stand zu halten.
                        """
                    )
                with gr.TabItem("Impressum"):
                    gr.Markdown(
                        """
                        ## Impressum

                        **CipherCore**
                        Ralf Krümmel
                        Wintergartenstraße 2
                        04103 Leipzig

                        E-Mail: support@ciphercore.de

                        CipherCore bietet umfassende Beratungsleistungen und Schulungen für KMU zum EU AI Act an.
                        """
                    )

    def run(self):
        demo = gr.Blocks(title="Info - Standalone - CipherCore")
        with demo:
            # Wiederholung der allgemeinen Info, gefolgt von den Untertabs
            gr.Markdown(
                """
                # Wichtige Hinweise und Warnungen zur Arbeit mit Künstlicher Intelligenz (KI)
                **Erstellt von CipherCore**

                [Siehe unten die spezifischen Bereiche für weitere Details.]
                """
            )
            with gr.Tabs():
                with gr.TabItem("Allgemein"):
                    gr.Markdown(
                        """
                        ## Allgemeine Hinweise

                        - Überprüfe die KI-Ergebnisse kritisch.
                        - Nutze die Systeme nur im vorgesehenen Rahmen.
                        - Informiere Dich regelmäßig über aktuelle Entwicklungen und Best Practices.
                        """
                    )
                with gr.TabItem("AI Act Europa"):
                    gr.Markdown(
                        """
                        ## Neuer AI Act Europa

                        Der seit Februar in Kraft getretene AI Act legt strenge Vorgaben für Transparenz, Sicherheit und Risikomanagement fest.

                        **Wichtige Punkte:**
                        - Transparenz und Nachvollziehbarkeit der KI-Algorithmen.
                        - Sicherheit und Zuverlässigkeit der Systeme.
                        - Verpflichtendes Risikomanagement.
                        - Einhaltung gesetzlicher Vorgaben und Compliance-Maßnahmen.
                        """
                    )
                with gr.TabItem("Mitarbeiterschulung"):
                    gr.Markdown(
                        """
                        ## Mitarbeiterschulung für KI

                        Um den verantwortungsvollen Umgang mit KI sicherzustellen, ist eine umfassende Schulung der Mitarbeiter notwendig.

                        **Schulungsthemen:**
                        - Grundlagen und Funktionsweisen der Künstlichen Intelligenz.
                        - Rechtliche und ethische Aspekte (inkl. AI Act Europa).
                        - Praktischer Einsatz und Interpretation von KI-Ergebnissen.
                        - Maßnahmen zur Fehlervermeidung und Risikominimierung.
                        """
                    )
        demo.launch()

if __name__ == "__main__":
    info_tab = InfoTab()
    info_tab.run()