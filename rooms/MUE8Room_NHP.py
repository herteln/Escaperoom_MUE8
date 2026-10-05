
import string

from EscapeRoom import EscapeRoom

import lib.goblin_log as GL
import lib.encrypted_message as EM
import lib.stolen_data as SD


class MUE8Room_NHP(EscapeRoom):

    def __init__(self):

        super().__init__()

        self.set_metadata(
            "Nicole Hertel-Pirner",
            __name__
        )

        self.add_level(self.create_level1())
        self.add_level(self.create_level2())
        self.add_level(self.create_level3())


    # ============================================================
    # LEVEL 1
    # Goblin Log Analyzer
    # ============================================================

    def create_level1(self):

        evenements = GL.create_log_events()

        lignes_log = "<br>".join(evenements)

        task_messages = [
            "<b>Level 1 - Goblin Log Analyzer</b>",
            "",
            "Der gruene Kobold hat versucht, sich Zugang zum System zu verschaffen.",
            "",
            "Die Security-Abteilung konnte die folgenden Log-Eintraege sichern:",
            "",
            lignes_log,
            "",
            "<b>Aufgabe:</b>",
            "Analysiere die Login-Events.",
            "",
            "Ermittle die IP-Adresse, von der mindestens drei "
            "fehlgeschlagene Login-Versuche stammen.",
            "",
            "Dein Python-Programm soll die verdaechtige IP-Adresse zurueckgeben."
        ]

        hints = [
            "Durchlaufe die Liste mit einer for-Schleife.",
            "Mit split() kannst du jede Log-Zeile zerlegen.",
            "Beruecksichtige nur LOGIN-Eintraege mit dem Status FAILED.",
            "Ein Dictionary eignet sich zum Zaehlen der Fehlversuche pro IP-Adresse."
        ]

        return {
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": GL.verify_solution,
            "data": evenements
        }


    # ============================================================
    # LEVEL 2
    # Encrypted Message
    # ============================================================

    def create_level2(self):

        donnees = EM.create_challenge()

        task_messages = [
            "<b>Level 2 - Encrypted Message</b>",
            "",
            "Der gruene Kobold hat nach seinem "
            "fehlgeschlagenen Login-Versuch eine "
            "verschluesselte Nachricht hinterlassen.",
            "",
            "Die in Level 1 gefundene IP-Adresse "
            "ist Teil des Verschluesselungsschluessels.",
            "",
            "<b>Verdaechtige IP-Adresse:</b>",
            donnees["adresse_ip"],
            "",
            "<b>Verschluesselte Nachricht:</b>",
            donnees["message"],
            "",
            "<b>Aufgabe:</b>",
            "",
            "Entschluessle die Nachricht des Kobolds.",
            "",
            "Der Kobold hat zwischen die echten Zeichen "
            "zufaellige Stoerzeichen eingefuegt.",
            "Danach wurde die Zeichenfolge umgedreht "
            "und anhand der IP-Adresse rotiert.",
            "",
            "Dein Python-Programm soll die "
            "entschluesselte Nachricht zurueckgeben."
        ]

        hints = [
            "Die IP-Adresse aus Level 1 ist auch "
            "fuer dieses Level wichtig.",

            "Addiere die vier Zahlenbloecke der "
            "IP-Adresse. Der Modulo-Operator % "
            "koennte hilfreich sein.",

            "Der Kobold hat zuerst echte Zeichen "
            "mit Stoerzeichen vermischt und "
            "anschliessend die Reihenfolge veraendert.",

            "Nachdem du Rotation und Umkehrung "
            "rueckgaengig gemacht hast, befindet sich "
            "die echte Nachricht an jeder zweiten Position."
        ]

        return {
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": EM.verify_solution,
            "data": donnees
        }


    # ============================================================
    # LEVEL 3
    # Stolen Data File
    # ============================================================

    def create_level3(self):

        donnees = SD.create_challenge()

        task_messages = [
            "<b>Level 3 - Stolen Data File</b>",
            "",
            "Der gruene Kobold hat Datensaetze manipuliert.",
            "",
            "Identifiziere den manipulierten Datensatz."
        ]

        hints = [
            "Vergleiche die Werte der Datensaetze.",
            "Achte auf ungewoehnliche oder unplausible Werte.",
            "Dictionaries und Schleifen koennen dir helfen."
        ]

        return {
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": SD.verify_solution,
            "data": donnees
        }