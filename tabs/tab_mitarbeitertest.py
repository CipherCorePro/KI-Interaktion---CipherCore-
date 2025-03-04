#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modul: tab_mitarbeitertest_eu_ai_act.py
Beschreibung:
Dieses Modul implementiert einen interaktiven Mitarbeitertest zum EU AI Act mit 52 Fragen.
Für jede Frage wird der Fragetext, vier Antwortoptionen, die korrekte Antwort und eine kurze Erklärung angegeben.
Bei der Auswertung wird bei falscher Beantwortung jeweils das Feedback (Frage, gegebene Antwort, korrekte Antwort und Erklärung) angezeigt.
Das Programm wurde von CipherCore erstellt.
"""

import gradio as gr
from typing import Union

class MitarbeiterTestEUAIAct:
    def __init__(self) -> None:
        # ---------------------------------------------------------
        # 1) KORREKTE ANTWORTEN (exakte Übereinstimmung beachten!)
        # ---------------------------------------------------------
        self.korrekte_antworten: dict[str, str] = {
            "frage1": "Der EU AI Act ist eine Regulierung, die die Nutzung von KI-Systemen in der Europäischen Union regelt, insbesondere in kritischen Bereichen.",
            "frage2": "Der EU AI Act stellt sicher, dass KI-Systeme wie Google Gemini oder ChatGPT sicher und verantwortungsvoll genutzt werden.",
            "frage3": "Kritische Bereiche wie Personalwesen, Kundenmanagement und Entscheidungsfindung sind besonders betroffen.",
            "frage4": "Es gibt verschiedene Risikostufen, je nachdem, wie und wo die KI eingesetzt wird.",
            "frage5": "Mitarbeiter müssen wissen, welche Daten sie eingeben dürfen und wie sie KI-Ergebnisse kritisch bewerten.",
            "frage6": "Unternehmen müssen Nutzer informieren, wenn KI-generierte Inhalte in Entscheidungen einfließen.",
            "frage7": "Mitarbeiter sollten geschult werden, Verzerrungen in KI-Ergebnissen zu erkennen und gegenzusteuern.",
            "frage8": "KI darf keine sensiblen oder personenbezogene Daten ohne klare Rechtsgrundlage verarbeiten.",
            "frage9": "Entscheidungen, die durch KI getroffen oder unterstützt werden, müssen überprüfbar bleiben.",
            "frage10": "Eine Schulung stellt sicher, dass Mitarbeiter die Risiken und Verantwortlichkeiten bei der Nutzung von KI verstehen.",
            "frage11": "Besonders wichtig ist eine Schulung bei automatisierter Kundeninteraktion, Datenverarbeitung und der Erstellung von Texten oder Berichten.",
            "frage12": "Verstöße können zu hohen Strafen führen, bis zu 6 % des weltweiten Umsatzes.",
            "frage13": "Fehlinterpretationen oder falsche Nutzung können zu Reputationsschäden und rechtlichen Risiken führen.",
            "frage14": "Durch Einhaltung der DSGVO und klare Rechtsgrundlagen für die Datenverarbeitung.",
            "frage15": "Um Transparenz zu gewährleisten und das Vertrauen der Kunden zu bewahren.",
            "frage16": "Durch regelmäßige Überprüfung der Daten und Schulung der Mitarbeiter.",
            "frage17": "Diese müssen korrekt, transparent und nicht irreführend sein.",
            "frage18": "Hohe Strafen und mögliche rechtliche Schritte.",
            "frage19": "Durch klare Information der Kunden über den Einsatz von KI.",
            "frage20": "Weil sie personenbezogene Daten betreffen kann und daher strengen Datenschutzanforderungen unterliegt.",
            "frage21": "Die DSGVO stellt sicher, dass personenbezogene Daten geschützt werden.",
            "frage22": "Durch regelmäßige Überprüfung und die Möglichkeit, Entscheidungen zu revidieren.",
            "frage23": "Um Fehler und Verzerrungen zu erkennen und zu korrigieren.",
            "frage24": "Nur Daten, die den Datenschutzanforderungen entsprechen und eine klare Rechtsgrundlage haben.",
            "frage25": "Durch klare Information der Nutzer und Dokumentation der Prozesse.",
            "frage26": "Bias sind Verzerrungen, die zu ungerechten oder diskriminierenden Ergebnissen führen können.",
            "frage27": "Durch regelmäßige Überprüfung der Ergebnisse und Schulung der Mitarbeiter.",
            "frage28": "Um faire und gerechte Entscheidungen zu gewährleisten.",
            "frage29": "Klare Rechtsgrundlagen für die Datenverarbeitung und Einhaltung der DSGVO.",
            "frage30": "Durch regelmäßige Wartung, Schulung der Mitarbeiter und Überprüfung der Ergebnisse.",
            "frage31": "Durch klare Information der Mitarbeiter und Dokumentation der Prozesse.",
            "frage32": "Weil sie personenbezogene Daten betreffen kann und daher strengen Datenschutzanforderungen unterliegt.",
            "frage33": "Sie stellt sicher, dass Entscheidungen überprüfbar bleiben und Fehler korrigiert werden können.",
            "frage34": "Durch klare Information der Mitarbeiter und Dokumentation der Prozesse.",
            "frage35": "Um die Risiken und Verantwortlichkeiten bei der Nutzung von KI zu verstehen.",
            "frage36": "Hohe Strafen und mögliche rechtliche Schritte.",
            "frage37": "Durch klare Information der Kunden und Dokumentation der Prozesse.",
            "frage38": "Weil sie personenbezogene Daten betreffen kann und daher strengen Datenschutzanforderungen unterliegt.",
            "frage39": "Sie stellt sicher, dass Entscheidungen überprüfbar bleiben und Fehler korrigiert werden können.",
            "frage40": "Durch klare Information der Kunden und Dokumentation der Prozesse.",
            "frage41": "Um die Risiken und Verantwortlichkeiten bei der Nutzung von KI zu verstehen.",
            "frage42": "Hohe Strafen und mögliche rechtliche Schritte.",
            "frage43": "Durch klare Information der Beteiligten und Dokumentation der Prozesse.",
            "frage44": "Weil sie wichtige Entscheidungen beeinflussen kann und daher strengen Anforderungen unterliegt.",
            "frage45": "Sie stellt sicher, dass Entscheidungen überprüfbar bleiben und Fehler korrigiert werden können.",
            "frage46": "Durch klare Information der Beteiligten und Dokumentation der Prozesse.",
            "frage47": "Um die Risiken und Verantwortlichkeiten bei der Nutzung von KI zu verstehen.",
            "frage48": "Hohe Strafen und mögliche rechtliche Schritte.",
            "frage49": "Der Hauptzweck ist es, die Nutzung von KI-Systemen zu regulieren, um sicherzustellen, dass sie sicher und verantwortungsvoll eingesetzt werden.",
            "frage50": "Verschiedene Arten, je nach Anwendung und Risikostufe, einschließlich KI-gestützter Assistenten wie Google Gemini oder ChatGPT.",
            "frage51": "Transparenz hilft, das Vertrauen der Nutzer zu gewinnen und sicherzustellen, dass sie informierte Entscheidungen treffen können.",
            "frage52": "Durch Schulung der Mitarbeiter, Einhaltung der Datenschutzbestimmungen und regelmäßige Überprüfung der KI-Systeme."
        }

        # ---------------------------------------------------------
        # 2) FRAGEN: TEXT, OPTIONEN, ERKLÄRUNG
        # ---------------------------------------------------------
        self.fragen: dict[str, dict[str, Union[str, list[str]]]] = {
            "frage1": {
                "text": "Was ist der EU AI Act?",
                "optionen": [
                    "Ein Gesetz, das die Nutzung von KI-Systemen in der EU reguliert, insbesondere in kritischen Bereichen.",
                    "Ein Förderprogramm für KI-Startups.",
                    "Ein Sicherheitsprotokoll für KI-Systeme.",
                    "Eine internationale Vereinbarung zur KI-Entwicklung."
                ],
                "erklärung": "Der EU AI Act legt verbindliche Regeln für den Einsatz von KI in der EU fest, um Risiken zu minimieren."
            },
            "frage2": {
                "text": "Warum ist der EU AI Act für KI-gestützte Assistenten relevant?",
                "optionen": [
                    "Weil sie ausschließlich für Unterhaltung genutzt werden.",
                    "Weil er sicherstellt, dass Systeme wie Google Gemini oder ChatGPT sicher und verantwortungsvoll genutzt werden.",
                    "Weil sie nur in der Forschung eingesetzt werden dürfen.",
                    "Weil sie keine Auswirkungen auf Nutzer haben."
                ],
                "erklärung": "Der EU AI Act reguliert den Einsatz von KI, um beispielsweise kritische Bereiche wie den Kundenservice abzusichern."
            },
            "frage3": {
                "text": "Welche Bereiche sind besonders betroffen?",
                "optionen": [
                    "Nur der Finanzsektor.",
                    "Kritische Bereiche wie Personalwesen, Kundenmanagement und Entscheidungsfindung.",
                    "Ausschließlich der Unterhaltungsbereich.",
                    "Nur der öffentliche Sektor."
                ],
                "erklärung": "Insbesondere Bereiche, in denen KI direkt Entscheidungen beeinflusst, stehen im Fokus des EU AI Acts."
            },
            "frage4": {
                "text": "Welche Risikostufen gibt es im EU AI Act?",
                "optionen": [
                    "Nur ein Risikoniveau.",
                    "Verschiedene Risikostufen, je nach Einsatzgebiet der KI.",
                    "Zwei Risikostufen: sicher und unsicher.",
                    "Keine Risikostufen, nur Empfehlungen."
                ],
                "erklärung": "Die Einstufung in unterschiedliche Risikostufen ermöglicht es, gezielte Auflagen zu formulieren."
            },
            "frage5": {
                "text": "Was bedeutet verantwortungsbewusste Nutzung von KI?",
                "optionen": [
                    "Dass Mitarbeiter eigenständig KI-Systeme programmieren.",
                    "Dass Mitarbeiter wissen, welche Daten sie eingeben dürfen und KI-Ergebnisse kritisch bewerten.",
                    "Dass KI-Systeme automatisch arbeiten ohne menschliche Intervention.",
                    "Dass nur die IT-Abteilung für KI zuständig ist."
                ],
                "erklärung": "Verantwortungsbewusste Nutzung bedeutet, Risiken zu erkennen und sachgerecht zu handeln."
            },
            "frage6": {
                "text": "Was sind Transparenzpflichten im Zusammenhang mit KI?",
                "optionen": [
                    "Dass Unternehmen interne Prozesse geheim halten.",
                    "Dass Unternehmen Nutzer informieren, wenn KI-generierte Inhalte in Entscheidungen einfließen.",
                    "Dass nur Behörden über KI informiert werden müssen.",
                    "Dass KI-Systeme keine Dokumentation benötigen."
                ],
                "erklärung": "Transparenz sorgt dafür, dass Nutzer immer wissen, wann KI im Spiel ist."
            },
            "frage7": {
                "text": "Wie kann Bias in KI-Ergebnissen vermieden werden?",
                "optionen": [
                    "Durch Schulung der Mitarbeiter und regelmäßige Überprüfung der Ergebnisse.",
                    "Indem man die KI vollständig unkontrolliert arbeiten lässt.",
                    "Durch den Verzicht auf KI-Systeme.",
                    "Bias kann nicht vermieden werden."
                ],
                "erklärung": "Schulungen und regelmäßige Audits helfen, Verzerrungen frühzeitig zu erkennen und zu beheben."
            },
            "frage8": {
                "text": "Welche Rolle spielt der Datenschutz bei der Nutzung von KI?",
                "optionen": [
                    "KI darf alle Daten ohne Einschränkung verarbeiten.",
                    "KI darf keine sensiblen oder personenbezogene Daten ohne klare Rechtsgrundlage verarbeiten.",
                    "Datenschutz ist nur für Banken wichtig.",
                    "Datenschutz gilt nur für manuelle Prozesse."
                ],
                "erklärung": "Der Schutz personenbezogener Daten ist zentral, um die Privatsphäre der Nutzer zu gewährleisten."
            },
            "frage9": {
                "text": "Was bedeutet menschliche Aufsicht bei KI-Entscheidungen?",
                "optionen": [
                    "Dass KI-Systeme autonom arbeiten und nicht kontrolliert werden müssen.",
                    "Dass Entscheidungen, die durch KI getroffen oder unterstützt werden, von Menschen überprüft werden müssen.",
                    "Dass nur Manager Entscheidungen treffen dürfen.",
                    "Dass KI nur in Testumgebungen eingesetzt wird."
                ],
                "erklärung": "Menschliche Aufsicht ist wichtig, um bei Fehlern oder unerwarteten Ergebnissen eingreifen zu können."
            },
            "frage10": {
                "text": "Warum ist eine Schulung der Mitarbeiter wichtig?",
                "optionen": [
                    "Weil sie dadurch KI-Systeme selbst entwickeln können.",
                    "Weil sie so die Risiken und Verantwortlichkeiten im Umgang mit KI verstehen.",
                    "Weil Schulungen gesetzlich nicht vorgeschrieben sind.",
                    "Weil sie nur für Führungskräfte notwendig sind."
                ],
                "erklärung": "Schulungen befähigen die Mitarbeiter, KI-Systeme sicher und effizient zu nutzen."
            },
            "frage11": {
                "text": "Wann ist eine Schulung besonders wichtig?",
                "optionen": [
                    "Nur bei technischen Problemen.",
                    "Bei automatisierter Kundeninteraktion, Datenverarbeitung und Erstellung von Berichten.",
                    "Schulungen sind immer optional.",
                    "Nur vor dem ersten Einsatz von KI."
                ],
                "erklärung": "Insbesondere bei direktem Kundenkontakt und datenintensiven Prozessen ist fundiertes Wissen essenziell."
            },
            "frage12": {
                "text": "Was passiert bei Nichteinhaltung des EU AI Act?",
                "optionen": [
                    "Es gibt lediglich eine mündliche Verwarnung.",
                    "Verstöße können zu hohen Strafen, bis zu 6 % des weltweiten Umsatzes, führen.",
                    "Nichts, da der Act nur Empfehlungen enthält.",
                    "Nur interne Maßnahmen werden ergriffen."
                ],
                "erklärung": "Die Nichteinhaltung kann erhebliche finanzielle und rechtliche Konsequenzen nach sich ziehen."
            },
            "frage13": {
                "text": "Welche rechtlichen Risiken gibt es bei falscher Nutzung von KI?",
                "optionen": [
                    "Es gibt keine rechtlichen Risiken.",
                    "Fehlinterpretationen oder falsche Nutzung können zu Reputationsschäden und rechtlichen Risiken führen.",
                    "Nur technische Probleme entstehen.",
                    "Rechtliche Risiken betreffen nur Entwickler."
                ],
                "erklärung": "Falsche Nutzung kann zu erheblichen Schadenersatzforderungen und Reputationsverlust führen."
            },
            "frage14": {
                "text": "Wie können Datenschutzverstöße bei der Nutzung von KI vermieden werden?",
                "optionen": [
                    "Indem man keine Daten verarbeitet.",
                    "Durch Einhaltung der DSGVO und klare Rechtsgrundlagen für die Datenverarbeitung.",
                    "Durch ausschließliche Nutzung von Cloud-Diensten.",
                    "Datenschutzverstöße sind unvermeidbar."
                ],
                "erklärung": "Klare Regelungen und die Einhaltung der DSGVO minimieren das Risiko von Datenschutzverletzungen."
            },
            "frage15": {
                "text": "Warum müssen Kunden wissen, dass sie mit einer KI interagieren?",
                "optionen": [
                    "Weil KI-Systeme immer fehlerfrei sind.",
                    "Um Transparenz zu gewährleisten und das Vertrauen der Kunden zu bewahren.",
                    "Kunden brauchen keine Information darüber.",
                    "Nur im internen Gebrauch ist Transparenz wichtig."
                ],
                "erklärung": "Die Information stärkt das Vertrauen und ermöglicht informierte Entscheidungen."
            },
            "frage16": {
                "text": "Wie kann die Zuverlässigkeit von KI-generierten Daten sichergestellt werden?",
                "optionen": [
                    "Durch regelmäßige Überprüfung der Daten und Schulung der Mitarbeiter.",
                    "Indem man sich ausschließlich auf KI verlässt.",
                    "Zuverlässigkeit ist nicht relevant.",
                    "Nur durch externe Audits."
                ],
                "erklärung": "Regelmäßige Kontrollen und Schulungen helfen, fehlerhafte Daten frühzeitig zu identifizieren."
            },
            "frage17": {
                "text": "Was muss bei der Erstellung von KI-generierten Inhalten beachtet werden?",
                "optionen": [
                    "Die Inhalte müssen korrekt, transparent und nicht irreführend sein.",
                    "Es spielt keine Rolle, solange es schnell geht.",
                    "Inhalte können beliebig sein.",
                    "Nur der kreative Aspekt ist wichtig."
                ],
                "erklärung": "Nur durch klare und korrekte Inhalte kann das Vertrauen der Nutzer gesichert werden."
            },
            "frage18": {
                "text": "Welche Konsequenzen haben Verstöße gegen den EU AI Act?",
                "optionen": [
                    "Es gibt lediglich eine interne Mahnung.",
                    "Hohe Strafen und mögliche rechtliche Schritte.",
                    "Nur eine Verbesserung der Prozesse.",
                    "Verstöße haben keine Auswirkungen."
                ],
                "erklärung": "Die Nichteinhaltung kann schwerwiegende finanzielle und rechtliche Folgen haben."
            },
            "frage19": {
                "text": "Wie kann die Nutzung von KI im Kundenservice transparent gestaltet werden?",
                "optionen": [
                    "Durch geheime interne Prozesse.",
                    "Durch klare Information der Kunden über den Einsatz von KI.",
                    "Transparenz ist im Kundenservice nicht wichtig.",
                    "Nur durch externe Berichte."
                ],
                "erklärung": "Kunden müssen wissen, wann und wie KI in den Service einfließt, um Vertrauen aufzubauen."
            },
            "frage20": {
                "text": "Warum ist die Datenverarbeitung durch KI besonders sensibel?",
                "optionen": [
                    "Weil sie ausschließlich technische Daten verarbeitet.",
                    "Weil sie personenbezogene Daten betreffen kann und strengen Datenschutzanforderungen unterliegt.",
                    "Datenverarbeitung ist immer unkritisch.",
                    "Nur bei großen Datenmengen ist Vorsicht geboten."
                ],
                "erklärung": "Sensibel ist die Datenverarbeitung, wenn personenbezogene Daten ohne Rechtsgrundlage verarbeitet werden."
            },
            "frage21": {
                "text": "Welche Rolle spielt die DSGVO bei der Nutzung von KI?",
                "optionen": [
                    "Die DSGVO hat keinen Einfluss auf KI.",
                    "Die DSGVO stellt sicher, dass personenbezogene Daten geschützt werden.",
                    "Die DSGVO regelt nur den internationalen Handel.",
                    "Die DSGVO ist nur für physische Daten relevant."
                ],
                "erklärung": "Die DSGVO schützt die Privatsphäre der Nutzer, indem sie den Umgang mit personenbezogenen Daten regelt."
            },
            "frage22": {
                "text": "Wie kann die menschliche Aufsicht bei KI-Entscheidungen gewährleistet werden?",
                "optionen": [
                    "Indem man KI-Systeme unbeaufsichtigt laufen lässt.",
                    "Durch regelmäßige Überprüfung und die Möglichkeit, Entscheidungen zu revidieren.",
                    "Menschliche Aufsicht ist nicht erforderlich.",
                    "Nur durch externe Berater."
                ],
                "erklärung": "Nur so kann sichergestellt werden, dass bei Fehlern rechtzeitig eingegriffen wird."
            },
            "frage23": {
                "text": "Warum ist es wichtig, KI-Ergebnisse kritisch zu bewerten?",
                "optionen": [
                    "Weil KI immer korrekte Ergebnisse liefert.",
                    "Um Fehler und Verzerrungen zu erkennen und zu korrigieren.",
                    "Kritische Bewertung ist nur in der Theorie wichtig.",
                    "Nur Manager müssen Ergebnisse bewerten."
                ],
                "erklärung": "Eine kritische Bewertung verhindert, dass fehlerhafte oder verzerrte Ergebnisse unkontrolliert weiterverwendet werden."
            },
            "frage24": {
                "text": "Welche Daten dürfen in KI-Systeme eingegeben werden?",
                "optionen": [
                    "Beliebige Daten ohne Einschränkung.",
                    "Nur Daten, die den Datenschutzanforderungen entsprechen und eine klare Rechtsgrundlage haben.",
                    "Nur öffentliche Daten.",
                    "Alle Daten, solange sie digital vorliegen."
                ],
                "erklärung": "Dies schützt vor unrechtmäßiger Verarbeitung sensibler Informationen."
            },
            "frage25": {
                "text": "Wie kann die Transparenz bei der Nutzung von KI sichergestellt werden?",
                "optionen": [
                    "Durch geheime interne Abläufe.",
                    "Durch klare Information der Nutzer und Dokumentation der Prozesse.",
                    "Transparenz ist unwichtig, wenn die Technologie funktioniert.",
                    "Nur durch externe Zertifikate."
                ],
                "erklärung": "Dokumentation und Information schaffen Vertrauen und ermöglichen Überprüfbarkeit."
            },
            "frage26": {
                "text": "Was bedeutet Bias in KI-Ergebnissen?",
                "optionen": [
                    "Bias sind zufällige Fehler, die nicht vermieden werden können.",
                    "Bias sind Verzerrungen, die zu ungerechten oder diskriminierenden Ergebnissen führen können.",
                    "Bias bezieht sich auf technische Ausfälle.",
                    "Bias bedeutet, dass die KI immer richtige Ergebnisse liefert."
                ],
                "erklärung": "Bias kann dazu führen, dass bestimmte Gruppen benachteiligt werden – dies gilt es zu vermeiden."
            },
            "frage27": {
                "text": "Wie kann Bias in KI-Systemen erkannt werden?",
                "optionen": [
                    "Durch regelmäßige Überprüfung der Ergebnisse und Schulung der Mitarbeiter.",
                    "Bias kann nicht erkannt werden.",
                    "Nur durch externe Prüfungen.",
                    "Indem man die KI ausschließlich in isolierten Umgebungen einsetzt."
                ],
                "erklärung": "Regelmäßige Audits und Schulungen helfen, systematische Verzerrungen frühzeitig zu identifizieren."
            },
            "frage28": {
                "text": "Warum ist die Vermeidung von Bias in KI wichtig?",
                "optionen": [
                    "Um faire und gerechte Entscheidungen zu gewährleisten.",
                    "Bias ist nur ein theoretisches Problem.",
                    "Bias führt zu schnelleren Ergebnissen.",
                    "Bias ist in der Praxis unvermeidlich."
                ],
                "erklärung": "Nur durch den Abbau von Verzerrungen können KI-Systeme objektiv und gerecht agieren."
            },
            "frage29": {
                "text": "Welche rechtlichen Grundlagen sind für die Nutzung von KI notwendig?",
                "optionen": [
                    "Es sind keine rechtlichen Grundlagen nötig.",
                    "Klare Rechtsgrundlagen für die Datenverarbeitung und die Einhaltung der DSGVO.",
                    "Nur interne Richtlinien sind ausreichend.",
                    "Rechtliche Grundlagen gelten nur für öffentliche Einrichtungen."
                ],
                "erklärung": "Eine solide Rechtsgrundlage schützt vor unrechtmäßiger Datenverarbeitung und Haftungsrisiken."
            },
            "frage30": {
                "text": "Wie kann die Zuverlässigkeit von KI-Systemen sichergestellt werden?",
                "optionen": [
                    "Durch regelmäßige Wartung, Schulung der Mitarbeiter und Überprüfung der Ergebnisse.",
                    "Zuverlässigkeit ist ein Zufallsprodukt.",
                    "Nur durch den Einsatz von High-End-Hardware.",
                    "Durch einmalige Tests vor dem Einsatz."
                ],
                "erklärung": "Kontinuierliche Überwachung und regelmäßige Updates sind entscheidend für den stabilen Betrieb."
            },
            "frage31": {
                "text": "Wie kann die Nutzung von KI im Personalwesen transparent gestaltet werden?",
                "optionen": [
                    "Durch geheime interne Prozesse.",
                    "Durch klare Information der Mitarbeiter und Dokumentation der Prozesse.",
                    "Transparenz ist im Personalwesen nicht wichtig.",
                    "Nur durch externe Audits."
                ],
                "erklärung": "Transparenz im Personalwesen hilft, Missbrauch zu vermeiden und das Vertrauen der Mitarbeiter zu sichern."
            },
            "frage32": {
                "text": "Warum ist die Nutzung von KI im Personalwesen sensibel?",
                "optionen": [
                    "Weil sie lediglich technische Aufgaben übernimmt.",
                    "Weil sie personenbezogene Daten betreffen kann und strengen Datenschutzanforderungen unterliegt.",
                    "Personalwesen ist unkritisch.",
                    "Weil sie immer fehlerhafte Ergebnisse liefert."
                ],
                "erklärung": "Im Personalwesen sind sensible Daten betroffen – daher sind strenge Datenschutzmaßnahmen notwendig."
            },
            "frage33": {
                "text": "Welche Rolle spielt die menschliche Aufsicht bei der Nutzung von KI im Personalwesen?",
                "optionen": [
                    "Sie ist nicht erforderlich.",
                    "Sie stellt sicher, dass Entscheidungen überprüfbar bleiben und Fehler korrigiert werden können.",
                    "Sie erfolgt nur sporadisch.",
                    "Sie wird ausschließlich von externen Beratern übernommen."
                ],
                "erklärung": "Menschliche Kontrolle ist essenziell, um ungewollte Folgen im Personalbereich zu vermeiden."
            },
            "frage34": {
                "text": "Wie kann die Transparenz bei der Nutzung von KI im Personalwesen sichergestellt werden?",
                "optionen": [
                    "Durch klare Information der Mitarbeiter und umfassende Dokumentation der Prozesse.",
                    "Transparenz ist hier nicht wichtig.",
                    "Nur durch gelegentliche Berichte.",
                    "Indem man alle Prozesse geheim hält."
                ],
                "erklärung": "Nur so kann nachvollzogen werden, wie KI im Personalwesen eingesetzt wird."
            },
            "frage35": {
                "text": "Warum ist die Schulung der Mitarbeiter im Personalwesen wichtig?",
                "optionen": [
                    "Weil sie dadurch neue Technologien erfinden.",
                    "Um die Risiken und Verantwortlichkeiten im Umgang mit KI zu verstehen.",
                    "Schulungen sind hier überflüssig.",
                    "Nur Führungskräfte benötigen Schulungen."
                ],
                "erklärung": "Gut geschulte Mitarbeiter können besser mit sensiblen Daten und KI-gestützten Prozessen umgehen."
            },
            "frage36": {
                "text": "Welche Konsequenzen haben Verstöße gegen den EU AI Act im Personalwesen?",
                "optionen": [
                    "Es gibt lediglich interne Maßnahmen.",
                    "Hohe Strafen und mögliche rechtliche Schritte.",
                    "Nur eine schriftliche Verwarnung.",
                    "Keine Konsequenzen, wenn es um Personal geht."
                ],
                "erklärung": "Verstöße im sensiblen Bereich Personalwesen können gravierende rechtliche Folgen haben."
            },
            "frage37": {
                "text": "Wie kann die Nutzung von KI im Kundenmanagement transparent gestaltet werden?",
                "optionen": [
                    "Durch klare Information der Kunden und lückenlose Dokumentation der Prozesse.",
                    "Kunden müssen nicht informiert werden.",
                    "Transparenz erfolgt nur intern.",
                    "Nur durch externe Berichte."
                ],
                "erklärung": "Transparenz im Kundenmanagement stärkt das Vertrauen und ermöglicht es, eventuelle Fehler schnell zu erkennen."
            },
            "frage38": {
                "text": "Warum ist die Nutzung von KI im Kundenmanagement sensibel?",
                "optionen": [
                    "Weil sie ausschließlich technische Daten verarbeitet.",
                    "Weil sie personenbezogene Daten betreffen kann und strengen Datenschutzanforderungen unterliegt.",
                    "Kundenmanagement ist unkritisch.",
                    "Weil es keine regulatorischen Vorgaben gibt."
                ],
                "erklärung": "Personenbezogene Kundendaten erfordern besondere Sorgfalt und Schutzmaßnahmen."
            },
            "frage39": {
                "text": "Welche Rolle spielt die menschliche Aufsicht bei der Nutzung von KI im Kundenmanagement?",
                "optionen": [
                    "Sie ist nicht notwendig.",
                    "Sie stellt sicher, dass Entscheidungen überprüfbar bleiben und Fehler korrigiert werden können.",
                    "Sie wird nur im Notfall aktiviert.",
                    "Sie erfolgt ausschließlich durch externe Auditoren."
                ],
                "erklärung": "Menschliche Kontrolle ist auch im Kundenmanagement essenziell, um Fehlentscheidungen zu vermeiden."
            },
            "frage40": {
                "text": "Wie kann die Transparenz bei der Nutzung von KI im Kundenmanagement sichergestellt werden?",
                "optionen": [
                    "Durch klare Information der Kunden und lückenlose Dokumentation der Prozesse.",
                    "Transparenz ist hier unwichtig.",
                    "Nur durch interne Richtlinien.",
                    "Indem man die Prozesse geheim hält."
                ],
                "erklärung": "Klare Kommunikation und Dokumentation fördern das Vertrauen der Kunden."
            },
            "frage41": {
                "text": "Warum ist die Schulung der Mitarbeiter im Kundenmanagement wichtig?",
                "optionen": [
                    "Weil sie so KI-Systeme entwickeln können.",
                    "Um die Risiken und Verantwortlichkeiten bei der Nutzung von KI zu verstehen.",
                    "Schulungen sind nur für Führungskräfte nötig.",
                    "Kundenmanagement erfordert keine speziellen Kenntnisse."
                ],
                "erklärung": "Gut informierte Mitarbeiter können Fehler vermeiden und den korrekten Umgang mit KI gewährleisten."
            },
            "frage42": {
                "text": "Welche Konsequenzen haben Verstöße gegen den EU AI Act im Kundenmanagement?",
                "optionen": [
                    "Es gibt nur interne Konsequenzen.",
                    "Hohe Strafen und mögliche rechtliche Schritte.",
                    "Nur eine mündliche Verwarnung.",
                    "Verstöße haben keine Auswirkungen im Kundenmanagement."
                ],
                "erklärung": "Verstöße im Kundenmanagement können zu erheblichen Reputations- und finanziellen Schäden führen."
            },
            "frage43": {
                "text": "Wie kann die Nutzung von KI in der Entscheidungsfindung transparent gestaltet werden?",
                "optionen": [
                    "Durch klare Information der Beteiligten und umfassende Dokumentation der Prozesse.",
                    "Entscheidungen sollten ausschließlich intern getroffen werden.",
                    "Transparenz ist bei strategischen Entscheidungen nicht erforderlich.",
                    "Nur durch externe Zertifikate."
                ],
                "erklärung": "Transparenz in der Entscheidungsfindung ist wichtig, um nachvollziehbare Prozesse zu garantieren."
            },
            "frage44": {
                "text": "Warum ist die Nutzung von KI in der Entscheidungsfindung sensibel?",
                "optionen": [
                    "Weil sie wichtige Entscheidungen beeinflussen kann und daher strengen Anforderungen unterliegt.",
                    "Entscheidungen durch KI sind immer korrekt.",
                    "Die Nutzung von KI hat keinen Einfluss auf Entscheidungen.",
                    "Nur technische Aspekte sind hier relevant."
                ],
                "erklärung": "Fehler in der Entscheidungsfindung können gravierende Folgen für das Unternehmen haben."
            },
            "frage45": {
                "text": "Welche Rolle spielt die menschliche Aufsicht bei der Nutzung von KI in der Entscheidungsfindung?",
                "optionen": [
                    "Sie stellt sicher, dass Entscheidungen überprüfbar bleiben und bei Bedarf revidiert werden können.",
                    "Menschliche Aufsicht ist in der Entscheidungsfindung nicht notwendig.",
                    "Nur externe Berater kontrollieren die Entscheidungen.",
                    "Die KI übernimmt die komplette Verantwortung."
                ],
                "erklärung": "Menschliche Kontrolle ermöglicht es, Fehler frühzeitig zu erkennen und gegenzusteuern."
            },
            "frage46": {
                "text": "Wie kann die Transparenz bei der Nutzung von KI in der Entscheidungsfindung sichergestellt werden?",
                "optionen": [
                    "Durch klare Information der Beteiligten und lückenlose Dokumentation der Prozesse.",
                    "Transparenz ist in der Entscheidungsfindung irrelevant.",
                    "Nur interne Notizen genügen.",
                    "Indem man die Entscheidungsprozesse geheim hält."
                ],
                "erklärung": "Dokumentation und offene Kommunikation sorgen dafür, dass die Entscheidungswege nachvollziehbar sind."
            },
            "frage47": {
                "text": "Warum ist die Schulung der Mitarbeiter in der Entscheidungsfindung wichtig?",
                "optionen": [
                    "Um die Risiken und Verantwortlichkeiten bei der Nutzung von KI zu verstehen.",
                    "Schulungen sind in diesem Bereich überflüssig.",
                    "Nur Führungskräfte sollten geschult werden.",
                    "Die Entscheidungsfindung erfordert keine speziellen Kenntnisse."
                ],
                "erklärung": "Nur gut geschulte Mitarbeiter können fundierte Entscheidungen treffen und Fehler vermeiden."
            },
            "frage48": {
                "text": "Welche Konsequenzen haben Verstöße gegen den EU AI Act in der Entscheidungsfindung?",
                "optionen": [
                    "Hohe Strafen und mögliche rechtliche Schritte.",
                    "Nur interne Verwarnungen.",
                    "Es gibt keine Konsequenzen in diesem Bereich.",
                    "Verstöße werden nur mild geahndet."
                ],
                "erklärung": "Fehlverhalten in der Entscheidungsfindung kann zu erheblichen rechtlichen und finanziellen Konsequenzen führen."
            },
            "frage49": {
                "text": "Was ist der Hauptzweck des EU AI Act?",
                "optionen": [
                    "Der EU AI Act fördert ausschließlich den internationalen Handel.",
                    "Der Hauptzweck ist es, die Nutzung von KI-Systemen zu regulieren, um sicherzustellen, dass sie sicher und verantwortungsvoll eingesetzt werden.",
                    "Er ermöglicht eine uneingeschränkte Nutzung von KI in allen Bereichen.",
                    "Er dient nur der technischen Standardisierung."
                ],
                "erklärung": "Der Act soll Risiken minimieren und Grundrechte schützen, indem er klare Regeln für den KI-Einsatz aufstellt."
            },
            "frage50": {
                "text": "Welche Arten von KI-Systemen fallen unter den EU AI Act?",
                "optionen": [
                    "Nur KI-Systeme im öffentlichen Sektor.",
                    "Verschiedene Arten, je nach Anwendung und Risikostufe, einschließlich KI-gestützter Assistenten wie Google Gemini oder ChatGPT.",
                    "Ausschließlich KI-Systeme, die in der Forschung verwendet werden.",
                    "Nur KI-Systeme, die keine sensiblen Daten verarbeiten."
                ],
                "erklärung": "Der Act betrifft alle KI-Anwendungen, die potenziell Risiken für Grundrechte oder Sicherheit darstellen."
            },
            "frage51": {
                "text": "Warum ist die Transparenz bei der Nutzung von KI wichtig?",
                "optionen": [
                    "Weil Transparenz hilft, das Vertrauen der Nutzer zu gewinnen und informierte Entscheidungen zu treffen.",
                    "Weil Transparenz nur eine theoretische Anforderung ist.",
                    "Weil sie ausschließlich für externe Audits relevant ist.",
                    "Transparenz ist in der Praxis nicht umsetzbar."
                ],
                "erklärung": "Offene Kommunikation und klare Prozesse fördern das Vertrauen in die eingesetzten KI-Systeme."
            },
            "frage52": {
                "text": "Wie können Unternehmen sicherstellen, dass sie den EU AI Act einhalten?",
                "optionen": [
                    "Durch gelegentliche interne Meetings.",
                    "Durch Schulung der Mitarbeiter, Einhaltung der Datenschutzbestimmungen und regelmäßige Überprüfung der KI-Systeme.",
                    "Indem sie den Act ignorieren und auf Selbstregulierung setzen.",
                    "Durch ausschließliche externe Beratung ohne interne Maßnahmen."
                ],
                "erklärung": "Kontinuierliche Schulungen und regelmäßige Überprüfungen sind essenziell, um gesetzliche Vorgaben einzuhalten."
            }
        }

    def evaluate_answers(
        self,
        a1: str, a2: str, a3: str, a4: str, a5: str,
        a6: str, a7: str, a8: str, a9: str, a10: str,
        a11: str, a12: str, a13: str, a14: str, a15: str,
        a16: str, a17: str, a18: str, a19: str, a20: str,
        a21: str, a22: str, a23: str, a24: str, a25: str,
        a26: str, a27: str, a28: str, a29: str, a30: str,
        a31: str, a32: str, a33: str, a34: str, a35: str,
        a36: str, a37: str, a38: str, a39: str, a40: str,
        a41: str, a42: str, a43: str, a44: str, a45: str,
        a46: str, a47: str, a48: str, a49: str, a50: str,
        a51: str, a52: str
    ) -> str:
        """
        Diese Methode wertet die Antworten aus und liefert ein Ergebnis sowie detailliertes Feedback.
        Für jede falsch beantwortete Frage wird der Fragetext, die vom Nutzer gegebene Antwort,
        die korrekte Antwort und eine kurze Erklärung angezeigt.
        """
        antworten: dict[str, str] = {
            "frage1": a1,   "frage2": a2,   "frage3": a3,   "frage4": a4,   "frage5": a5,
            "frage6": a6,   "frage7": a7,   "frage8": a8,   "frage9": a9,   "frage10": a10,
            "frage11": a11, "frage12": a12, "frage13": a13, "frage14": a14, "frage15": a15,
            "frage16": a16, "frage17": a17, "frage18": a18, "frage19": a19, "frage20": a20,
            "frage21": a21, "frage22": a22, "frage23": a23, "frage24": a24, "frage25": a25,
            "frage26": a26, "frage27": a27, "frage28": a28, "frage29": a29, "frage30": a30,
            "frage31": a31, "frage32": a32, "frage33": a33, "frage34": a34, "frage35": a35,
            "frage36": a36, "frage37": a37, "frage38": a38, "frage39": a39, "frage40": a40,
            "frage41": a41, "frage42": a42, "frage43": a43, "frage44": a44, "frage45": a45,
            "frage46": a46, "frage47": a47, "frage48": a48, "frage49": a49, "frage50": a50,
            "frage51": a51, "frage52": a52
        }

        score = 0
        feedback = ""

        for frage_id, user_antwort in antworten.items():
            korrekte_antwort = self.korrekte_antworten[frage_id]
            if user_antwort == korrekte_antwort:
                score += 1
            else:
                feedback += (
                    f"Frage: {self.fragen[frage_id]['text']}\n"
                    f"Deine Antwort: {user_antwort}\n"
                    f"Richtige Antwort: {korrekte_antwort}\n"
                    f"Erklärung: {self.fragen[frage_id]['erklärung']}\n\n"
                )

        result = f"Du hast {score} von 52 Fragen richtig beantwortet.\n"
        if score == 52:
            result += "Ausgezeichnet! Dein Wissen entspricht den höchsten Anforderungen des EU AI Acts."
        elif score >= 40:
            result += "Sehr gut gemacht, aber es gibt noch Raum für Verbesserungen."
        elif score >= 25:
            result += "Solides Ergebnis, aber bitte vertiefe dein Wissen in den genannten Bereichen."
        else:
            result += "Bitte wiederhole die Schulungsinhalte und konsultiere weiterführende Materialien."

        if feedback:
            result += "\n\nFeedback zu den falsch beantworteten Fragen:\n" + feedback
        return result

    def build_tab(self) -> None:
        with gr.TabItem("Mitarbeitertest EU AI Act"):
            gr.Markdown(
                f"""
                # Mitarbeitertest EU AI Act

                **Erstellt von: CipherCore - Sicherheit in der Programmierung**

                Bitte beantworte die folgenden 52 Fragen, um dein Wissen über den EU AI Act zu überprüfen.
                """
            )
            # Aufbau der Radio-Buttons für alle 52 Fragen
            frage1  = gr.Radio(self.fragen["frage1"]["optionen"],  label=self.fragen["frage1"]["text"])
            frage2  = gr.Radio(self.fragen["frage2"]["optionen"],  label=self.fragen["frage2"]["text"])
            frage3  = gr.Radio(self.fragen["frage3"]["optionen"],  label=self.fragen["frage3"]["text"])
            frage4  = gr.Radio(self.fragen["frage4"]["optionen"],  label=self.fragen["frage4"]["text"])
            frage5  = gr.Radio(self.fragen["frage5"]["optionen"],  label=self.fragen["frage5"]["text"])
            frage6  = gr.Radio(self.fragen["frage6"]["optionen"],  label=self.fragen["frage6"]["text"])
            frage7  = gr.Radio(self.fragen["frage7"]["optionen"],  label=self.fragen["frage7"]["text"])
            frage8  = gr.Radio(self.fragen["frage8"]["optionen"],  label=self.fragen["frage8"]["text"])
            frage9  = gr.Radio(self.fragen["frage9"]["optionen"],  label=self.fragen["frage9"]["text"])
            frage10 = gr.Radio(self.fragen["frage10"]["optionen"], label=self.fragen["frage10"]["text"])
            frage11 = gr.Radio(self.fragen["frage11"]["optionen"], label=self.fragen["frage11"]["text"])
            frage12 = gr.Radio(self.fragen["frage12"]["optionen"], label=self.fragen["frage12"]["text"])
            frage13 = gr.Radio(self.fragen["frage13"]["optionen"], label=self.fragen["frage13"]["text"])
            frage14 = gr.Radio(self.fragen["frage14"]["optionen"], label=self.fragen["frage14"]["text"])
            frage15 = gr.Radio(self.fragen["frage15"]["optionen"], label=self.fragen["frage15"]["text"])
            frage16 = gr.Radio(self.fragen["frage16"]["optionen"], label=self.fragen["frage16"]["text"])
            frage17 = gr.Radio(self.fragen["frage17"]["optionen"], label=self.fragen["frage17"]["text"])
            frage18 = gr.Radio(self.fragen["frage18"]["optionen"], label=self.fragen["frage18"]["text"])
            frage19 = gr.Radio(self.fragen["frage19"]["optionen"], label=self.fragen["frage19"]["text"])
            frage20 = gr.Radio(self.fragen["frage20"]["optionen"], label=self.fragen["frage20"]["text"])
            frage21 = gr.Radio(self.fragen["frage21"]["optionen"], label=self.fragen["frage21"]["text"])
            frage22 = gr.Radio(self.fragen["frage22"]["optionen"], label=self.fragen["frage22"]["text"])
            frage23 = gr.Radio(self.fragen["frage23"]["optionen"], label=self.fragen["frage23"]["text"])
            frage24 = gr.Radio(self.fragen["frage24"]["optionen"], label=self.fragen["frage24"]["text"])
            frage25 = gr.Radio(self.fragen["frage25"]["optionen"], label=self.fragen["frage25"]["text"])
            frage26 = gr.Radio(self.fragen["frage26"]["optionen"], label=self.fragen["frage26"]["text"])
            frage27 = gr.Radio(self.fragen["frage27"]["optionen"], label=self.fragen["frage27"]["text"])
            frage28 = gr.Radio(self.fragen["frage28"]["optionen"], label=self.fragen["frage28"]["text"])
            frage29 = gr.Radio(self.fragen["frage29"]["optionen"], label=self.fragen["frage29"]["text"])
            frage30 = gr.Radio(self.fragen["frage30"]["optionen"], label=self.fragen["frage30"]["text"])
            frage31 = gr.Radio(self.fragen["frage31"]["optionen"], label=self.fragen["frage31"]["text"])
            frage32 = gr.Radio(self.fragen["frage32"]["optionen"], label=self.fragen["frage32"]["text"])
            frage33 = gr.Radio(self.fragen["frage33"]["optionen"], label=self.fragen["frage33"]["text"])
            frage34 = gr.Radio(self.fragen["frage34"]["optionen"], label=self.fragen["frage34"]["text"])
            frage35 = gr.Radio(self.fragen["frage35"]["optionen"], label=self.fragen["frage35"]["text"])
            frage36 = gr.Radio(self.fragen["frage36"]["optionen"], label=self.fragen["frage36"]["text"])
            frage37 = gr.Radio(self.fragen["frage37"]["optionen"], label=self.fragen["frage37"]["text"])
            frage38 = gr.Radio(self.fragen["frage38"]["optionen"], label=self.fragen["frage38"]["text"])
            frage39 = gr.Radio(self.fragen["frage39"]["optionen"], label=self.fragen["frage39"]["text"])
            frage40 = gr.Radio(self.fragen["frage40"]["optionen"], label=self.fragen["frage40"]["text"])
            frage41 = gr.Radio(self.fragen["frage41"]["optionen"], label=self.fragen["frage41"]["text"])
            frage42 = gr.Radio(self.fragen["frage42"]["optionen"], label=self.fragen["frage42"]["text"])
            frage43 = gr.Radio(self.fragen["frage43"]["optionen"], label=self.fragen["frage43"]["text"])
            frage44 = gr.Radio(self.fragen["frage44"]["optionen"], label=self.fragen["frage44"]["text"])
            frage45 = gr.Radio(self.fragen["frage45"]["optionen"], label=self.fragen["frage45"]["text"])
            frage46 = gr.Radio(self.fragen["frage46"]["optionen"], label=self.fragen["frage46"]["text"])
            frage47 = gr.Radio(self.fragen["frage47"]["optionen"], label=self.fragen["frage47"]["text"])
            frage48 = gr.Radio(self.fragen["frage48"]["optionen"], label=self.fragen["frage48"]["text"])
            frage49 = gr.Radio(self.fragen["frage49"]["optionen"], label=self.fragen["frage49"]["text"])
            frage50 = gr.Radio(self.fragen["frage50"]["optionen"], label=self.fragen["frage50"]["text"])
            frage51 = gr.Radio(self.fragen["frage51"]["optionen"], label=self.fragen["frage51"]["text"])
            frage52 = gr.Radio(self.fragen["frage52"]["optionen"], label=self.fragen["frage52"]["text"])

            result_box = gr.Textbox(label="Testergebnis", interactive=False)
            submit_btn = gr.Button("Test auswerten")
            submit_btn.click(
                self.evaluate_answers,
                inputs=[
                    frage1, frage2, frage3, frage4, frage5,
                    frage6, frage7, frage8, frage9, frage10,
                    frage11, frage12, frage13, frage14, frage15,
                    frage16, frage17, frage18, frage19, frage20,
                    frage21, frage22, frage23, frage24, frage25,
                    frage26, frage27, frage28, frage29, frage30,
                    frage31, frage32, frage33, frage34, frage35,
                    frage36, frage37, frage38, frage39, frage40,
                    frage41, frage42, frage43, frage44, frage45,
                    frage46, frage47, frage48, frage49, frage50,
                    frage51, frage52
                ],
                outputs=result_box
            )

if __name__ == "__main__":
    with gr.Blocks(title="Mitarbeitertest EU AI Act - CipherCore") as demo:
        MitarbeiterTestEUAIAct().build_tab()
    demo.launch()


class MitarbeiterTest:
    def __init__(self) -> None:
        """
        1) self.korrekte_antworten: Dictionary mit den richtigen Antworten (Frage-ID -> String).
        2) self.fragen: Dictionary mit Fragen, Antwortoptionen und Erklärungen (Frage-ID -> {text, optionen, erklärung}).
        """
        # ---------------------------------------------------------
        # 1) KORREKTE ANTWORTEN - BITTE GENAU AUF STRING-GLEICHHEIT ACHTEN!
        # ---------------------------------------------------------
        self.korrekte_antworten: dict[str, str] = {
            # --- 1 bis 12: Bekannte Fragen ---
            "frage1": "Unannehmbares Risiko",
            "frage2": "Transparenz, Nachvollziehbarkeit, menschliche Aufsicht",
            "frage3": "Geldbußen, Marktrücknahme, zivilrechtliche Haftung",
            "frage4": "Unannehmbares Risiko, hohes Risiko, begrenztes Risiko, minimales Risiko",
            "frage5": "DSGVO, Datenschutz-Folgenabschätzung",
            "frage6": "Detaillierte technische Dokumentation und kontinuierliche Überwachung",
            "frage7": "Hohe Datenqualität und regelmäßige Überprüfungen",
            "frage8": "Menschliche Aufsicht und Eingriffsmöglichkeiten",
            "frage9": "Transparenzpflichten und Benachrichtigung der Nutzer",
            "frage10": "Regelmäßige Audits und externe Überprüfungen",
            "frage11": "Einhaltung der Vorgaben und kontinuierliche Verbesserung",
            "frage12": "Transparenzpflichten, Datenschutz-Folgenabschätzung, menschliche Aufsicht",

            # --- 13 bis 50: Neue Fragen ---
            "frage13": "Alle KI-Systeme, die als unannehmbares Risiko eingestuft sind",
            "frage14": "Regelmäßige Prüfungen und Protokollierung",
            "frage15": "Hochrisiko-KI-Systeme erfordern eine Konformitätsbewertung",
            "frage16": "Verboten, es sei denn, enge Ausnahmen greifen",
            "frage17": "Menschenzentrierung und Schutz der Grundrechte",
            "frage18": "Der EU AI Act gilt auch für Anbieter außerhalb der EU, sofern sie KI-Systeme in der EU bereitstellen",
            "frage19": "Ethische Leitlinien und Selbstverpflichtungen sind empfehlenswert, aber keine formale Pflicht",
            "frage20": "Das Risiko für Gesundheit, Sicherheit oder Grundrechte",
            "frage21": "Unabhängige Stellen prüfen Hochrisiko-KI-Systeme vor dem Inverkehrbringen",
            "frage22": "Ein umfassendes Risikomanagement-System muss implementiert sein",
            "frage23": "Das System muss transparent sein und klar auf KI-Einsatz hinweisen",
            "frage24": "Bei biometrischer Fernidentifizierung gelten besonders strenge Regeln",
            "frage25": "Daten müssen repräsentativ, fehlerfrei und vollständig sein",
            "frage26": "Ja, KI-Systeme mit Echtzeit-Biometrie-Erkennung gelten als besonders kritisch",
            "frage27": "4% des weltweiten Jahresumsatzes oder bis zu 30 Mio. Euro, je nachdem, was höher ist",
            "frage28": "Ein Verfahren, um KI-Systeme im laufenden Betrieb zu überwachen und zu verbessern",
            "frage29": "Bei Verletzung von Grundrechten kann auch zivilrechtliche Haftung entstehen",
            "frage30": "Eine schriftliche und nachvollziehbare Dokumentation des KI-Systems",
            "frage31": "Regelmäßige Updates der Trainingsdaten und Modelle",
            "frage32": "Ja, für Hochrisiko-KI-Systeme ist ein Konformitätsbewertungsverfahren erforderlich",
            "frage33": "Das EU AI Act-Portal zur Meldung von Vorfällen",
            "frage34": "Angemessene technische und organisatorische Maßnahmen (TOMs) sind vorgeschrieben",
            "frage35": "Strafverfolgung und militärische Anwendungen können teils ausgenommen sein",
            "frage36": "Stets den Menschen im Mittelpunkt behalten",
            "frage37": "Unannehmbare Risiken sind unter allen Umständen verboten",
            "frage38": "Bestimmung von Verantwortlichkeiten in allen Phasen des KI-Lebenszyklus",
            "frage39": "Bei Hochrisiko-KI-Systemen muss menschliche Aufsicht stets möglich sein",
            "frage40": "Nein, es gibt Ausnahmen für Forschung und Tests unter kontrollierten Bedingungen",
            "frage41": "Auflistung der KI-Komponenten, Datenquellen und Algorithmen",
            "frage42": "Möglichst erklärbare Modelle oder XAI-Verfahren anwenden",
            "frage43": "Der EU AI Act ergänzt bestehende Rechtsvorschriften (z.B. Produktsicherheit)",
            "frage44": "KI-Systeme dürfen nicht zum sozialen Scoring eingesetzt werden, wenn Grundrechte verletzt werden",
            "frage45": "Ein hohes Maß an Cybersicherheit und Robustheit ist vorgeschrieben",
            "frage46": "Nicht diskriminierend, fair und inklusiv sein",
            "frage47": "Alle Dokumentations- und Berichtspflichten müssen erfüllt werden",
            "frage48": "Ständige Überwachung auf mögliche Bias und Fehler",
            "frage49": "Alle KI-Systeme müssen nach dem risikobasierten Ansatz klassifiziert werden",
            "frage50": "Ja, Verstöße können behördlich sanktioniert und geahndet werden"
        }

        # ---------------------------------------------------------
        # 2) FRAGEN: TEXT, OPTIONEN, ERKLÄRUNG
        # ---------------------------------------------------------
        self.fragen: dict[str, dict[str, Union[str, list[str]]]] = {
            # Vorhandene Fragen 1-12 (leicht gekürzt für Übersicht)
            "frage1": {
                "text": "Welche Risikokategorie beschreibt KI-Systeme, die als eine klare Bedrohung für Grundrechte gelten und daher verboten sind?",
                "optionen": [
                    "Hochrisiko-KI-Systeme",
                    "Unannehmbares Risiko",
                    "Begrenztes Risiko",
                    "Minimales Risiko"
                ],
                "erklärung": (
                    "Diese Kategorie umfasst KI-Systeme, die inakzeptable Risiken für die Grundrechte darstellen. "
                    "Mehr Infos: https://digital-strategy.ec.europa.eu/en/policies/eu-regulation-artificial-intelligence"
                )
            },
            "frage2": {
                "text": "Welche Anforderungen gelten für Hochrisiko-KI-Systeme? (Wähle die beste Antwort)",
                "optionen": [
                    "Transparenz, Nachvollziehbarkeit, menschliche Aufsicht",
                    "Geringe Genauigkeit",
                    "Keine Dokumentation",
                    "Vollautomatischer Betrieb ohne Kontrolle"
                ],
                "erklärung": (
                    "Hochrisiko-Systeme müssen strenge Anforderungen erfüllen, um Sicherheit, Fairness und "
                    "Nachvollziehbarkeit zu gewährleisten."
                )
            },
            "frage3": {
                "text": "Welche rechtlichen Konsequenzen können bei Verstößen gegen den EU AI Act drohen?",
                "optionen": [
                    "Nichts",
                    "Geldbußen, Marktrücknahme, zivilrechtliche Haftung",
                    "Nur Verwarnungen",
                    "Nur interne Sanktionen"
                ],
                "erklärung": (
                    "Verstöße können erhebliche finanzielle und rechtliche Folgen nach sich ziehen."
                )
            },
            "frage4": {
                "text": "Wie werden KI-Systeme gemäß dem EU AI Act risikokategorisiert?",
                "optionen": [
                    "Nach Funktionsweise",
                    "Unannehmbares Risiko, hohes Risiko, begrenztes Risiko, minimales Risiko",
                    "Nach Popularität",
                    "Nach technischer Komplexität"
                ],
                "erklärung": (
                    "Die Kategorisierung erfolgt anhand des Risikopotenzials für Grundrechte und die Sicherheit der Nutzer."
                )
            },
            "frage5": {
                "text": "Welche Datenschutzregelungen sind bei der Entwicklung von KI-Systemen besonders relevant?",
                "optionen": [
                    "DSGVO, Datenschutz-Folgenabschätzung",
                    "Haftungsregelungen",
                    "Arbeitsrecht",
                    "Patentrecht"
                ],
                "erklärung": (
                    "Die DSGVO sowie eine Datenschutz-Folgenabschätzung sind zentrale Bausteine für den Schutz personenbezogener Daten."
                )
            },
            "frage6": {
                "text": "Welche ergänzenden Maßnahmen sind erforderlich, um '100%ige' Konformität im Betrieb von Hochrisiko-KI-Systemen zu erreichen?",
                "optionen": [
                    "Standardmäßige Implementierung ohne weitere Maßnahmen",
                    "Detaillierte technische Dokumentation und kontinuierliche Überwachung",
                    "Nur manuelle Prüfungen",
                    "Ausschließlich externe Audits"
                ],
                "erklärung": (
                    "Neben der Einhaltung gesetzlicher Vorgaben sind Dokumentation, Überwachung und regelmäßige Audits wichtig."
                )
            },
            "frage7": {
                "text": "Welche Anforderungen gelten für die Datenqualität in Hochrisiko-KI-Systemen?",
                "optionen": [
                    "Hohe Datenqualität und regelmäßige Überprüfungen",
                    "Keine speziellen Anforderungen",
                    "Nur interne Überprüfungen",
                    "Datenqualität ist irrelevant"
                ],
                "erklärung": (
                    "Hochrisiko-KI-Systeme müssen hohe Standards an Datenqualität erfüllen und regelmäßig überprüft werden."
                )
            },
            "frage8": {
                "text": "Welche Rolle spielt die menschliche Aufsicht in Hochrisiko-KI-Systemen?",
                "optionen": [
                    "Menschliche Aufsicht und Eingriffsmöglichkeiten",
                    "Keine menschliche Aufsicht erforderlich",
                    "Nur bei Systemfehlern",
                    "Nur bei Nutzerbeschwerden"
                ],
                "erklärung": (
                    "Menschliche Aufsicht ist entscheidend, um sicherzustellen, dass KI-Systeme sicher und ethisch betrieben werden."
                )
            },
            "frage9": {
                "text": "Welche Transparenzpflichten gelten für bestimmte KI-Anwendungen?",
                "optionen": [
                    "Transparenzpflichten und Benachrichtigung der Nutzer",
                    "Keine Transparenzpflichten",
                    "Nur interne Transparenz",
                    "Nur bei behördlichen Anfragen"
                ],
                "erklärung": (
                    "Bestimmte KI-Anwendungen müssen transparent sein und Nutzer über ihre Funktionsweise informieren."
                )
            },
            "frage10": {
                "text": "Welche Maßnahmen sind notwendig, um die Konformität von Hochrisiko-KI-Systemen langfristig sicherzustellen?",
                "optionen": [
                    "Regelmäßige Audits und externe Überprüfungen",
                    "Keine zusätzlichen Maßnahmen",
                    "Nur interne Überprüfungen",
                    "Nur bei Beschwerden"
                ],
                "erklärung": (
                    "Regelmäßige Audits und externe Überprüfungen sind notwendig, um die Konformität zu gewährleisten."
                )
            },
            "frage11": {
                "text": "Wie sollte ein Unternehmen mit den Vorgaben des EU AI Acts umgehen?",
                "optionen": [
                    "Einhaltung der Vorgaben und kontinuierliche Verbesserung",
                    "Ignorieren der Vorgaben",
                    "Einmalige Anpassung ohne weitere Überprüfungen",
                    "Nur bei behördlichen Anfragen reagieren"
                ],
                "erklärung": (
                    "Unternehmen sollten die Vorgaben einhalten und kontinuierlich verbessern, um langfristige Konformität zu gewährleisten."
                )
            },
            "frage12": {
                "text": "Fallstudie: Ein KI-System zur Gesichtserkennung wird in einem öffentlichen Raum eingesetzt. Welche Maßnahmen sind erforderlich, um die Konformität sicherzustellen?",
                "optionen": [
                    "Transparenzpflichten, Datenschutz-Folgenabschätzung, menschliche Aufsicht",
                    "Keine speziellen Maßnahmen",
                    "Nur technische Dokumentation",
                    "Nur interne Überprüfungen"
                ],
                "erklärung": (
                    "Bei Gesichtserkennung im öffentlichen Raum sind Transparenz, DSFA und menschliche Aufsicht erforderlich."
                )
            },

            # ----------------------------------------------------------------------
            # Neue Fragen 13-50 (Themen: Prohibited Practices, Konformitätsverfahren,
            # Risikobewertung, Dokumentation, Strafmaßnahmen etc.)
            # ----------------------------------------------------------------------

            "frage13": {
                "text": "Welche KI-Systeme sind laut EU AI Act strikt verboten?",
                "optionen": [
                    "Alle KI-Systeme, die als unannehmbares Risiko eingestuft sind",
                    "Nur Systeme mit geringer Genauigkeit",
                    "Alle KI-Systeme in der EU",
                    "Keine, es gibt nur Auflagen"
                ],
                "erklärung": (
                    "Systeme, die als unannehmbares Risiko gelten, sind laut AI Act untersagt. "
                    "Dazu gehören z.B. manipulative KI oder soziale Scoring-Systeme."
                )
            },
            "frage14": {
                "text": "Welche regelmäßigen Maßnahmen sind bei Hochrisiko-KI-Systemen vorgeschrieben, um Sicherheit zu gewährleisten?",
                "optionen": [
                    "Keine besonderen Maßnahmen",
                    "Regelmäßige Prüfungen und Protokollierung",
                    "Nur einmalige Tests vor Markteinführung",
                    "Ausschließlich manuelle Überprüfung bei Fehlern"
                ],
                "erklärung": (
                    "Hochrisiko-KI-Systeme erfordern regelmäßige Überprüfungen, Protokollierung und Monitoring, "
                    "um sicherzustellen, dass sie weiterhin konform bleiben."
                )
            },
            "frage15": {
                "text": "Was schreibt der EU AI Act für Hochrisiko-KI-Systeme im Hinblick auf Konformität vor?",
                "optionen": [
                    "Sie sind generell verboten",
                    "Hochrisiko-KI-Systeme erfordern eine Konformitätsbewertung",
                    "Es gibt keine besonderen Anforderungen",
                    "Die Konformität spielt keine Rolle"
                ],
                "erklärung": (
                    "Vor dem Inverkehrbringen müssen Hochrisiko-KI-Systeme einer Konformitätsbewertung unterzogen werden, "
                    "um sicherzustellen, dass alle Auflagen erfüllt sind."
                )
            },
            "frage16": {
                "text": "Wie wird die biometrische Fernidentifizierung in Echtzeit im öffentlichen Raum im EU AI Act behandelt?",
                "optionen": [
                    "Generell erlaubt, ohne Auflagen",
                    "Verboten, es sei denn, enge Ausnahmen greifen",
                    "Nur bei Strafverfolgung ohne Einschränkungen",
                    "Gar nicht geregelt"
                ],
                "erklärung": (
                    "Biometrische Fernidentifizierung in Echtzeit ist grundsätzlich untersagt, "
                    "mit wenigen eng gefassten Ausnahmen (z.B. Terrorabwehr)."
                )
            },
            "frage17": {
                "text": "Welches übergeordnete Ziel verfolgt der EU AI Act im Umgang mit KI-Systemen?",
                "optionen": [
                    "Maximale Automatisierung aller Prozesse",
                    "Menschenzentrierung und Schutz der Grundrechte",
                    "Verbot von KI jeglicher Art",
                    "Nur wirtschaftliche Interessen im Fokus"
                ],
                "erklärung": (
                    "Der EU AI Act will KI fördern, aber stets die Menschenwürde und Grundrechte schützen."
                )
            },
            "frage18": {
                "text": "Gilt der EU AI Act auch für Anbieter außerhalb der EU?",
                "optionen": [
                    "Nein, nur für Unternehmen mit Sitz in der EU",
                    "Der EU AI Act gilt auch für Anbieter außerhalb der EU, sofern sie KI-Systeme in der EU bereitstellen",
                    "Ja, aber nur für US-Unternehmen",
                    "Nur, wenn der Anbieter explizit zustimmt"
                ],
                "erklärung": (
                    "Der Anwendungsbereich umfasst auch Anbieter aus Drittstaaten, wenn sie KI-Systeme in der EU in Verkehr bringen."
                )
            },
            "frage19": {
                "text": "Sind im EU AI Act verbindliche ethische Leitlinien vorgeschrieben?",
                "optionen": [
                    "Ethische Leitlinien und Selbstverpflichtungen sind empfehlenswert, aber keine formale Pflicht",
                    "Ja, es gibt eine umfassende, bindende Ethikrichtlinie",
                    "Nein, Ethik spielt keine Rolle",
                    "Ethik wird nur in Erwägungsgründen erwähnt, aber nicht gefordert"
                ],
                "erklärung": (
                    "Der EU AI Act schreibt gewisse Grundprinzipien fest, jedoch keine separate, bindende Ethikrichtlinie. "
                    "Ethische Leitlinien sind sinnvoll, aber nicht explizit vorgeschrieben."
                )
            },
            "frage20": {
                "text": "Welches Kriterium ist besonders wichtig bei der Einstufung von KI-Systemen als Hochrisiko?",
                "optionen": [
                    "Der Preis des KI-Systems",
                    "Das Risiko für Gesundheit, Sicherheit oder Grundrechte",
                    "Die Anzahl der Codezeilen",
                    "Die verwendete Programmiersprache"
                ],
                "erklärung": (
                    "Bei Hochrisiko-KI-Systemen steht im Fokus, ob Gesundheit, Sicherheit oder Grundrechte in signifikanter Weise betroffen sind."
                )
            },
            "frage21": {
                "text": "Wer prüft Hochrisiko-KI-Systeme vor dem Inverkehrbringen?",
                "optionen": [
                    "Unabhängige Stellen prüfen Hochrisiko-KI-Systeme vor dem Inverkehrbringen",
                    "Niemand, die Hersteller prüfen sich selbst",
                    "Eine EU-weite KI-Polizei",
                    "Nur die Entwickler selbst, wenn sie Zeit haben"
                ],
                "erklärung": (
                    "Hochrisiko-KI-Systeme müssen einer externen oder internen (je nach Fall) Konformitätsbewertung unterzogen werden."
                )
            },
            "frage22": {
                "text": "Was muss ein Anbieter von Hochrisiko-KI-Systemen laut EU AI Act einrichten?",
                "optionen": [
                    "Ein umfassendes Risikomanagement-System muss implementiert sein",
                    "Nur eine grobe Dokumentation",
                    "Gar nichts, die Verantwortung liegt bei den Nutzern",
                    "Einen internen Ethikrat ohne konkrete Befugnisse"
                ],
                "erklärung": (
                    "Der Anbieter ist verpflichtet, ein Risikomanagement-System zu betreiben, um potenzielle Gefahren zu identifizieren und zu minimieren."
                )
            },
            "frage23": {
                "text": "Was bedeutet Transparenz für Nutzer bei Hochrisiko-KI-Systemen?",
                "optionen": [
                    "Das System muss transparent sein und klar auf KI-Einsatz hinweisen",
                    "Keine Auskunft über KI-Einsatz",
                    "Nur kryptische Hinweise im Kleingedruckten",
                    "Transparenz ist freiwillig"
                ],
                "erklärung": (
                    "Der AI Act fordert klare Informationen für Nutzer, damit sie wissen, dass sie mit einem KI-System interagieren."
                )
            },
            "frage24": {
                "text": "Welche Besonderheit gilt bei biometrischer Fernidentifizierung (z.B. Gesichtserkennung) laut EU AI Act?",
                "optionen": [
                    "Bei biometrischer Fernidentifizierung gelten besonders strenge Regeln",
                    "Sie ist völlig frei erlaubt",
                    "Nur bei privaten Veranstaltungen verboten",
                    "Keine spezifische Regelung"
                ],
                "erklärung": (
                    "Biometrische Fernidentifizierung im öffentlichen Raum wird sehr streng reguliert und teils verboten."
                )
            },
            "frage25": {
                "text": "Wie müssen Trainingsdaten für Hochrisiko-KI-Systeme beschaffen sein?",
                "optionen": [
                    "Daten müssen repräsentativ, fehlerfrei und vollständig sein",
                    "Daten dürfen beliebig verzerrt sein",
                    "Nur zufällig ausgewählte Datensätze",
                    "Es gibt keine Vorgaben zur Datenqualität"
                ],
                "erklärung": (
                    "Der AI Act verlangt, dass Daten korrekt, repräsentativ und angemessen sind, um Verzerrungen zu vermeiden."
                )
            },
            "frage26": {
                "text": "Gehören KI-Systeme zur Echtzeit-Biometrie-Erkennung zu den Hochrisiko-Anwendungen?",
                "optionen": [
                    "Ja, KI-Systeme mit Echtzeit-Biometrie-Erkennung gelten als besonders kritisch",
                    "Nein, niemals",
                    "Nur, wenn sie im Ausland eingesetzt werden",
                    "Die Einordnung obliegt dem Hersteller"
                ],
                "erklärung": (
                    "Echtzeit-Biometrie-Erkennung ist in der Regel hochrisikobehaftet und fällt unter strenge Vorgaben."
                )
            },
            "frage27": {
                "text": "Wie hoch können die Geldbußen laut EU AI Act ausfallen?",
                "optionen": [
                    "Maximal 10.000 Euro",
                    "4% des weltweiten Jahresumsatzes oder bis zu 30 Mio. Euro, je nachdem, was höher ist",
                    "Es gibt keine Geldbußen, nur Verwarnungen",
                    "Nur bei schweren Verstößen bis 1 Mio. Euro"
                ],
                "erklärung": (
                    "Die Höchstgrenze liegt bei 30 Mio. Euro oder 6% (in neueren Fassungen meist 6%), je nach finaler Ausgestaltung. "
                    "Hier wurde 4% und 30 Mio. oft diskutiert, kann je nach finalem Gesetzestext variieren."
                )
            },
            "frage28": {
                "text": "Was versteht man unter 'Post-Market Monitoring' im EU AI Act?",
                "optionen": [
                    "Ein Verfahren, um KI-Systeme im laufenden Betrieb zu überwachen und zu verbessern",
                    "Nur eine abschließende Prüfung vor dem Verkauf",
                    "Ausschließlich ein Marketing-Tool",
                    "Überwachung der Verkaufszahlen, aber nicht der Sicherheit"
                ],
                "erklärung": (
                    "'Post-Market Monitoring' meint, dass Anbieter Hochrisiko-KI-Systeme auch nach dem Inverkehrbringen "
                    "beobachten und gegebenenfalls anpassen."
                )
            },
            "frage29": {
                "text": "Was kann zusätzlich zu Geldbußen auf Unternehmen zukommen, wenn Grundrechte verletzt werden?",
                "optionen": [
                    "Bei Verletzung von Grundrechten kann auch zivilrechtliche Haftung entstehen",
                    "Keine weiteren Folgen",
                    "Nur eine formlose Entschuldigung",
                    "Ausschließlich eine behördliche Verwarnung"
                ],
                "erklärung": (
                    "Neben behördlichen Strafen können geschädigte Personen zivilrechtliche Ansprüche (Schadensersatz) geltend machen."
                )
            },
            "frage30": {
                "text": "Was versteht man im EU AI Act unter 'technischer Dokumentation'?",
                "optionen": [
                    "Eine schriftliche und nachvollziehbare Dokumentation des KI-Systems",
                    "Nur ein kurzes Werbeblatt",
                    "Eine interne Notiz ohne Details",
                    "Keinerlei schriftliche Nachweise"
                ],
                "erklärung": (
                    "Der Anbieter muss das KI-System umfassend beschreiben: Funktionsweise, Datenquellen, Risikoanalyse usw."
                )
            },
            "frage31": {
                "text": "Welche Maßnahmen werden bei Hochrisiko-KI-Systemen im laufenden Betrieb empfohlen?",
                "optionen": [
                    "Regelmäßige Updates der Trainingsdaten und Modelle",
                    "Einmalige Installation ohne Wartung",
                    "Ausschließlich menschliche Kontrolle ohne technische Anpassung",
                    "Keine Maßnahmen nötig, wenn die Zertifizierung vorliegt"
                ],
                "erklärung": (
                    "Um Bias und Fehler zu reduzieren, sollte man Modelle und Datenquellen aktuell halten und laufend optimieren."
                )
            },
            "frage32": {
                "text": "Muss jedes Hochrisiko-KI-System ein Konformitätsbewertungsverfahren durchlaufen?",
                "optionen": [
                    "Ja, für Hochrisiko-KI-Systeme ist ein Konformitätsbewertungsverfahren erforderlich",
                    "Nein, nur wenn der Anbieter es wünscht",
                    "Nur bei Open-Source-Lösungen",
                    "Keine Vorgabe im EU AI Act"
                ],
                "erklärung": (
                    "Der AI Act schreibt eine Konformitätsbewertung vor, bevor ein Hochrisiko-KI-System auf den Markt kommt."
                )
            },
            "frage33": {
                "text": "Wohin können schwerwiegende Vorfälle oder Verstöße gemeldet werden?",
                "optionen": [
                    "Das EU AI Act-Portal zur Meldung von Vorfällen",
                    "Es gibt kein Meldesystem",
                    "Nur an den Hersteller selbst",
                    "Ausschließlich an nationale Gerichte"
                ],
                "erklärung": (
                    "Ein Meldesystem für schwere Vorfälle ist Teil des AI Acts, um rasch auf Probleme reagieren zu können."
                )
            },
            "frage34": {
                "text": "Welche Sicherheitsmaßnahmen sind für Hochrisiko-KI-Systeme vorgeschrieben?",
                "optionen": [
                    "Angemessene technische und organisatorische Maßnahmen (TOMs) sind vorgeschrieben",
                    "Keine Sicherheitsanforderungen",
                    "Nur Passwörter für Administratoren",
                    "Die Endnutzer tragen allein die Verantwortung"
                ],
                "erklärung": (
                    "Der Anbieter muss geeignete TOMs umsetzen, um Sicherheit und Datenschutz zu gewährleisten."
                )
            },
            "frage35": {
                "text": "Gibt es Ausnahmen für bestimmte Bereiche (z.B. Strafverfolgung) im EU AI Act?",
                "optionen": [
                    "Strafverfolgung und militärische Anwendungen können teils ausgenommen sein",
                    "Nein, alle Bereiche sind gleich geregelt",
                    "Nur zivile Bereiche sind ausgenommen",
                    "Alle Strafverfolgungsbehörden sind komplett ausgenommen"
                ],
                "erklärung": (
                    "Einige Sonderregelungen existieren, insbesondere bei Sicherheits- oder Strafverfolgungsbehörden."
                )
            },
            "frage36": {
                "text": "Welche Grundhaltung empfiehlt der AI Act im Umgang mit KI?",
                "optionen": [
                    "Stets den Menschen im Mittelpunkt behalten",
                    "Automatisierung um jeden Preis",
                    "Hauptsache Profitmaximierung",
                    "KI-Systeme sollen den Menschen ersetzen"
                ],
                "erklärung": (
                    "Der Mensch steht im Zentrum. KI soll dienen, nicht dominieren."
                )
            },
            "frage37": {
                "text": "Was gilt für unannehmbare Risiken?",
                "optionen": [
                    "Unannehmbare Risiken sind unter allen Umständen verboten",
                    "Sie sind erlaubt, wenn sie profitabel sind",
                    "Sie sind nicht im AI Act definiert",
                    "Eine Genehmigung kann erkauft werden"
                ],
                "erklärung": (
                    "Systeme, die als unannehmbares Risiko eingestuft werden, sind strikt untersagt."
                )
            },
            "frage38": {
                "text": "Warum ist die klare Zuweisung von Verantwortlichkeiten so wichtig?",
                "optionen": [
                    "Bestimmung von Verantwortlichkeiten in allen Phasen des KI-Lebenszyklus",
                    "Nicht notwendig, da KI-Systeme selbstverantwortlich sind",
                    "Die Verantwortung liegt immer nur beim Endnutzer",
                    "Es gibt keine Regelung zur Verantwortlichkeit"
                ],
                "erklärung": (
                    "Der AI Act schreibt vor, dass Rollen und Pflichten (Anbieter, Nutzer usw.) eindeutig geregelt sein müssen."
                )
            },
            "frage39": {
                "text": "Warum ist die menschliche Aufsicht bei Hochrisiko-KI-Systemen so zentral?",
                "optionen": [
                    "Bei Hochrisiko-KI-Systemen muss menschliche Aufsicht stets möglich sein",
                    "Weil Menschen Fehler machen und KI nicht",
                    "Weil KI-Systeme keinen Schaden anrichten können",
                    "Es ist nur eine Empfehlung"
                ],
                "erklärung": (
                    "Menschen müssen in der Lage sein, einzugreifen und Entscheidungen zu übersteuern, "
                    "falls das KI-System unerwünschte Ergebnisse liefert."
                )
            },
            "frage40": {
                "text": "Sind Forschungstätigkeiten vom EU AI Act erfasst?",
                "optionen": [
                    "Nein, es gibt Ausnahmen für Forschung und Tests unter kontrollierten Bedingungen",
                    "Ja, in vollem Umfang",
                    "Forschung ist generell verboten",
                    "Es gibt keine Bestimmungen dazu"
                ],
                "erklärung": (
                    "Forschung und Entwicklung können von bestimmten Pflichten ausgenommen sein, solange keine Markteinführung erfolgt."
                )
            },
            "frage41": {
                "text": "Welche Inhalte sollte die technische Dokumentation mindestens umfassen?",
                "optionen": [
                    "Auflistung der KI-Komponenten, Datenquellen und Algorithmen",
                    "Nur den Firmennamen",
                    "Beliebige Kurzbeschreibung ohne Details",
                    "Ausschließlich ein Zertifikat"
                ],
                "erklärung": (
                    "Die Dokumentation muss die Funktionsweise, Datenbasis und Risiken des Systems nachvollziehbar darlegen."
                )
            },
            "frage42": {
                "text": "Wie kann man die Nachvollziehbarkeit komplexer KI-Modelle verbessern?",
                "optionen": [
                    "Möglichst erklärbare Modelle oder XAI-Verfahren anwenden",
                    "Komplette Black-Box-Modelle verwenden",
                    "Nutzer erhalten keine Einblicke",
                    "Nachvollziehbarkeit ist unwichtig"
                ],
                "erklärung": (
                    "Explainable AI (XAI) ermöglicht es, Entscheidungsprozesse besser zu verstehen."
                )
            },
            "frage43": {
                "text": "Wie verhält sich der EU AI Act zu anderen EU-Rechtsvorschriften?",
                "optionen": [
                    "Der EU AI Act ergänzt bestehende Rechtsvorschriften (z.B. Produktsicherheit)",
                    "Er ersetzt alle anderen Gesetze",
                    "Er ist nachrangig gegenüber jeder Richtlinie",
                    "Er ist ohne Bezug zu anderem EU-Recht"
                ],
                "erklärung": (
                    "Der AI Act koexistiert mit anderen Rechtsvorschriften und bildet einen zusätzlichen Rahmen."
                )
            },
            "frage44": {
                "text": "Wie steht der EU AI Act zu KI-basierten sozialen Scoring-Systemen?",
                "optionen": [
                    "KI-Systeme dürfen nicht zum sozialen Scoring eingesetzt werden, wenn Grundrechte verletzt werden",
                    "Soziales Scoring ist immer erlaubt",
                    "Es gibt keine Regelung zum sozialen Scoring",
                    "Nur private Unternehmen dürfen es einsetzen"
                ],
                "erklärung": (
                    "Soziale Scoring-Systeme, die Grundrechte beeinträchtigen, fallen unter die verbotenen Praktiken."
                )
            },
            "frage45": {
                "text": "Welche technischen Anforderungen werden an Hochrisiko-KI-Systeme gestellt?",
                "optionen": [
                    "Ein hohes Maß an Cybersicherheit und Robustheit ist vorgeschrieben",
                    "Keine technischen Anforderungen",
                    "Nur Minimalkonfigurationen",
                    "Sie müssen ausschließlich offline betrieben werden"
                ],
                "erklärung": (
                    "Der AI Act verlangt, dass Hochrisiko-KI-Systeme robust, sicher und vor Manipulation geschützt sind."
                )
            },
            "frage46": {
                "text": "Wie sollten Hochrisiko-KI-Systeme im Hinblick auf Diskriminierung gestaltet sein?",
                "optionen": [
                    "Nicht diskriminierend, fair und inklusiv sein",
                    "Leichte Diskriminierung ist erlaubt",
                    "Nur nach Geschlecht differenzieren",
                    "Es gibt keine Vorgaben zur Fairness"
                ],
                "erklärung": (
                    "Ein zentrales Ziel ist es, Diskriminierung zu vermeiden und Fairness zu gewährleisten."
                )
            },
            "frage47": {
                "text": "Was gilt in Bezug auf Dokumentations- und Berichtspflichten?",
                "optionen": [
                    "Alle Dokumentations- und Berichtspflichten müssen erfüllt werden",
                    "Es reicht ein kurzes internes Memo",
                    "Pflichten gelten nur für Forschungsprojekte",
                    "Es gibt keine Berichtspflichten"
                ],
                "erklärung": (
                    "Der AI Act sieht umfangreiche Dokumentationspflichten vor, besonders bei Hochrisiko-KI-Systemen."
                )
            },
            "frage48": {
                "text": "Was ist hinsichtlich Bias und Fehlern in KI-Systemen zu beachten?",
                "optionen": [
                    "Ständige Überwachung auf mögliche Bias und Fehler",
                    "Bias ist unvermeidlich und wird toleriert",
                    "Nur ein einmaliger Test zu Projektbeginn",
                    "Fehler sind irrelevant, Hauptsache es läuft"
                ],
                "erklärung": (
                    "Ein kontinuierliches Monitoring ist unerlässlich, um unfaire Verzerrungen und Fehler schnell zu erkennen."
                )
            },
            "frage49": {
                "text": "Wie erfolgt die Klassifizierung aller KI-Systeme unter dem EU AI Act?",
                "optionen": [
                    "Alle KI-Systeme müssen nach dem risikobasierten Ansatz klassifiziert werden",
                    "Nur Hochrisiko-KI wird klassifiziert",
                    "Es gibt gar keine Klassifizierung",
                    "Die Klassifizierung erfolgt rein nach Marktanteil"
                ],
                "erklärung": (
                    "Der risikobasierte Ansatz unterscheidet zwischen unannehmbaren, hohen, begrenzten und minimalen Risiken."
                )
            },
            "frage50": {
                "text": "Kann es zu behördlichen Sanktionen kommen, wenn gegen den EU AI Act verstoßen wird?",
                "optionen": [
                    "Ja, Verstöße können behördlich sanktioniert und geahndet werden",
                    "Nein, der AI Act ist nur eine Empfehlung",
                    "Strafen gelten nur bei Patentrechtsverletzungen",
                    "Nur bei Unfällen mit Personenschäden"
                ],
                "erklärung": (
                    "Behörden können empfindliche Strafen verhängen, darunter Geldbußen und Marktrücknahmen."
                )
            }
        }

    # ----------------------------------------------------------------
    # EVALUIERUNGSFUNKTION MIT 50 PARAMETERN
    # ----------------------------------------------------------------
    def evaluate_answers(
        self,
        a1: str, a2: str, a3: str, a4: str, a5: str,
        a6: str, a7: str, a8: str, a9: str, a10: str,
        a11: str, a12: str, a13: str, a14: str, a15: str,
        a16: str, a17: str, a18: str, a19: str, a20: str,
        a21: str, a22: str, a23: str, a24: str, a25: str,
        a26: str, a27: str, a28: str, a29: str, a30: str,
        a31: str, a32: str, a33: str, a34: str, a35: str,
        a36: str, a37: str, a38: str, a39: str, a40: str,
        a41: str, a42: str, a43: str, a44: str, a45: str,
        a46: str, a47: str, a48: str, a49: str, a50: str
    ) -> str:
        """
        Diese Methode wertet die Antworten aus und liefert ein Ergebnis sowie detailliertes Feedback.
        Bei falschen Antworten wird zusätzlich der Fragetext, die vom Benutzer gegebene Antwort
        und die korrekte Antwort angezeigt.
        """
        # Alle Antworten in einem Dictionary zusammenfassen
        antworten: dict[str, str] = {
            "frage1": a1,   "frage2": a2,   "frage3": a3,   "frage4": a4,   "frage5": a5,
            "frage6": a6,   "frage7": a7,   "frage8": a8,   "frage9": a9,   "frage10": a10,
            "frage11": a11, "frage12": a12, "frage13": a13, "frage14": a14, "frage15": a15,
            "frage16": a16, "frage17": a17, "frage18": a18, "frage19": a19, "frage20": a20,
            "frage21": a21, "frage22": a22, "frage23": a23, "frage24": a24, "frage25": a25,
            "frage26": a26, "frage27": a27, "frage28": a28, "frage29": a29, "frage30": a30,
            "frage31": a31, "frage32": a32, "frage33": a33, "frage34": a34, "frage35": a35,
            "frage36": a36, "frage37": a37, "frage38": a38, "frage39": a39, "frage40": a40,
            "frage41": a41, "frage42": a42, "frage43": a43, "frage44": a44, "frage45": a45,
            "frage46": a46, "frage47": a47, "frage48": a48, "frage49": a49, "frage50": a50
        }

        score = 0
        feedback = ""

        for frage_id, user_antwort in antworten.items():
            korrekte_antwort = self.korrekte_antworten[frage_id]
            if user_antwort == korrekte_antwort:
                score += 1
            else:
                # Füge ins Feedback den Fragetext, die falsche Antwort und die korrekte Antwort ein
                feedback += (
                    f"Frage: {self.fragen[frage_id]['text']}\n"
                    f"Deine Antwort: {user_antwort}\n"
                    f"Richtige Antwort: {korrekte_antwort}\n"
                    f"Erklärung: {self.fragen[frage_id]['erklärung']}\n\n"
                )

        # Ergebnisanzeige
        result = f"Du hast {score} von 50 Fragen richtig beantwortet.\n"
        if score == 50:
            result += "Ausgezeichnet! Dein Wissen entspricht den höchsten Anforderungen des EU AI Acts."
        elif score >= 40:
            result += "Sehr gut gemacht, aber es gibt noch Raum für Verbesserungen."
        elif score >= 25:
            result += "Solides Ergebnis, aber bitte vertiefe dein Wissen in den genannten Bereichen."
        else:
            result += "Bitte wiederhole die Schulungsinhalte und konsultiere die weiterführenden Materialien."

        if feedback:
            result += "\n\nFeedback zu den falsch beantworteten Fragen:\n" + feedback
        return result

    def build_tab(self) -> None:
        """
        Diese Methode baut den erweiterten Tab für den Mitarbeitertest in der Gradio-App.
        """
        with gr.TabItem("Mitarbeitertest (50 Fragen)"):

            gr.Markdown(
                """
                # Mitarbeitertest (50 Fragen) zum EU AI Act
                **Erstellt von: CipherCore - Sicherheit in der Programmierung**

                **Wichtig:**
                - Dieser Test ist nicht erschöpfend und deckt nicht alle Nuancen des EU AI Acts ab.
                - Er dient als Ergänzung zu umfassenderen Schulungen und Informationsmaterialien.
                - Die Platzhalterfragen 13-50 können an Deine konkreten Bedürfnisse angepasst werden.

                **Nächste Schritte für 100%ige Konformität:**
                - Zusätzliche, detailliertere Fragen (z.B. zu Datenqualität, technischer Dokumentation und menschlicher Aufsicht)
                - Einbau von Fallstudien oder Szenarien zur praxisnahen Überprüfung
                - Bereitstellung detaillierterer Erklärungen und weiterführender Links bei falschen Antworten
                """
            )

            # Wir bauen 50 Radio-Elemente auf
            frage1  = gr.Radio(self.fragen["frage1"]["optionen"],  label=self.fragen["frage1"]["text"])
            frage2  = gr.Radio(self.fragen["frage2"]["optionen"],  label=self.fragen["frage2"]["text"])
            frage3  = gr.Radio(self.fragen["frage3"]["optionen"],  label=self.fragen["frage3"]["text"])
            frage4  = gr.Radio(self.fragen["frage4"]["optionen"],  label=self.fragen["frage4"]["text"])
            frage5  = gr.Radio(self.fragen["frage5"]["optionen"],  label=self.fragen["frage5"]["text"])
            frage6  = gr.Radio(self.fragen["frage6"]["optionen"],  label=self.fragen["frage6"]["text"])
            frage7  = gr.Radio(self.fragen["frage7"]["optionen"],  label=self.fragen["frage7"]["text"])
            frage8  = gr.Radio(self.fragen["frage8"]["optionen"],  label=self.fragen["frage8"]["text"])
            frage9  = gr.Radio(self.fragen["frage9"]["optionen"],  label=self.fragen["frage9"]["text"])
            frage10 = gr.Radio(self.fragen["frage10"]["optionen"], label=self.fragen["frage10"]["text"])
            frage11 = gr.Radio(self.fragen["frage11"]["optionen"], label=self.fragen["frage11"]["text"])
            frage12 = gr.Radio(self.fragen["frage12"]["optionen"], label=self.fragen["frage12"]["text"])

            frage13 = gr.Radio(self.fragen["frage13"]["optionen"], label=self.fragen["frage13"]["text"])
            frage14 = gr.Radio(self.fragen["frage14"]["optionen"], label=self.fragen["frage14"]["text"])
            frage15 = gr.Radio(self.fragen["frage15"]["optionen"], label=self.fragen["frage15"]["text"])
            frage16 = gr.Radio(self.fragen["frage16"]["optionen"], label=self.fragen["frage16"]["text"])
            frage17 = gr.Radio(self.fragen["frage17"]["optionen"], label=self.fragen["frage17"]["text"])
            frage18 = gr.Radio(self.fragen["frage18"]["optionen"], label=self.fragen["frage18"]["text"])
            frage19 = gr.Radio(self.fragen["frage19"]["optionen"], label=self.fragen["frage19"]["text"])
            frage20 = gr.Radio(self.fragen["frage20"]["optionen"], label=self.fragen["frage20"]["text"])
            frage21 = gr.Radio(self.fragen["frage21"]["optionen"], label=self.fragen["frage21"]["text"])
            frage22 = gr.Radio(self.fragen["frage22"]["optionen"], label=self.fragen["frage22"]["text"])
            frage23 = gr.Radio(self.fragen["frage23"]["optionen"], label=self.fragen["frage23"]["text"])
            frage24 = gr.Radio(self.fragen["frage24"]["optionen"], label=self.fragen["frage24"]["text"])
            frage25 = gr.Radio(self.fragen["frage25"]["optionen"], label=self.fragen["frage25"]["text"])
            frage26 = gr.Radio(self.fragen["frage26"]["optionen"], label=self.fragen["frage26"]["text"])
            frage27 = gr.Radio(self.fragen["frage27"]["optionen"], label=self.fragen["frage27"]["text"])
            frage28 = gr.Radio(self.fragen["frage28"]["optionen"], label=self.fragen["frage28"]["text"])
            frage29 = gr.Radio(self.fragen["frage29"]["optionen"], label=self.fragen["frage29"]["text"])
            frage30 = gr.Radio(self.fragen["frage30"]["optionen"], label=self.fragen["frage30"]["text"])
            frage31 = gr.Radio(self.fragen["frage31"]["optionen"], label=self.fragen["frage31"]["text"])
            frage32 = gr.Radio(self.fragen["frage32"]["optionen"], label=self.fragen["frage32"]["text"])
            frage33 = gr.Radio(self.fragen["frage33"]["optionen"], label=self.fragen["frage33"]["text"])
            frage34 = gr.Radio(self.fragen["frage34"]["optionen"], label=self.fragen["frage34"]["text"])
            frage35 = gr.Radio(self.fragen["frage35"]["optionen"], label=self.fragen["frage35"]["text"])
            frage36 = gr.Radio(self.fragen["frage36"]["optionen"], label=self.fragen["frage36"]["text"])
            frage37 = gr.Radio(self.fragen["frage37"]["optionen"], label=self.fragen["frage37"]["text"])
            frage38 = gr.Radio(self.fragen["frage38"]["optionen"], label=self.fragen["frage38"]["text"])
            frage39 = gr.Radio(self.fragen["frage39"]["optionen"], label=self.fragen["frage39"]["text"])
            frage40 = gr.Radio(self.fragen["frage40"]["optionen"], label=self.fragen["frage40"]["text"])
            frage41 = gr.Radio(self.fragen["frage41"]["optionen"], label=self.fragen["frage41"]["text"])
            frage42 = gr.Radio(self.fragen["frage42"]["optionen"], label=self.fragen["frage42"]["text"])
            frage43 = gr.Radio(self.fragen["frage43"]["optionen"], label=self.fragen["frage43"]["text"])
            frage44 = gr.Radio(self.fragen["frage44"]["optionen"], label=self.fragen["frage44"]["text"])
            frage45 = gr.Radio(self.fragen["frage45"]["optionen"], label=self.fragen["frage45"]["text"])
            frage46 = gr.Radio(self.fragen["frage46"]["optionen"], label=self.fragen["frage46"]["text"])
            frage47 = gr.Radio(self.fragen["frage47"]["optionen"], label=self.fragen["frage47"]["text"])
            frage48 = gr.Radio(self.fragen["frage48"]["optionen"], label=self.fragen["frage48"]["text"])
            frage49 = gr.Radio(self.fragen["frage49"]["optionen"], label=self.fragen["frage49"]["text"])
            frage50 = gr.Radio(self.fragen["frage50"]["optionen"], label=self.fragen["frage50"]["text"])

            # Ausgabefeld
            result_box = gr.Textbox(label="Testergebnis", interactive=False)

            # Button zur Auswertung
            submit_btn = gr.Button("Test auswerten")

            # Klick-Event mit 50 Inputs
            submit_btn.click(
                self.evaluate_answers,
                inputs=[
                    frage1, frage2, frage3, frage4, frage5,
                    frage6, frage7, frage8, frage9, frage10,
                    frage11, frage12, frage13, frage14, frage15,
                    frage16, frage17, frage18, frage19, frage20,
                    frage21, frage22, frage23, frage24, frage25,
                    frage26, frage27, frage28, frage29, frage30,
                    frage31, frage32, frage33, frage34, frage35,
                    frage36, frage37, frage38, frage39, frage40,
                    frage41, frage42, frage43, frage44, frage45,
                    frage46, frage47, frage48, frage49, frage50
                ],
                outputs=result_box
            )

# ------------------------------------------------------------------------------
# Standalone-Ausführung (zum Testen ohne Einbindung in eine größere App)
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    with gr.Blocks(title="Mitarbeitertest - Fragen zum EU AI Act - CipherCore") as demo:
        MitarbeiterTest50().build_tab()
    demo.launch()