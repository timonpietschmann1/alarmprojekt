# Bewegungs- und Alarmsystem (Raspberry Pi)

## Projektbeschreibung
Ein defektes Überwachungssystem wurde durch eine kostengünstige, individuell anpassbare Lösung ersetzt.  
Das System erkennt Bewegungen und sendet automatisch eine E-Mail mit Zeitstempel und Bild.

---

## Inhaltsverzeichnis
- Ablaufplan
- Hardware
- Installation
- Ordnerstruktur
- Tests
- Hauptfunktionen

---

## Ablaufplan
Das System startet und nimmt drei Bilder nacheinander auf.  
Zwischen den Aufnahmen gibt es kurze Wartezeiten.

- Frame 1 und Frame 2 werden zur Bewegungserkennung verglichen  
- Keine Änderung → Ablauf startet erneut  
- Bewegung erkannt → Cooldown wird geprüft  
- Cooldown aktiv → keine Aktion  
- Kein Cooldown →  
  - Frame 3 wird gespeichert  
  - E-Mail wird versendet (Bild + Zeitstempel)  
  - Log wird geschrieben  

Danach startet der Ablauf erneut.  

**Beenden:** `STRG + C`

---

## Benötigte Hardware
- Raspberry Pi 3  
- Netzteil  
- CSI Kamera  
- Monitor  
- Tastatur und Maus  
- SD-Karte  
- HDMI-Kabel  

---

## Software Installation
- Raspberry Pi OS  
- Python 3  
- OpenCV (Python)  
- Thonny  
- Git (optional)  

---

## Ordnerstruktur
```bash
alarmprojekt/
├── main.py
├── motion.py
├── mailer.py
├── config.py
├── camera.py
├── mail_test.py
├── README.md
├── logs/
│   └── log.txt
└── data/
    └── snapshots/
