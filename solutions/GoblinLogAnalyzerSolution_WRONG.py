def run(data):

    echecs = {}

    for evenement in data:

        parties = evenement.split()

        # Ungueltige bzw. andere Events ignorieren

        if len(parties) != 4:
            continue

        type_evenement = parties[1]

        if type_evenement != "LOGIN":
            continue

        adresse_ip = parties[2]
        stati = parties[3]

        # Nur fehlgeschlagene Logins berücksichtigen

        if stati == "FAILED":

            if adresse_ip not in echecs:
                echecs[adresse_ip] = 0

            echecs[adresse_ip] += 1

    # Verdaechtige IP suchen

    for adresse_ip, nombre_echecs in echecs.items():

        if nombre_echecs in [1,2]:
            return adresse_ip

    return None