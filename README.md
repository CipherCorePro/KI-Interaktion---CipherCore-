# KI Interaktion - CipherCore 🤖🔒

[![Gradio App](https://img.shields.io/badge/Gradio-App-orange)](https://gradio.app)
[![Python](https://img.shields.io/badge/Python-3.9+-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Willkommen zum **KI Interaktion - CipherCore** Projekt! 👋

Dieses Projekt, entwickelt von **CipherCore**, Ihrem Experten für **Sicherheit in der Programmierung**, bietet eine vielseitige Gradio-Anwendung für die Interaktion mit Künstlicher Intelligenz.  Unser Fokus liegt auf der sicheren und verantwortungsvollen Nutzung von KI-Technologien. Diese Anwendung demonstriert verschiedene Möglichkeiten, wie Sie KI in Ihrem Arbeitsalltag oder für private Projekte nutzen können – **immer mit Blick auf Sicherheit und Datenschutz**.

## ✨ Funktionalitäten im Überblick

Die Anwendung ist modular aufgebaut und bietet verschiedene Modi der KI-Interaktion, übersichtlich in Tabs gegliedert:

*   **🎤 Audio-Interaktion:** Transkribieren Sie Audioaufnahmen oder lassen Sie die KI Audioinhalte analysieren. Ideal für Meetings, Podcasts oder Sprachnotizen.
*   **💬 Chat & Bildanalyse:**  Führen Sie Dialoge mit der KI und analysieren Sie Bilder gleichzeitig. Perfekt für kreative Brainstormings oder Bildbeschreibungen.
*   **🎬 Videoanalyse:**  Laden Sie Videos hoch und lassen Sie die KI den Inhalt beschreiben oder analysieren. Nützlich für Content-Analyse oder Video-Zusammenfassungen.
*   **📁 Dateianalyse:**  Analysieren Sie verschiedene Dateiformate (Text, Code, Dokumente, Tabellen) mit der KI.  Steigern Sie Ihre Produktivität im Umgang mit Dokumenten.
*   **📝 Inhaltserstellung & Export:**  Generieren Sie Texte, Berichte oder andere Inhalte mit der KI und exportieren Sie diese in gängige Formate wie Word, Excel, CSV oder PDF.
*   **🎨 Bildgenerierung (DALL·E):**  Erstellen Sie einzigartige Bilder mit DALL·E 3 und transformieren Sie diese.  Entfesseln Sie Ihre Kreativität!
*   **ℹ️ Info:**  Wichtige Hinweise, Warnungen und Informationen zum verantwortungsvollen Umgang mit KI, dem EU AI Act und Mitarbeiterschulungen. Bleiben Sie informiert und sicher!
*   **🎓 Mitarbeiterschulung:**  Umfassende Schulungsmaterialien zu KI-Grundlagen, verantwortungsvollem Einsatz, rechtlichen Rahmenbedingungen und praktischer Anwendung.  Bilden Sie sich und Ihre Mitarbeiter weiter!
*   **✅ Mitarbeitertest EU AI Act:**  Überprüfen Sie Ihr Wissen zum EU AI Act mit einem interaktiven Test.  Seien Sie compliant!
*   **🛡️ PDF Sicherheitsprüfung:**  Scannen Sie PDF-Dateien auf potenziell gefährliche Inhalte, um Ihre Dokumente sicher zu halten.  Sicherheit geht vor!
*   **🤝 Agenten-Konversation:**  Starten Sie Diskussionen zwischen verschiedenen KI-Agenten zu einem bestimmten Thema und beobachten Sie die vielfältigen Perspektiven.

## 🔒 Sicherheitsfokus von CipherCore

CipherCore legt höchsten Wert auf **Sicherheit in der Programmierung**. Diese Anwendung wurde mit Blick auf folgende Sicherheitsaspekte entwickelt:

*   **Eingabevalidierung:**  Prompts werden auf Länge geprüft, um Missbrauch zu verhindern.
*   **Dateigrößenbeschränkungen:**  Upload-Größen sind limitiert, um Denial-of-Service-Angriffe zu vermeiden.
*   **Sichere API-Nutzung:**  Verwendung von Umgebungsvariablen für API-Schlüssel und implementierter Fehlerbehandlung bei API-Aufrufen.
*   **PDF-Sicherheitsprüfung:**  Integrierte Analyse und Bereinigung von PDF-Dateien auf potenziell schädliche Inhalte.
*   **Verantwortungsvolle KI-Nutzung:**  Hinweise und Schulungsmaterialien fördern einen ethischen und sicheren Umgang mit KI.

## ⚙️ Installation

Folgen Sie diesen Schritten, um die Anwendung lokal auszuführen:

1.  **Klonen Sie das Repository:**
    ```bash
    git clone [REPOSITORY-URL]
    cd [REPOSITORY-NAME]
    ```
2.  **Erstellen Sie eine virtuelle Umgebung (empfohlen):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # oder venv\Scripts\activate unter Windows
    ```
3.  **Installieren Sie die benötigten Python-Pakete:**
    ```bash
    pip install -r requirements.txt
    ```
    Stellen Sie sicher, dass Sie `requirements.txt` im Repository finden (falls nicht vorhanden, manuell installieren: `pip install gradio python-dotenv google-generativeai openai requests torch pillow docx pandas fpdf opencv-python PyMuPDF pdfid-script jsonschema`).
4.  **Konfigurieren Sie die API-Schlüssel:**
    *   Erstellen Sie eine `.env`-Datei im Hauptverzeichnis des Projekts.
    *   Fügen Sie Ihre API-Keys in die `.env`-Datei ein. Ersetzen Sie `DEIN_API_KEY`, `DEIN_OPENAI_API_KEY` und `DEIN_MISTRAL_API_KEY` mit Ihren tatsächlichen Schlüsseln:
        ```
        API_KEY=DEIN_GEMINI_API_KEY
        OPENAI_API_KEY=DEIN_OPENAI_API_KEY
        MISTRAL_API_KEY=DEIN_MISTRAL_API_KEY
        ```
        **Hinweis:**  Sichern Sie Ihre `.env`-Datei und teilen Sie Ihre API-Keys nicht öffentlich!
5.  **Starten Sie die Anwendung:**
    ```bash
    python main.py
    ```
    Oder navigieren Sie zum `test`-Ordner und führen Sie `main.py` aus:
    ```bash
    cd test
    python main.py
    ```
6.  **Öffnen Sie die Anwendung im Browser:**
    Die Anwendung wird in Ihrem Standardbrowser unter der angegebenen Adresse (`http://localhost:7860` oder ähnlich) geöffnet.

## 🚀 Nutzung

Nach dem Start der Anwendung können Sie über die Tabs am oberen Rand zwischen den verschiedenen Funktionalitäten wechseln.

*   **Wählen Sie einen Tab** aus, der Ihren Bedürfnissen entspricht (z.B. "Chat & Bildanalyse" für textbasierte und bildbezogene Fragen).
*   **Geben Sie einen Prompt oder eine ANFRAGE** in das entsprechende Textfeld ein.
*   **Laden Sie optionale Dateien hoch**, falls erforderlich (z.B. Audiodateien, Bilder, Videos, Dokumente).
*   **Klicken Sie auf den "Senden"-Button**, um die Anfrage an die KI zu senden.
*   **Die Antwort der KI wird im Ausgabebereich angezeigt.**
*   In einigen Tabs (z.B. "Inhaltserstellung & Export", "PDF Sicherheitsprüfung") können Sie Dateien **herunterladen**.

**Agenten-Konversation Tab:**

*   Wählen Sie im Tab "Agenten-Konversation" die gewünschten **Agenten** und deren **Persönlichkeit** aus.
*   Geben Sie ein **Diskussionsthema** ein.
*   Passen Sie die **Anzahl der Gesprächsrunden** und das **Experten-Level** an.
*   Starten Sie die Konversation mit dem Button "Konversation starten".
*   Bewerten Sie die Antworten der Agenten mit den 👍 und 👎 Buttons.
*   Speichern Sie die Diskussion oder laden Sie den Chatverlauf als Word-Datei herunter.

**PDF Sicherheitsprüfung Tab:**

*   Laden Sie eine PDF-Datei hoch, um sie auf potenziell gefährliche Inhalte zu überprüfen.
*   Die Anwendung analysiert die Datei und gibt ein Ergebnis mit Warnungen oder Hinweisen aus.
*   Bei Bedarf wird eine bereinigte Version der PDF-Datei zum Download bereitgestellt.

**Mitarbeitertest EU AI Act Tab:**

*   Absolvieren Sie den interaktiven Test mit 52 Fragen zum EU AI Act, um Ihr Wissen zu überprüfen.
*   Nach Abschluss des Tests erhalten Sie eine Auswertung und detailliertes Feedback zu falsch beantworteten Fragen.

**Mitarbeiterschulung Tab:**

*   Nutzen Sie die umfassenden Schulungsmaterialien zu verschiedenen KI-Themen, um Ihr Wissen und das Ihrer Mitarbeiter zu erweitern.

## 🤝 Beiträge

Beiträge zu diesem Projekt sind willkommen! Wenn Sie Fehler finden, Verbesserungsvorschläge haben oder neue Funktionen hinzufügen möchten, erstellen Sie bitte einen Issue oder einen Pull Request.

## 📜 Lizenz

Dieses Projekt ist unter der [MIT Lizenz](LICENSE) lizenziert.

## ✉️ Kontakt

**CipherCore**
Ralf Krümmel
Wintergartenstraße 2
04103 Leipzig

E-Mail: [support@ciphercore.de](mailto:support@ciphercore.de)

[Website von CipherCore (https://ciphercore.de)]

---

**Viel Spaß mit der KI Interaktion - CipherCore Anwendung!** 🚀
