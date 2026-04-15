**#Bewegungs- und Alarmsystem (Raspberry Pi)**

**#Projektbeschreibung**
- Ein defektes Überwachungssystem wurde durch eine kostengünstige, individuell anpassbare Lösung ersetzt
- Das System erkennt Bewegungen und sendet automatisch eine E-Mail mit Zeitstempel und Bild


**#Inhaltsverzeichnis**
- Ablaufplan
- Hardware
- Installation
- Ordnerstruktur
- Tests
- Hauptfunktionen


**#Ablaufplan**
- Das System startet und nimmt drei Bilder nacheinander auf. Zwischen den Aufnahmen gibt es kurze Wartezeiten. Die ersten beiden Bilder (Frame 1 und Frame 2) werden zur Bewegungserkennung miteinander verglichen.
- Wenn keine signifikante Änderung erkannt wird, wird der Ablauf wiederholt und erneut mit neuen Frames gestartet.
- Wenn eine Bewegung erkannt wird, wird geprüft ob ein Cooldown aktiv ist. Falls ja, wird keine Aktion ausgeführt und das System startet erneut.
- Wenn kein Cooldown aktiv ist, wird das dritte Bild (Frame 3) als Ereignisbild gespeichert und anschließend per E-Mail versendet. Die Mail enthält das Bild, einen Zeitstempel und einen kurzen Text. Danach wird ein lokales Log geschrieben.
- Anschließend startet der Ablauf erneut.
- Beenden des Programms erfolgt über STRG + C.


**#Benötigte Hardware**
- Raspberry Pi 3
- Netzteil
- CSI Kamera
- Monitor
- Tastatur und Maus
- SD-Karte
- HDMI Kabel


**#Software Installation**
- Raspberry Pi OS
- Python 3
- OpenCV für Python
- Thonny
- Git (optional für Entwicklung)


**#Ordnerstruktur**
alarmprojekt/
├── main.py
├── motion.py
├── mailer.py
├── config.py
├── camera.py
├── mail_test.py
├── README.md
├── logs/
│ └── log.txt
├── data/
│ └── snapshots


**#Testdateien**
- camera.py → Test der Kamera
- mail_test.py → Test des E-Mail Versands


**#Hauptfunktionen**
- main.py → Steuerung des gesamten Programms
- motion.py → Bewegungserkennung über Framevergleich
- mailer.py → E-Mail Versand mit Bild und Zeitstempel
- config.py → Konfiguration (z. B. Maildaten, Schwellenwerte)


**#Testen**
- Programm starten:
- python3 main.py
- Bewegung vor Kamera auslösen
- E-Mail Eingang prüfen
- Beenden mit STRG + C


**#Autor**
Timon Pietschmann
