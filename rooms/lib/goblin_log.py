# -*- coding: utf-8 -*-

import random
from pathlib import Path
from datetime import datetime, timedelta


# ============================================================
# PATHS
# ============================================================

def get_workfiles_path():
    """
    Ermittelt den WorkFiles-Ordner relativ zum Projekt.

    goblin_log.py liegt unter:
    rooms/lib/goblin_log.py

    WorkFiles liegt unter:
    WorkFiles/
    """

    goblin_projet = Path(__file__).resolve().parent.parent.parent
    goblin_workfiles = goblin_projet / "WorkFiles"

    goblin_workfiles.mkdir(
        parents=True,
        exist_ok=True
    )

    return goblin_workfiles


def get_challenge_files():
    """
    Liefert die beiden Dateien der Challenge zurueck.
    """

    goblin_workfiles = get_workfiles_path()

    goblin_ip = goblin_workfiles / "IP.txt"
    goblin_events = goblin_workfiles / "Events.txt"

    return goblin_ip, goblin_events


# ============================================================
# RESET CHALLENGE
# ============================================================

def reset_challenge():
    """
    Loescht die gespeicherten Challenge-Daten.

    Beim naechsten Aufruf von create_log_events()
    werden neue IP-Adressen und neue Events erzeugt.

    Rueckgabe:
        True  -> mindestens eine Datei wurde geloescht
        False -> keine Datei war vorhanden
    """

    goblin_ip, goblin_events = get_challenge_files()

    fichier_supprime = False

    for goblin_fichier in [
        goblin_ip,
        goblin_events
    ]:

        if goblin_fichier.exists():
            goblin_fichier.unlink()
            fichier_supprime = True

    return fichier_supprime


# ============================================================
# FILE CHECKS
# ============================================================

def file_has_data(goblin_fichier):
    """
    Prueft, ob eine Datei existiert und nicht leer ist.
    """

    return (
        goblin_fichier.exists()
        and goblin_fichier.is_file()
        and goblin_fichier.stat().st_size > 0
    )


def load_ip_addresses(goblin_ip):
    """
    Liest IP-Adressen aus IP.txt.

    Leere Zeilen werden ignoriert.
    """

    adresses_ip = []

    with open(
        goblin_ip,
        "r",
        encoding="utf-8"
    ) as fichier:

        for ligne in fichier:

            adresse_ip = ligne.strip()

            if adresse_ip:
                adresses_ip.append(adresse_ip)

    return adresses_ip


def load_log_events(goblin_events):
    """
    Liest Log-Events aus Events.txt.

    Leere Zeilen werden ignoriert.
    """

    evenements = []

    with open(
        goblin_events,
        "r",
        encoding="utf-8"
    ) as fichier:

        for ligne in fichier:

            evenement = ligne.strip()

            if evenement:
                evenements.append(evenement)

    return evenements


# ============================================================
# RANDOM IP GENERATION
# ============================================================

def create_random_ip():
    """
    Erzeugt eine zufaellige private IPv4-Adresse.

    Moegliche private Bereiche:

    10.x.x.x
    172.16.x.x bis 172.31.x.x
    192.168.x.x
    """

    type_reseau = random.choice([
        "10",
        "172",
        "192"
    ])

    if type_reseau == "10":

        adresse_ip = (
            f"10."
            f"{random.randint(0, 255)}."
            f"{random.randint(0, 255)}."
            f"{random.randint(1, 254)}"
        )

    elif type_reseau == "172":

        adresse_ip = (
            f"172."
            f"{random.randint(16, 31)}."
            f"{random.randint(0, 255)}."
            f"{random.randint(1, 254)}"
        )

    else:

        adresse_ip = (
            f"192.168."
            f"{random.randint(0, 255)}."
            f"{random.randint(1, 254)}"
        )

    return adresse_ip


def create_ip_addresses(anzahl=5):
    """
    Erzeugt eine Liste mit eindeutigen IP-Adressen.
    """

    adresses_ip = []

    while len(adresses_ip) < anzahl:

        adresse_ip = create_random_ip()

        if adresse_ip not in adresses_ip:
            adresses_ip.append(adresse_ip)

    return adresses_ip


# ============================================================
# TIME GENERATION
# ============================================================

def create_time(start_time, minutes):
    """
    Erzeugt eine Uhrzeit fuer einen Log-Eintrag.
    """

    heure_depart = datetime.strptime(
        start_time,
        "%H:%M"
    )

    nouvelle_heure = (
        heure_depart
        + timedelta(minutes=minutes)
    )

    return nouvelle_heure.strftime("%H:%M")


# ============================================================
# DYNAMIC LOG GENERATION
# ============================================================

def generate_log_events(adresses_ip):
    """
    Erzeugt Log-Eintraege.

    Genau eine IP-Adresse erzeugt mindestens
    drei FAILED LOGINs.
    """

    adresse_suspecte = random.choice(
        adresses_ip
    )

    evenements = []

    minute = 0

    # --------------------------------------------------------
    # Normale SUCCESS-Logins
    # --------------------------------------------------------

    for adresse_ip in adresses_ip:

        heure = create_time(
            "10:00",
            minute
        )

        evenements.append(
            f"{heure} LOGIN "
            f"{adresse_ip} SUCCESS"
        )

        minute += random.randint(
            2,
            5
        )

    # --------------------------------------------------------
    # Drei FAILED-Logins der verdaechtigen IP
    # --------------------------------------------------------

    for _ in range(3):

        heure = create_time(
            "10:00",
            minute
        )

        evenements.append(
            f"{heure} LOGIN "
            f"{adresse_suspecte} FAILED"
        )

        minute += random.randint(
            1,
            4
        )

    # --------------------------------------------------------
    # Zusaetzliche FAILED-Logins anderer IPs
    # aber jeweils weniger als 3
    # --------------------------------------------------------

    autres_adresses = [
        adresse_ip
        for adresse_ip in adresses_ip
        if adresse_ip != adresse_suspecte
    ]

    nombre_autres = min(
        2,
        len(autres_adresses)
    )

    for adresse_ip in random.sample(
        autres_adresses,
        nombre_autres
    ):

        heure = create_time(
            "10:00",
            minute
        )

        evenements.append(
            f"{heure} LOGIN "
            f"{adresse_ip} FAILED"
        )

        minute += random.randint(
            1,
            4
        )

    # --------------------------------------------------------
    # Stoer-Events
    # --------------------------------------------------------

    heure = create_time(
        "10:00",
        minute
    )

    evenements.append(
        f"{heure} BACKUP "
        f"SERVER01 SUCCESS"
    )

    minute += 2

    heure = create_time(
        "10:00",
        minute
    )

    evenements.append(
        f"{heure} FILE "
        f"SERVER02 SUCCESS"
    )

    # --------------------------------------------------------
    # Reihenfolge mischen
    # --------------------------------------------------------

    random.shuffle(evenements)

    return evenements


# ============================================================
# SAVE FILES
# ============================================================

def save_ip_addresses(
    goblin_ip,
    adresses_ip
):
    """
    Speichert IP-Adressen in IP.txt.
    """

    with open(
        goblin_ip,
        "w",
        encoding="utf-8"
    ) as fichier:

        for adresse_ip in adresses_ip:
            fichier.write(
                adresse_ip + "\n"
            )


def save_log_events(
    goblin_events,
    evenements
):
    """
    Speichert Log-Events in Events.txt.
    """

    with open(
        goblin_events,
        "w",
        encoding="utf-8"
    ) as fichier:

        for evenement in evenements:
            fichier.write(
                evenement + "\n"
            )


# ============================================================
# MAIN CREATION / LOAD FUNCTION
# ============================================================

def create_log_events():
    """
    Hauptfunktion fuer Level 1.

    Verhalten:

    1. Wenn IP.txt UND Events.txt existieren
       und Daten enthalten:
       -> bestehende Daten laden

    2. Andernfalls:
       -> IP-Adressen dynamisch erzeugen
       -> Events dynamisch erzeugen
       -> beide Dateien speichern

    Rueckgabe:
        Liste der Log-Events
    """

    goblin_ip, goblin_events = get_challenge_files()

    # --------------------------------------------------------
    # Bestehende Daten verwenden
    # --------------------------------------------------------

    if (
        file_has_data(goblin_ip)
        and file_has_data(goblin_events)
    ):

        adresses_ip = load_ip_addresses(
            goblin_ip
        )

        evenements = load_log_events(
            goblin_events
        )

        if (
            len(adresses_ip) > 0
            and len(evenements) > 0
        ):

            return evenements

    # --------------------------------------------------------
    # Neue Daten erzeugen
    # --------------------------------------------------------

    adresses_ip = create_ip_addresses(
        5
    )

    evenements = generate_log_events(
        adresses_ip
    )

    # --------------------------------------------------------
    # Neue Daten speichern
    # --------------------------------------------------------

    save_ip_addresses(
        goblin_ip,
        adresses_ip
    )

    save_log_events(
        goblin_events,
        evenements
    )

    return evenements


# ============================================================
# LOG ANALYSIS
# ============================================================

def parse_log_event(evenement):
    """
    Zerlegt einen LOGIN-Logeintrag.

    Beispiel:

    10:15 LOGIN 10.10.8.23 FAILED
    """

    parties = evenement.split()

    if len(parties) != 4:
        return None

    if parties[1] != "LOGIN":
        return None

    donnees = {
        "heure": parties[0],
        "type": parties[1],
        "adresse_ip": parties[2],
        "statut": parties[3]
    }

    return donnees


def count_failed_logins(evenements):
    """
    Zaehlt FAILED LOGINs pro IP-Adresse.
    """

    echecs = {}

    for evenement in evenements:

        donnees = parse_log_event(
            evenement
        )

        if donnees is None:
            continue

        if donnees["statut"] == "FAILED":

            adresse_ip = (
                donnees["adresse_ip"]
            )

            if adresse_ip not in echecs:
                echecs[adresse_ip] = 0

            echecs[adresse_ip] += 1

    return echecs


def find_suspicious_ip(
    evenements,
    limite=3
):
    """
    Liefert die IP-Adresse zurueck,
    die mindestens 'limite'
    fehlgeschlagene Login-Versuche hat.
    """

    echecs = count_failed_logins(
        evenements
    )

    for (
        adresse_ip,
        nombre_echecs
    ) in echecs.items():

        if nombre_echecs >= limite:
            return adresse_ip

    return None


def verify_solution(data):
    """
    Referenzloesung fuer das Escape-Room-Framework.
    """

    return find_suspicious_ip(
        data
    )