import csv
import json
import random
from pathlib import Path


# ============================================================
# PATHS
# ============================================================

def get_workfiles_path():
    """
    Ermittelt den WorkFiles-Ordner relativ zum Projekt.

    stolen_data.py liegt unter:
    rooms/lib/stolen_data.py

    WorkFiles liegt unter:
    WorkFiles/
    """

    stolen_data_projet = Path(__file__).resolve().parent.parent.parent
    stolen_data_workfiles = stolen_data_projet / "WorkFiles"

    stolen_data_workfiles.mkdir(
        parents=True,
        exist_ok=True
    )

    return stolen_data_workfiles


def get_challenge_files():
    """
    Liefert die Dateipfade fuer Level 3.
    """

    stolen_data_workfiles = get_workfiles_path()

    stolen_data_csv = stolen_data_workfiles / "stolen_data.csv"
    stolen_data_json = stolen_data_workfiles / "stolen_data.json"

    return stolen_data_csv, stolen_data_json


# ============================================================
# FILE CHECKS
# ============================================================

def file_has_data(stolen_data_files):
    """
    Prueft, ob eine Datei existiert und Daten enthaelt.
    """

    return (
        stolen_data_files.exists()
        and stolen_data_files.is_file()
        and stolen_data_files.stat().st_size > 0
    )


# ============================================================
# RESET
# ============================================================

def reset_challenge():
    """
    Loescht die Dateien von Level 3.

    Beim naechsten Aufruf von create_challenge()
    werden neue Daten erzeugt.
    """

    stolen_data_csv, stolen_data_json = get_challenge_files()

    files_supprime = False

    for stolen_data_files in [
        stolen_data_csv,
        stolen_data_json
    ]:

        if stolen_data_files.exists():
            stolen_data_files.unlink()
            files_supprime = True

    return files_supprime


# ============================================================
# DATA GENERATION
# ============================================================

def create_normal_record(
    identifiant,
    nom
):
    """
    Erzeugt einen plausiblen Datensatz.

    Regeln:

    - access_level: 1 bis 5
    - file_count: 5 bis 100
    - transfer_mb: 10 bis 500
    - status: ACTIVE
    """

    return {
        "id": identifiant,
        "name": nom,
        "access_level": random.randint(1, 5),
        "file_count": random.randint(5, 100),
        "transfer_mb": random.randint(10, 500),
        "status": "ACTIVE"
    }


def manipulate_record(record):
    """
    Manipuliert genau einen Datensatz.

    Der gruene Kobold erzeugt dabei mehrere
    auffaellige Werte.
    """

    record["access_level"] = random.randint(8, 9)

    record["file_count"] = random.randint(
        700,
        1200
    )

    record["transfer_mb"] = random.randint(
        5000,
        10000
    )

    record["status"] = "UNKNOWN"

    return record


def generate_records():
    """
    Erzeugt mehrere normale Datensaetze und
    manipuliert genau einen davon.
    """

    noms = [
        "Anna",
        "Paul",
        "Marie",
        "Peter",
        "Laura",
        "Thomas",
        "Sophie",
        "Daniel"
    ]

    random.shuffle(noms)

    records = []

    identifiant_depart = random.randint(
        100,
        500
    )

    for index in range(6):

        record = create_normal_record(
            identifiant_depart + index,
            noms[index]
        )

        records.append(record)

    # --------------------------------------------------------
    # Genau einen Datensatz manipulieren
    # --------------------------------------------------------

    index_manipule = random.randint(
        0,
        len(records) - 1
    )

    records[index_manipule] = manipulate_record(
        records[index_manipule]
    )

    return records


# ============================================================
# SAVE CSV
# ============================================================

def save_csv(
    stolen_data_csv,
    records
):
    """
    Speichert die Daten als CSV.
    """

    columns = [
        "id",
        "name",
        "access_level",
        "file_count",
        "transfer_mb",
        "status"
    ]

    with open(
        stolen_data_csv,
        "w",
        newline="",
        encoding="utf-8"
    ) as files:

        writer = csv.DictWriter(
            files,
            fieldnames=columns
        )

        writer.writeheader()

        for record in records:
            writer.writerow(record)


# ============================================================
# SAVE JSON
# ============================================================

def save_json(
    stolen_data_json,
    records
):
    """
    Speichert die gleichen Daten als JSON.
    """

    with open(
        stolen_data_json,
        "w",
        encoding="utf-8"
    ) as files:

        json.dump(
            records,
            files,
            indent=4,
            ensure_ascii=False
        )


# ============================================================
# LOAD CSV
# ============================================================

def load_csv(stolen_data_csv):
    """
    Liest die Daten aus der CSV-Datei.
    """

    records = []

    with open(
        stolen_data_csv,
        "r",
        encoding="utf-8"
    ) as files:

        reader = csv.DictReader(files)

        for record in reader:

            records.append({
                "id": int(record["id"]),
                "name": record["name"],
                "access_level": int(
                    record["access_level"]
                ),
                "file_count": int(
                    record["file_count"]
                ),
                "transfer_mb": int(
                    record["transfer_mb"]
                ),
                "status": record["status"]
            })

    return records


# ============================================================
# LOAD JSON
# ============================================================

def load_json(stolen_data_json):
    """
    Liest die JSON-Datei.
    """

    with open(
        stolen_data_json,
        "r",
        encoding="utf-8"
    ) as files:

        return json.load(files)


# ============================================================
# CREATE / LOAD CHALLENGE
# ============================================================

def create_challenge():
    """
    Hauptfunktion fuer Level 3.

    Wenn CSV und JSON bereits existieren und Daten
    enthalten, werden die vorhandenen Daten verwendet.

    Andernfalls werden neue Datensaetze erzeugt
    und beide Dateien geschrieben.
    """

    stolen_data_csv, stolen_data_json = get_challenge_files()

    # --------------------------------------------------------
    # Bereits vorhandene Daten verwenden
    # --------------------------------------------------------

    if (
        file_has_data(stolen_data_csv)
        and file_has_data(stolen_data_json)
    ):

        records = load_csv(
            stolen_data_csv
        )

        if len(records) > 0:

            return {
                "records": records,
                "csv_file": str(stolen_data_csv),
                "json_file": str(stolen_data_json)
            }

    # --------------------------------------------------------
    # Neue Daten generieren
    # --------------------------------------------------------

    records = generate_records()

    save_csv(
        stolen_data_csv,
        records
    )

    save_json(
        stolen_data_json,
        records
    )

    return {
        "records": records,
        "csv_file": str(stolen_data_csv),
        "json_file": str(stolen_data_json)
    }


# ============================================================
# MANIPULATION CHECK
# ============================================================

def is_manipulated(record):
    """
    Prueft, ob ein Datensatz die definierten
    Plausibilitaetsregeln verletzt.
    """

    if record["access_level"] > 5:
        return True

    if record["file_count"] > 100:
        return True

    if record["transfer_mb"] > 500:
        return True

    if record["status"] != "ACTIVE":
        return True

    return False


def find_manipulated_record(records):
    """
    Findet den manipulierten Datensatz.

    Rueckgabe:
        ID des manipulierten Datensatzes
    """

    for record in records:

        if is_manipulated(record):
            return record["id"]

    return None


# ============================================================
# REFERENCE SOLUTION
# ============================================================

def verify_solution(data):
    """
    Referenzloesung fuer das Escape-Room-Framework.
    """

    records = data["records"]

    return find_manipulated_record(
        records
    )