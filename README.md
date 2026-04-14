# Alarmprojekt – Bewegungserkennung mit Raspberry Pi

## Projektbeschreibung
Dieses Projekt ist ein automatisiertes Überwachungssystem zur Bewegungserkennung.
Eine Kamera erkennt Bewegungen in Echtzeit und sendet bei Auslösung automatisch eine E-Mail mit Zeitstempel und Bild.

## Funktionen
- Live-Kamerabild
- Bewegungserkennung mit OpenCV
- E-Mail Benachrichtigung bei Bewegung
- Bildversand als Anhang
- Cooldown gegen Spam
- Logging von Ereignissen
- Snapshot-Speicherung

## Verwendete Technologien
- Python 3
- OpenCV
- Picamera2
- SMTP (Gmail)
- Raspberry Pi OS (Linux)

## Projektstruktur

alarmprojekt/
├── camera.py        # Kameratest / Livebild
├── config.py        # Konfiguration (Mail, Threshold, etc.)
├── mailer.py        # E-Mail Versand
├── main.py          # Hauptlogik (Bewegung + Mail)
├── motion.py        # Bewegungserkennung
├── logs/
│   └── log.txt      # Ereignislog
├── data/
│   └── snapshots/   # Bilder bei Bewegung
└── README.md

## Start des Projekts

Kamera testen:
python3 camera.py

Hauptprogramm starten:
python3 main.py

## E-Mail Setup
SMTP Server: smtp.gmail.com
Port: 465
Authentifizierung über Gmail App-Passwort

## Hinweise
- Empfindlichkeit (THRESHOLD) ggf. anpassen
- Kamera stabil positionieren
- Zu hohe Sensitivität kann Fehlalarme verursachen

## Testablauf
1. Kamera starten
2. Bewegung auslösen
3. E-Mail Eingang prüfen
4. Logdatei prüfen

## Autor
Timon Pietschmann
Fachinformatiker Anwendungsentwicklung – Abschlussprojekt
