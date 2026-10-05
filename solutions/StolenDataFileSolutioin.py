def run(data):


    records = data["records"]

    for record in records:

        ids = record["id"]

        niveau_acces = record["access_level"]

        file_count = record["file_count"]

        tranferred = record["transfer_mb"]

        stati = record["status"]

        # ----------------------------------------------------
        # Plausibilitaetspruefung
        # ----------------------------------------------------

        manipulation = False

        if niveau_acces > 5:
            manipulation = True

        if file_count > 100:
            manipulation = True

        if tranferred > 500:
            manipulation = True

        if stati != "ACTIVE":
            manipulation = True

        # ----------------------------------------------------
        # Manipulierter Datensatz gefunden
        # ----------------------------------------------------

        if manipulation:
            return ids

    return None