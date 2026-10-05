import random
import string

import lib.goblin_log as GL


# ============================================================
# MESSAGES
# ============================================================

def create_secret_message():
    """
    Waehlt zufaellig eine Nachricht aus.

    Diese Nachricht wird spaeter fuer Level 3 verwendet.
    """

    messages = [
        "FIND_STOLEN_DATA",
        "CHECK_DATA_FILE",
        "SEARCH_FOR_GOBLIN",
        "FIND_MODIFIED_DATA"
    ]

    return random.choice(messages)


# ============================================================
# IP KEY
# ============================================================

def get_suspicious_ip():
    """
    Ermittelt die verdaechtige IP-Adresse aus den
    bestehenden Events von Level 1.

    Dadurch wird Level 2 direkt mit Level 1 verbunden.
    """

    evenements = GL.create_log_events()

    adresse_suspecte = GL.find_suspicious_ip(
        evenements
    )

    return adresse_suspecte


def calculate_rotation(adresse_ip, text_length):
    """
    Berechnet die Rotation aus der IP-Adresse.

    Beispiel:

    10.10.8.23

    10 + 10 + 8 + 23 = 51

    Rotation:
    51 % Laenge des Strings
    """

    parties_ip = adresse_ip.split(".")

    somme = 0

    for partie in parties_ip:
        somme += int(partie)

    if text_length == 0:
        return 0

    rotation = somme % text_length

    return rotation


# ============================================================
# NOISE
# ============================================================

def create_noise_character():
    """
    Erzeugt ein zufaelliges Stoerzeichen.
    """

    caracteres = (
        string.ascii_letters
        + string.digits
    )

    return random.choice(caracteres)


def add_noise(message):
    """
    Fuegt nach jedem echten Zeichen ein zufaelliges
    Stoerzeichen ein.

    Beispiel:

    DATA

    kann werden:

    D7AxT4Aq
    """

    resultat = ""

    for caractere in message:

        resultat += caractere
        resultat += create_noise_character()

    return resultat


# ============================================================
# ROTATION
# ============================================================

def rotate_right(texte, rotation):
    """
    Rotiert einen String nach rechts.
    """

    if len(texte) == 0:
        return texte

    rotation = rotation % len(texte)

    if rotation == 0:
        return texte

    return (
        texte[-rotation:]
        + texte[:-rotation]
    )


def rotate_left(texte, rotation):
    """
    Macht eine Rechtsrotation rueckgaengig.
    """

    if len(texte) == 0:
        return texte

    rotation = rotation % len(texte)

    if rotation == 0:
        return texte

    return (
        texte[rotation:]
        + texte[:rotation]
    )


# ============================================================
# ENCRYPTION
# ============================================================

def encrypt_message(
    message,
    adresse_ip
):
    """
    Verschluesselt die Nachricht.

    Schritte:

    1. Stoerzeichen einfuegen
    2. String umdrehen
    3. Mit IP-basiertem Wert rotieren
    """

    # Schritt 1:
    # Stoerzeichen einfuegen

    message_brouille = add_noise(
        message
    )

    # Schritt 2:
    # Reihenfolge umdrehen

    message_inverse = (
        message_brouille[::-1]
    )

    # Schritt 3:
    # Rotation berechnen

    rotation = calculate_rotation(
        adresse_ip,
        len(message_inverse)
    )

    # Nachricht rotieren

    message_chiffre = rotate_right(
        message_inverse,
        rotation
    )

    return message_chiffre


# ============================================================
# DECRYPTION
# ============================================================

def decrypt_message(
    message_chiffre,
    adresse_ip
):
    """
    Entschluesselt die Nachricht.

    Die Schritte der Verschluesselung werden
    in umgekehrter Reihenfolge ausgefuehrt.

    1. Rotation rueckgaengig machen
    2. String wieder umdrehen
    3. Stoerzeichen entfernen
    """

    # --------------------------------------------
    # Rotation berechnen
    # --------------------------------------------

    rotation = calculate_rotation(
        adresse_ip,
        len(message_chiffre)
    )

    # --------------------------------------------
    # Schritt 1:
    # Rotation rueckgaengig machen
    # --------------------------------------------

    message_derote = rotate_left(
        message_chiffre,
        rotation
    )

    # --------------------------------------------
    # Schritt 2:
    # String wieder umdrehen
    # --------------------------------------------

    message_normal = (
        message_derote[::-1]
    )

    # --------------------------------------------
    # Schritt 3:
    # Jedes zweite Zeichen nehmen
    #
    # Die echten Zeichen befinden sich an:
    #
    # 0, 2, 4, 6, ...
    # --------------------------------------------

    message_dechiffre = (
        message_normal[::2]
    )

    return message_dechiffre


# ============================================================
# CREATE CHALLENGE
# ============================================================

def create_challenge():
    """
    Erstellt die Daten fuer Level 2.
    """

    adresse_ip = get_suspicious_ip()

    message_original = (
        create_secret_message()
    )

    message_chiffre = encrypt_message(
        message_original,
        adresse_ip
    )

    donnees = {
        "message": message_chiffre,
        "adresse_ip": adresse_ip
    }

    return donnees


# ============================================================
# REFERENCE SOLUTION
# ============================================================

def verify_solution(data):
    """
    Referenzloesung fuer das Escape-Room-Framework.
    """

    message_chiffre = data["message"]
    adresse_ip = data["adresse_ip"]

    return decrypt_message(
        message_chiffre,
        adresse_ip
    )