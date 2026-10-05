def run(data):

    message_chiffre = data["message"]
    adresse_ip = "99.99.99" #data["adresse_ip"]

    # ========================================================
    # 1. Rotation aus IP-Adresse berechnen
    # ========================================================

    parties_ip = adresse_ip.split(".")

    somme = 0

    for partie in parties_ip:
        somme += int(partie)

    rotation = (
        somme
        % len(message_chiffre)
    )

    # ========================================================
    # 2. Rotation rueckgaengig machen
    # ========================================================

    if rotation > 0:

        message_derote = (
            message_chiffre[rotation:]
            + message_chiffre[:rotation]
        )

    else:

        message_derote = (
            message_chiffre
        )

    # ========================================================
    # 3. String wieder umdrehen
    # ========================================================

    message_normal = (
        message_derote[::-1]
    )

    # ========================================================
    # 4. Stoerzeichen entfernen
    #
    # Originalzeichen:
    #
    # Index 0
    # Index 2
    # Index 4
    # ...
    # ========================================================

    message_dechiffre = ""

    for index in range(
        0,
        len(message_normal),
        2
    ):

        message_dechiffre += (
            message_normal[index]
        )

    return message_dechiffre