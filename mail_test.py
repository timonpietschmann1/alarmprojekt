import smtplib
from email.message import EmailMessage
import config

msg = EmailMessage()
msg["Subject"] = "Test Mail"
msg["From"] = config.SENDER
msg["To"] = config.RECEIVER
msg.set_content("SMTP Test erfolgreich")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(config.SENDER, config.PASSWORD)
    smtp.send_message(msg)

    print("Mail gesendet")
