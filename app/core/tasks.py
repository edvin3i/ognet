from datetime import date
from sqlalchemy.orm import Session
from app.crud.extinguisher import get_extinguishers
from app.core.config import settings
import smtplib
from email.mime.text import MIMEText


def send_email(subject: str, message: str):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = settings.EMAIL_FROM
    msg['To'] = settings.EMAIL_TO

    with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        server.send_message(msg)

def check_extinguishers(db: Session):
    extinguishers = get_extinguishers(db)
    for ext in extinguishers:
        if ext.next_check_date <= date.today():
            send_email(
                subject="Проверка огнетушителя",
                message=f"Пожалуйста, проверьте огнетушитель с номером {ext.serial_number}."
            )
