import smtplib
from email.message import EmailMessage
from datetime import datetime
import config

def send_mail(image_path=None):
    msg = EmailMessage()

    # Zeitstempel
    zeit = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    msg["Subject"] = "ALARM"
    msg["From"] = config.SENDER
    msg["To"] = config.RECEIVER

    msg.set_content(f"Bewegung erkannt um {zeit}")

    # SMTP Verbindung zur Mail
    if image_path:
        with open(image_path, "rb") as img:
            msg.add_attachment(
                img.read(),
                maintype="image",
                subtype="jpeg",
                filename="alarm.jpg"
            )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(config.SENDER, config.PASSWORD)
        smtp.send_message(msg)

    print("Mail gesendet:", zeit)