import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.config import settings


def send_email(to_email: str, subject: str, body: str):
    try:
        message = MIMEMultipart()

        message["From"] = settings.MAIL_FROM
        message["To"] = to_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(
            settings.MAIL_SERVER,
            settings.MAIL_PORT
        )

        server.starttls()

        server.login(
            settings.MAIL_USERNAME,
            settings.MAIL_PASSWORD
        )

        server.sendmail(
            settings.MAIL_FROM,
            to_email,
            message.as_string()
        )

        server.quit()

        return True

    except Exception as e:
        print("Email Error:", e)
        return False