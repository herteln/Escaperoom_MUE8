# Escaperoom_MUE8
Escaperoom: Phyton Testing/Learnings for IT Forensic - Studiengang


# Python Escape Room – MUE8Room_NHP

This repository contains extensions to the Python Escape Room framework
originally provided by Markus M. Berg:

https://github.com/mmberg/pythonescaperoom

The exercises were developed in the context of the course
**"Programmierung II"** of the WINGS degree program **IT-Forensic**.

Three additional challenges were implemented in the room
`MUE8Room_NHP`:

1. Goblin Log Analyzer
2. Encrypted Message
3. Stolen Data File

The three challenges follow a connected storyline involving a green
goblin who attempts to gain unauthorized access to a system, leaves an
encrypted message, and manipulates company data.

---

# Deutsche Beschreibung

## 1. Überblick

Der Raum `MUE8Room_NHP` erweitert das vorhandene Python-Escape-Room-
Framework um drei miteinander verbundene Challenges:

1. **Goblin Log Analyzer**
2. **Encrypted Message**
3. **Stolen Data File**

Die Aufgaben kombinieren verschiedene Themen aus Python und steigern
schrittweise die Anforderungen.

Neben Listen, Schleifen und Bedingungen werden unter anderem
String-Verarbeitung, Slicing, Dictionaries, Funktionen,
Dateioperationen sowie CSV- und JSON-Daten verwendet.

| Challenge | Beschreibung | Python-Schwerpunkte |
|---|---|---|
| Goblin Log Analyzer | Analyse verdächtiger Login-Ereignisse | Listen, Schleifen, Bedingungen, Dictionaries, Strings, TXT-Dateien |
| Encrypted Message | Entschlüsselung einer Nachricht des Kobolds | Strings, Slicing, Indizes, Funktionen, Modulo |
| Stolen Data File | Erkennung eines manipulierten Datensatzes | Dictionaries, Schleifen, Bedingungen, CSV, JSON, Dateihandling |

Die Challenges sind innerhalb von `MUE8Room_NHP` als aufeinanderfolgende
Aufgaben integriert.

---

# 2. Projektstruktur

Die wichtigsten Dateien der Erweiterung befinden sich in folgender
Struktur:

```text
Escaperoom_MUE8/
│
├── rooms/
│   ├── lib/
│   │   ├── goblin_log.py
│   │   ├── encrypted_message.py
│   │   └── stolen_data.py
│   │
│   └── MUE8Room_NHP.py
│
├── solutions/
│   ├── GoblinLogAnalyzerSolution.py
│   ├── EncryptedMessageSolution.py
│   └── StolenDataFileSolution.py
│
└── WorkFiles/
    ├── IP.txt
    ├── Events.txt
    ├── stolen_data.csv
    └── stolen_data.json
```

Die Module unter `rooms/lib` stellen die Daten, Hilfsfunktionen und
Referenzlogik für die jeweiligen Challenges bereit.

Die Dateien unter `solutions` enthalten die Python-Lösungen zu den
Challenges.

Der Ordner `WorkFiles` enthält dynamisch erzeugte Daten, die zwischen
mehreren Ausführungen des Escape Rooms erhalten bleiben können.

---

# 3. Challenge 1 – Goblin Log Analyzer

## 3.1 Story

Der grüne Kobold hat versucht, sich unberechtigt Zugang zum System zu
verschaffen.

Dabei hat er verschiedene Spuren in den System-Logs hinterlassen.

Die Log-Daten enthalten erfolgreiche Login-Versuche, fehlgeschlagene
Login-Versuche und weitere Systemereignisse.

Die Aufgabe besteht darin, die IP-Adresse zu identifizieren, von der
mehrere fehlgeschlagene Login-Versuche ausgeführt wurden.

---

## 3.2 Aufgabenbeschreibung / Task Messages

Der grüne Kobold hat versucht, sich unberechtigt Zugang zum System zu
verschaffen und dabei verschiedene Spuren in den System-Logs
hinterlassen.

Die Log-Daten enthalten unterschiedliche Ereignisse. Darunter befinden
sich erfolgreiche Login-Versuche, fehlgeschlagene Login-Versuche und
weitere Systemereignisse, die für die Suche nach dem Kobold nicht
relevant sind.

Ein Login-Ereignis besitzt beispielsweise folgende Struktur:

```text
10:15 LOGIN 192.168.20.45 FAILED
```

Die einzelnen Bestandteile haben folgende Bedeutung:

```text
10:15           Zeitpunkt des Ereignisses
LOGIN           Typ des Ereignisses
192.168.20.45   IP-Adresse
FAILED          Status des Login-Versuchs
```

Ein erfolgreicher Login kann beispielsweise so aussehen:

```text
10:18 LOGIN 192.168.10.22 SUCCESS
```

Der Kobold hat mehrfach versucht, sich mit derselben IP-Adresse
anzumelden.

### Aufgabe

Analysiere die vorhandenen Log-Ereignisse mit Python.

Finde die IP-Adresse, von der mindestens drei fehlgeschlagene
Login-Versuche (`FAILED`) durchgeführt wurden.

Dabei müssen nur Ereignisse vom Typ `LOGIN` berücksichtigt werden.
Andere Ereignisse können ignoriert werden.

Das Python-Programm soll die verdächtige IP-Adresse zurückgeben.

Beispiel:

```text
192.168.20.45
```

---

## 3.3 Datenbereitstellung

Die Challenge verwendet die beiden Dateien:

```text
WorkFiles/IP.txt
WorkFiles/Events.txt
```

Beim Start der Challenge wird geprüft, ob beide Dateien bereits
existieren und Daten enthalten.

### Vorhandene Dateien

Wenn beide Dateien existieren und Daten enthalten, werden die
vorhandenen Daten verwendet.

Damit bleibt eine einmal erzeugte Challenge über mehrere Starts des
Programms hinweg erhalten.

### Dateien fehlen oder sind leer

Wenn die Dateien nicht vorhanden oder leer sind, werden automatisch
neue IP-Adressen und neue Log-Ereignisse generiert.

Die neu erzeugten Daten werden anschließend in `IP.txt` und
`Events.txt` gespeichert.

---

## 3.4 Dynamische Generierung

Für die Challenge werden mehrere zufällige private IPv4-Adressen
erzeugt.

Mögliche private Adressbereiche sind beispielsweise:

```text
10.x.x.x
172.16.x.x – 172.31.x.x
192.168.x.x
```

Eine IP-Adresse wird zufällig als verdächtige Adresse ausgewählt.

Für diese IP-Adresse werden mindestens drei fehlgeschlagene
Login-Versuche erzeugt.

Andere IP-Adressen können ebenfalls einzelne fehlgeschlagene
Login-Versuche besitzen.

Dadurch reicht es nicht aus, einfach den ersten `FAILED`-Eintrag zu
finden. Die Anzahl der fehlgeschlagenen Login-Versuche muss für jede
IP-Adresse ausgewertet werden.

---

## 3.5 Hinweise / Hints

### Hint 1

Nicht jeder Eintrag ist für die Lösung relevant.

Suche zuerst nach Ereignissen vom Typ:

```text
LOGIN
```

### Hint 2

Ein fehlgeschlagener Login besitzt den Status:

```text
FAILED
```

### Hint 3

Mit `split()` kann ein Log-Eintrag in seine einzelnen Bestandteile
zerlegt werden.

Beispiel:

```text
10:15 LOGIN 192.168.20.45 FAILED
```

wird zu:

```python
["10:15", "LOGIN", "192.168.20.45", "FAILED"]
```

### Hint 4

Eine einzelne IP-Adresse kann mehrfach in den Log-Daten vorkommen.

Zähle deshalb die Anzahl der fehlgeschlagenen Login-Versuche für jede
IP-Adresse.

Ein Dictionary kann dabei hilfreich sein.

### Hint 5

Gesucht wird die IP-Adresse mit mindestens drei `FAILED LOGIN`-
Ereignissen.

---

## 3.6 Lösungslogik

Die Lösung verarbeitet die vorhandenen Log-Ereignisse nacheinander.

Jeder Log-Eintrag wird zunächst in seine Bestandteile zerlegt.

Danach wird geprüft:

- Handelt es sich um ein `LOGIN`-Event?
- Ist der Status `FAILED`?
- Von welcher IP-Adresse stammt das Ereignis?

Ein Dictionary kann verwendet werden, um die Anzahl der
fehlgeschlagenen Login-Versuche pro IP-Adresse zu speichern.

Beispiel:

```python
{
    "192.168.20.45": 3,
    "10.20.15.12": 1
}
```

Anschließend wird nach einer IP-Adresse gesucht, deren Anzahl
fehlgeschlagener Login-Versuche mindestens drei beträgt.

Diese IP-Adresse ist das Ergebnis der Challenge.

---

## 3.7 Reset der Challenge

Die Funktion:

```python
reset_challenge()
```

löscht die gespeicherten Challenge-Daten.

Beim nächsten Aufruf der Challenge werden neue IP-Adressen und neue
Log-Ereignisse generiert.

Der Reset wird nicht automatisch bei jedem Start ausgeführt, damit
bereits erzeugte Daten wiederverwendet werden können.

---

## 3.8 Lernziele

Die Challenge trainiert insbesondere:

- Listen
- `for`-Schleifen
- `if`-Bedingungen
- Dictionaries
- String-Verarbeitung
- `split()`
- Zähler
- Dateioperationen
- dynamische Datengenerierung
- einfache Log-Analyse

---

# 4. Challenge 2 – Encrypted Message

## 4.1 Story

Nachdem die verdächtige IP-Adresse identifiziert wurde, wird eine
weitere Spur des grünen Kobolds entdeckt.

Der Kobold hat eine verschlüsselte Nachricht hinterlassen.

Die verdächtige IP-Adresse aus der vorherigen Challenge ist ein
wichtiger Bestandteil der Verschlüsselung.

Dadurch sind Challenge 1 und Challenge 2 direkt miteinander verbunden.

---

## 4.2 Aufgabenbeschreibung / Task Messages

Die verdächtige IP-Adresse wurde gefunden.

Der grüne Kobold hat jedoch noch eine weitere Spur hinterlassen:
eine verschlüsselte Nachricht.

Die Nachricht wurde nicht mit einer klassischen Caesar-
Verschlüsselung verschlüsselt.

Stattdessen hat der Kobold mehrere Operationen miteinander kombiniert.

Die IP-Adresse aus der vorherigen Challenge ist ein wichtiger
Bestandteil des Verschlüsselungsschlüssels.

### Aufgabe

Entschlüssele die Nachricht des grünen Kobolds.

Dazu müssen die einzelnen Schritte der Verschlüsselung verstanden und
in umgekehrter Reihenfolge rückgängig gemacht werden.

Das Python-Programm soll die vollständig entschlüsselte Nachricht
zurückgeben.

---

## 4.3 Verschlüsselungsverfahren

Die ursprüngliche Nachricht wird in drei Schritten verändert.

### Schritt 1 – Störzeichen einfügen

Zwischen beziehungsweise nach jedem echten Zeichen wird ein
zufälliges Störzeichen eingefügt.

Aus:

```text
DATA
```

könnte beispielsweise werden:

```text
D7AxT4Aq
```

Die ursprünglichen Zeichen befinden sich damit zunächst an jeder
zweiten Position.

---

### Schritt 2 – Zeichenfolge umdrehen

Anschließend wird die gesamte Zeichenfolge umgedreht.

Aus:

```text
D7AxT4Aq
```

wird:

```text
qA4TxA7D
```

---

### Schritt 3 – Zeichenfolge rotieren

Zum Schluss wird die Zeichenfolge um eine bestimmte Anzahl von
Positionen rotiert.

Die Anzahl der Positionen wird aus der verdächtigen IP-Adresse aus
Challenge 1 berechnet.

Bei der IP-Adresse:

```text
10.10.8.23
```

werden zunächst die vier Zahlenblöcke addiert:

```text
10 + 10 + 8 + 23 = 51
```

Anschließend wird aus der Summe und der Länge der Nachricht mit dem
Modulo-Operator `%` die tatsächliche Rotationsposition berechnet.

Beispielsweise:

```python
rotation = 51 % len(message)
```

Dadurch hängt die Verschlüsselung von der in der vorherigen Challenge
ermittelten IP-Adresse ab.

---

## 4.4 Entschlüsselung

Um die ursprüngliche Nachricht wiederherzustellen, müssen die Schritte
der Verschlüsselung in umgekehrter Reihenfolge ausgeführt werden:

```text
Verschlüsselte Nachricht
        |
        v
Rotation rückgängig machen
        |
        v
String umdrehen
        |
        v
Störzeichen entfernen
        |
        v
Originalnachricht
```

Nach dem Rückgängigmachen der Rotation wird der String wieder
umgedreht.

Anschließend befinden sich die echten Zeichen wieder an jeder zweiten
Position.

Diese können beispielsweise mit Slicing extrahiert werden:

```python
message[::2]
```

---

## 4.5 Hinweise / Hints

### Hint 1

Die IP-Adresse aus der vorherigen Challenge ist auch für dieses Level
wichtig.

### Hint 2

Teile die IP-Adresse an den Punkten und addiere die vier Zahlenblöcke.

Beispiel:

```text
10.10.8.23
```

ergibt:

```text
10 + 10 + 8 + 23 = 51
```

### Hint 3

Der Modulo-Operator `%` kann verwendet werden, um aus der Summe der
IP-Adresse und der Länge der Nachricht die Rotationsposition zu
bestimmen.

### Hint 4

Der Kobold hat zuerst echte Zeichen mit zufälligen Störzeichen
vermischt und anschließend die Reihenfolge verändert.

Beim Entschlüsseln müssen diese Schritte in umgekehrter Reihenfolge
durchgeführt werden.

### Hint 5

Nachdem Rotation und Umkehrung rückgängig gemacht wurden, befindet
sich die ursprüngliche Nachricht an jeder zweiten Position.

Slicing kann dabei hilfreich sein:

```python
message[::2]
```

---

## 4.6 Lösungslogik

Die Lösung führt folgende Schritte durch:

1. Die IP-Adresse wird mit `split(".")` in ihre vier Zahlenblöcke
   zerlegt.
2. Die vier Zahlen werden in Integer-Werte umgewandelt und addiert.
3. Mit `%` und der Länge der Nachricht wird die Rotation berechnet.
4. Die Rotation wird rückgängig gemacht.
5. Die Zeichenfolge wird umgedreht.
6. Jedes zweite Zeichen wird extrahiert.
7. Die entschlüsselte Nachricht wird zurückgegeben.

Die Challenge kombiniert damit mehrere einfache Python-Techniken zu
einem mehrstufigen Algorithmus.

---

## 4.7 Lernziele

Die Challenge trainiert insbesondere:

- Strings
- Slicing
- Indizes
- Listen
- Schleifen
- Funktionen
- `split()`
- Integer-Konvertierung
- Modulo `%`
- String-Rotation
- algorithmisches Denken
- Verarbeitung des Ergebnisses einer vorherigen Challenge

---

# 5. Challenge 3 – Stolen Data File

## 5.1 Story

Die entschlüsselte Nachricht führt zu einem weiteren Hinweis.

Der grüne Kobold hat nicht nur versucht, auf das System zuzugreifen,
sondern außerdem Unternehmensdaten manipuliert.

Mehrere Datensätze wurden gefunden.

Die meisten Datensätze enthalten normale und plausible Werte.
Mindestens ein Datensatz enthält jedoch auffällige Werte und wurde vom
Kobold manipuliert.

---

## 5.2 Aufgabenbeschreibung / Task Messages

Die Unternehmensdaten bestehen aus mehreren strukturierten
Datensätzen.

Jeder Datensatz besitzt folgende Felder:

```text
id
name
access_level
file_count
transfer_mb
status
```

Ein normaler Datensatz könnte beispielsweise folgendermaßen aussehen:

```text
ID: 317
Name: Anna
Access Level: 2
File Count: 34
Transfer MB: 145
Status: ACTIVE
```

### Aufgabe

Analysiere die Datensätze mit Python und finde den Datensatz, der vom
grünen Kobold manipuliert wurde.

Prüfe dafür die einzelnen Werte jedes Datensatzes gegen die
vorgegebenen Plausibilitätsregeln.

Das Python-Programm soll die `id` des manipulierten Datensatzes
zurückgeben.

Beispiel:

```text
320
```

---

## 5.3 Plausibilitätsregeln

Für normale Datensätze gelten folgende Regeln:

```text
access_level <= 5
file_count <= 100
transfer_mb <= 500
status = ACTIVE
```

Ein manipulierter Datensatz verletzt eine oder mehrere dieser Regeln.

Ein auffälliger Datensatz könnte beispielsweise so aussehen:

```text
ID: 320
Name: Sophie
Access Level: 9
File Count: 892
Transfer MB: 7342
Status: UNKNOWN
```

Dieser Datensatz ist auffällig, da mehrere Werte außerhalb der
erlaubten Bereiche liegen.

---

## 5.4 CSV- und JSON-Dateien

Die Challenge verwendet zwei Dateien:

```text
WorkFiles/stolen_data.csv
WorkFiles/stolen_data.json
```

Die CSV-Datei kann beispielsweise folgende Struktur besitzen:

```csv
id,name,access_level,file_count,transfer_mb,status
317,Anna,2,34,145,ACTIVE
318,Peter,4,77,342,ACTIVE
319,Marie,1,28,92,ACTIVE
320,Sophie,9,892,7342,UNKNOWN
321,Paul,3,54,276,ACTIVE
```

Die Daten werden zusätzlich als JSON gespeichert.

Beispiel:

```json
[
    {
        "id": 317,
        "name": "Anna",
        "access_level": 2,
        "file_count": 34,
        "transfer_mb": 145,
        "status": "ACTIVE"
    }
]
```

Die eigentliche Aufgabe besteht nicht in einer einfachen
CSV-zu-JSON-Konvertierung, sondern in der Analyse der strukturierten
Daten und der Identifikation eines manipulierten Datensatzes.

---

## 5.5 Dynamische Generierung

Wenn die Challenge-Dateien bereits existieren und Daten enthalten,
werden die vorhandenen Daten wiederverwendet.

Wenn die benötigten Dateien fehlen oder leer sind, werden neue
Datensätze erzeugt.

Dabei werden mehrere normale Datensätze und ein manipulierter Datensatz
generiert.

Die Position und die konkreten Werte des manipulierten Datensatzes
können sich daher nach einem Reset ändern.

---

## 5.6 Hinweise / Hints

### Hint 1

Nicht der Name eines Datensatzes entscheidet darüber, ob er manipuliert
wurde.

Vergleiche die Werte mit den vorgegebenen Plausibilitätsregeln.

### Hint 2

Ein normaler `access_level` liegt zwischen 1 und 5.

Ein Wert größer als 5 ist verdächtig.

### Hint 3

Ein normaler Benutzer besitzt maximal 100 Dateien:

```text
file_count <= 100
```

und transferiert maximal 500 MB:

```text
transfer_mb <= 500
```

### Hint 4

Der Status eines normalen Datensatzes lautet:

```text
ACTIVE
```

Ein anderer Status ist auffällig.

### Hint 5

Gehe mit einer Schleife durch die Datensätze und prüfe für jeden
Datensatz die einzelnen Bedingungen.

Sobald ein manipulierter Datensatz gefunden wurde, gib dessen `id`
zurück.

---

## 5.7 Lösungslogik

Die Datensätze werden nacheinander analysiert.

Für jeden Datensatz werden die einzelnen Werte überprüft.

Beispielsweise:

```python
if record["access_level"] > 5:
    # manipuliert

if record["file_count"] > 100:
    # manipuliert

if record["transfer_mb"] > 500:
    # manipuliert

if record["status"] != "ACTIVE":
    # manipuliert
```

Sobald ein Datensatz mindestens eine Plausibilitätsregel verletzt,
kann er als manipuliert erkannt werden.

Als Ergebnis wird dessen `id` zurückgegeben.

---

## 5.8 Reset der Challenge

Mit:

```python
reset_challenge()
```

können die gespeicherten Daten der Challenge gelöscht werden.

Beim nächsten Start werden neue Datensätze erzeugt und erneut in den
WorkFiles gespeichert.

---

## 5.9 Lernziele

Die Challenge trainiert insbesondere:

- Listen
- Dictionaries
- Schleifen
- Bedingungen
- strukturierte Daten
- CSV-Dateien
- JSON-Dateien
- Dateioperationen
- Plausibilitätsprüfung
- Datenqualität
- algorithmische Validierung

---

# 6. Zusammenhang der drei Challenges

Die drei Challenges bilden eine zusammenhängende Geschichte:

```text
Goblin Log Analyzer
        |
        | verdächtige IP-Adresse
        v
Encrypted Message
        |
        | entschlüsselte Nachricht
        v
Stolen Data File
        |
        | manipulierter Datensatz
        v
Challenge completed
```

In der ersten Challenge werden die Spuren des unerlaubten
Login-Versuchs untersucht.

Die dabei gefundene verdächtige IP-Adresse wird in der zweiten
Challenge für die Entschlüsselung der Nachricht verwendet.

Die entschlüsselte Nachricht führt zur dritten Challenge, in der
manipulierte Unternehmensdaten identifiziert werden müssen.

Dadurch entstehen drei miteinander verbundene Aufgaben statt drei
vollständig unabhängiger Python-Übungen.

---

# English Description

## 1. Overview

The room `MUE8Room_NHP` extends the existing Python Escape Room
framework with three connected challenges:

1. **Goblin Log Analyzer**
2. **Encrypted Message**
3. **Stolen Data File**

The challenges follow a common storyline involving a green goblin who
attempts to gain unauthorized access to a system, leaves an encrypted
message, and manipulates company data.

The challenges gradually introduce and combine Python concepts such as
lists, loops, conditions, dictionaries, string processing, slicing,
functions, and file handling.

| Challenge | Description | Main Python Concepts |
|---|---|---|
| Goblin Log Analyzer | Identify suspicious login activity | Lists, loops, conditions, dictionaries, strings, TXT files |
| Encrypted Message | Decrypt the goblin's message | Strings, slicing, indexes, functions, modulo |
| Stolen Data File | Identify manipulated data | Dictionaries, loops, conditions, CSV, JSON, file handling |

---

# 2. Project Structure

The main files added for the three challenges are:

```text
Escaperoom_MUE8/
│
├── rooms/
│   ├── lib/
│   │   ├── goblin_log.py
│   │   ├── encrypted_message.py
│   │   └── stolen_data.py
│   │
│   └── MUE8Room_NHP.py
│
├── solutions/
│   ├── GoblinLogAnalyzerSolution.py
│   ├── EncryptedMessageSolution.py
│   └── StolenDataFileSolution.py
│
└── WorkFiles/
    ├── IP.txt
    ├── Events.txt
    ├── stolen_data.csv
    └── stolen_data.json
```

The modules under `rooms/lib` provide the challenge data, helper
functions, and reference logic required by the Escape Room framework.

The files under `solutions` contain the Python solutions for the
individual challenges.

The `WorkFiles` directory stores dynamically generated challenge data
that can be reused between executions.

---

# 3. Challenge 1 – Goblin Log Analyzer

## 3.1 Story

The green goblin has attempted to gain unauthorized access to the
system and has left several traces in the system logs.

The logs contain successful login attempts, failed login attempts, and
other system events.

The goal is to identify the IP address responsible for multiple failed
login attempts.

---

## 3.2 Task Description / Task Messages

A login event may look like this:

```text
10:15 LOGIN 192.168.20.45 FAILED
```

The individual elements represent:

```text
10:15           Time of the event
LOGIN           Event type
192.168.20.45   IP address
FAILED          Login status
```

A successful login may look like:

```text
10:18 LOGIN 192.168.10.22 SUCCESS
```

The goblin attempted to log in several times using the same IP address.

### Your Task

Analyze the available log events using Python.

Find the IP address that generated at least three failed (`FAILED`)
login attempts.

Only events of type `LOGIN` need to be considered. Other events can be
ignored.

Your Python program must return the suspicious IP address.

Example:

```text
192.168.20.45
```

---

## 3.3 Data Handling

The challenge uses:

```text
WorkFiles/IP.txt
WorkFiles/Events.txt
```

If both files already exist and contain data, the existing values are
loaded and reused.

If the files are missing or empty, new IP addresses and log events are
generated automatically and stored in the two files.

This means that a generated challenge remains unchanged between
application restarts until it is reset.

---

## 3.4 Dynamic Generation

Several private IPv4 addresses are generated dynamically.

One address is randomly selected as the suspicious address and receives
at least three `FAILED` login events.

Other IP addresses may also have individual failed login attempts.

The solution therefore has to count the number of failed login attempts
for each IP address instead of simply selecting the first failed event.

---

## 3.5 Hints

### Hint 1

Not every event is relevant.

Start by looking for events of type:

```text
LOGIN
```

### Hint 2

A failed login has the status:

```text
FAILED
```

### Hint 3

You can use `split()` to separate a log entry into its individual
elements.

For example:

```text
10:15 LOGIN 192.168.20.45 FAILED
```

becomes:

```python
["10:15", "LOGIN", "192.168.20.45", "FAILED"]
```

### Hint 4

The same IP address may occur several times.

Count the number of failed login attempts for each IP address.

A dictionary may be useful for this.

### Hint 5

You are looking for the IP address with at least three `FAILED LOGIN`
events.

---

## 3.6 Solution Logic

Each log event is processed individually.

The program checks:

- whether the event is a `LOGIN`,
- whether its status is `FAILED`,
- and which IP address generated the event.

A dictionary can be used to count failed login attempts per IP address.

For example:

```python
{
    "192.168.20.45": 3,
    "10.20.15.12": 1
}
```

The IP address with at least three failed login attempts is returned as
the result.

---

## 3.7 Reset

The function:

```python
reset_challenge()
```

removes the stored challenge data.

The next execution generates new IP addresses and new log events.

---

## 3.8 Learning Objectives

This challenge practices:

- lists
- `for` loops
- `if` conditions
- dictionaries
- string processing
- `split()`
- counters
- file handling
- dynamic data generation
- basic log analysis

---

# 4. Challenge 2 – Encrypted Message

## 4.1 Story

After identifying the suspicious login activity, another clue is
discovered.

The green goblin has left an encrypted message.

The suspicious IP address identified in the previous challenge becomes
part of the encryption mechanism, directly connecting Challenge 1 and
Challenge 2.

---

## 4.2 Task Description / Task Messages

The message was not encrypted using a standard Caesar cipher.

Instead, the goblin combined several operations.

The suspicious IP address from the previous challenge is an important
part of the encryption key.

### Your Task

Decrypt the green goblin's message.

To recover the original message, understand the individual encryption
steps and reverse them in the opposite order.

Your Python program must return the completely decrypted message.

---

## 4.3 Encryption Method

The original message is modified in three steps.

### Step 1 – Insert Noise Characters

A random noise character is inserted after every real character.

For example:

```text
DATA
```

could become:

```text
D7AxT4Aq
```

The original characters are therefore located at every second position.

---

### Step 2 – Reverse the String

The complete string is then reversed.

For example:

```text
D7AxT4Aq
```

becomes:

```text
qA4TxA7D
```

---

### Step 3 – Rotate the String

Finally, the resulting string is rotated.

The number of positions is calculated from the suspicious IP address
found in the previous challenge.

For example:

```text
10.10.8.23
```

results in:

```text
10 + 10 + 8 + 23 = 51
```

The modulo operator `%` is then used together with the length of the
message to calculate the actual rotation:

```python
rotation = 51 % len(message)
```

---

## 4.4 Decryption

The encryption operations must be reversed in the opposite order:

```text
Encrypted Message
        |
        v
Reverse the rotation
        |
        v
Reverse the string
        |
        v
Remove the noise characters
        |
        v
Original Message
```

After reversing the rotation and reversing the string, the original
characters are once again located at every second position.

Python slicing can then be used:

```python
message[::2]
```

---

## 4.5 Hints

### Hint 1

The IP address from the previous challenge is also important for this
challenge.

### Hint 2

Split the IP address at the dots and add its four numeric blocks.

For example:

```text
10.10.8.23
```

results in:

```text
10 + 10 + 8 + 23 = 51
```

### Hint 3

The modulo operator `%` can be used with the sum of the IP address and
the length of the message to determine the rotation.

### Hint 4

The goblin first mixed the real characters with random noise characters
and then changed their order.

When decrypting the message, these operations have to be reversed in
the opposite order.

### Hint 5

After reversing the rotation and reversing the string, the original
message can be found at every second position.

Python slicing may be useful:

```python
message[::2]
```

---

## 4.6 Solution Logic

The solution performs the following steps:

1. Split the IP address into its four numeric blocks.
2. Convert the blocks into integers.
3. Add the four values.
4. Calculate the rotation using modulo `%`.
5. Reverse the rotation.
6. Reverse the string.
7. Extract every second character.
8. Return the decrypted message.

This challenge combines several basic Python techniques into a
multi-step algorithm.

---

## 4.7 Learning Objectives

This challenge practices:

- strings
- slicing
- indexes
- loops
- functions
- `split()`
- integer conversion
- modulo `%`
- string rotation
- algorithmic thinking
- using the result of a previous challenge

---

# 5. Challenge 3 – Stolen Data File

## 5.1 Story

The decrypted message reveals another clue.

The green goblin did more than attempt to access the system.

The goblin has also manipulated company data.

Several records have been recovered. Most records contain normal and
plausible values, but at least one record contains suspicious values.

---

## 5.2 Task Description / Task Messages

Each record contains the following fields:

```text
id
name
access_level
file_count
transfer_mb
status
```

A normal record may look like:

```text
ID: 317
Name: Anna
Access Level: 2
File Count: 34
Transfer MB: 145
Status: ACTIVE
```

### Your Task

Analyze the records using Python and identify the record manipulated by
the green goblin.

Check the individual values of each record against the defined
plausibility rules.

Your Python program must return the `id` of the manipulated record.

Example:

```text
320
```

---

## 5.3 Plausibility Rules

Normal records follow these rules:

```text
access_level <= 5
file_count <= 100
transfer_mb <= 500
status = ACTIVE
```

A manipulated record violates one or more of these rules.

For example:

```text
ID: 320
Name: Sophie
Access Level: 9
File Count: 892
Transfer MB: 7342
Status: UNKNOWN
```

This record is suspicious because several values are outside the
expected ranges.

---

## 5.4 CSV and JSON Files

The challenge uses:

```text
WorkFiles/stolen_data.csv
WorkFiles/stolen_data.json
```

The CSV file may contain data such as:

```csv
id,name,access_level,file_count,transfer_mb,status
317,Anna,2,34,145,ACTIVE
318,Peter,4,77,342,ACTIVE
319,Marie,1,28,92,ACTIVE
320,Sophie,9,892,7342,UNKNOWN
321,Paul,3,54,276,ACTIVE
```

The same structured data is also stored as JSON.

The main objective is not a simple CSV-to-JSON conversion.

Instead, the challenge requires the player to analyze structured data
and detect manipulated information based on defined rules.

---

## 5.5 Dynamic Generation

If the challenge files already exist and contain data, the existing
data is reused.

If the required files are missing or empty, new records are generated
automatically.

The generated data contains several valid records and one manipulated
record.

The position and values of the manipulated record can therefore change
after the challenge has been reset.

---

## 5.6 Hints

### Hint 1

The name of a record does not determine whether it has been manipulated.

Compare its values with the defined plausibility rules.

### Hint 2

A normal `access_level` is between 1 and 5.

A value greater than 5 is suspicious.

### Hint 3

A normal user has no more than 100 files:

```text
file_count <= 100
```

and transfers no more than 500 MB:

```text
transfer_mb <= 500
```

### Hint 4

The status of a normal record is:

```text
ACTIVE
```

Any other status is suspicious.

### Hint 5

Loop through the records and check the individual conditions for each
record.

As soon as you identify the manipulated record, return its `id`.

---

## 5.7 Solution Logic

The records are processed one after another.

For each record, the defined rules are checked.

For example:

```python
if record["access_level"] > 5:
    # manipulated

if record["file_count"] > 100:
    # manipulated

if record["transfer_mb"] > 500:
    # manipulated

if record["status"] != "ACTIVE":
    # manipulated
```

When a record violates one or more plausibility rules, it can be
identified as manipulated.

Its `id` is returned as the result.

---

## 5.8 Reset

The function:

```python
reset_challenge()
```

removes the stored challenge data.

New records are generated and stored in the WorkFiles the next time the
challenge is executed.

---

## 5.9 Learning Objectives

This challenge practices:

- lists
- dictionaries
- loops
- conditions
- structured data
- CSV processing
- JSON processing
- file handling
- data-quality validation
- plausibility checks
- algorithmic validation

---

# 6. Challenge Flow

The three challenges form one connected Escape Room scenario:

```text
Goblin Log Analyzer
        |
        | suspicious IP address
        v
Encrypted Message
        |
        | decrypted message
        v
Stolen Data File
        |
        | manipulated record
        v
Challenge completed
```

The first challenge investigates traces of unauthorized login attempts.

The suspicious IP address identified in the first challenge is used in
the second challenge as part of the decryption mechanism.

The decrypted message leads to the third challenge, where manipulated
company data must be identified.

This creates a connected Escape Room scenario rather than three
independent Python exercises.

---

# Credits

The original Python Escape Room framework was provided by:

**Markus M. Berg**

https://github.com/mmberg/pythonescaperoom

The additional challenges:

- Goblin Log Analyzer
- Encrypted Message
- Stolen Data File

were added to `MUE8Room_NHP` in the context of the course
**Programmierung II**, WINGS, degree program **IT-Forensic**.