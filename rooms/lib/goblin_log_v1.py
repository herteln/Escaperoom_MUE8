
import random


def create_log_events():
    """
    Erzeugt Log-Eintraege fuer Level 1.
    Eine IP-Adresse verursacht mindestens drei FAILED LOGINs.
    """

    adresses_ip = [
        "192.168.1.15",
        "192.168.1.20",
        "10.10.8.23",
        "172.16.0.12",
        "192.168.1.44"
    ]

    adresse_suspecte = random.choice(adresses_ip)

    evenements = [
        "10:01 LOGIN 192.168.1.15 SUCCESS",
        "10:04 LOGIN 192.168.1.20 SUCCESS",
        "10:07 LOGIN 172.16.0.12 FAILED",
        "10:10 BACKUP SERVER01 SUCCESS",
        "10:12 LOGIN 192.168.1.44 SUCCESS"
    ]

    # Drei fehlgeschlagene Logins der verdaechtigen IP

    evenements.append(
        f"10:15 LOGIN {adresse_suspecte} FAILED"
    )

    evenements.append(
        f"10:17 LOGIN {adresse_suspecte} FAILED"
    )

    evenements.append(
        f"10:19 LOGIN {adresse_suspecte} FAILED"
    )

    # Weitere normale bzw. stoerende Events

    evenements.extend([
        "10:21 LOGIN 192.168.1.15 SUCCESS",
        "10:23 FILE SERVER02 SUCCESS",
        "10:25 LOGIN 192.168.1.20 FAILED"
    ])

    random.shuffle(evenements)

    return evenements


def parse_log_event(evenement):
    """
    Zerlegt einen Log-Eintrag.

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
    Zaehlt fehlgeschlagene Login-Versuche pro IP-Adresse.
    """

    echecs = {}

    for evenement in evenements:

        donnees = parse_log_event(evenement)

        if donnees is None:
            continue

        if donnees["statut"] == "FAILED":

            adresse_ip = donnees["adresse_ip"]

            if adresse_ip not in echecs:
                echecs[adresse_ip] = 0

            echecs[adresse_ip] += 1

    return echecs


def find_suspicious_ip(evenements):
    """
    Findet die IP-Adresse mit mindestens drei Fehlversuchen.
    """

    echecs = count_failed_logins(evenements)

    for adresse_ip, nombre_echecs in echecs.items():

        if nombre_echecs >= 3:
            return adresse_ip

    return None


def verify_solution(data):
    """
    Referenzloesung des Escape-Room-Frameworks.
    """

    return find_suspicious_ip(data)