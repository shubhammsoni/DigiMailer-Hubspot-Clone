import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config.settings import (
    EMAIL_HOST,
    EMAIL_PORT,
    EMAIL_ADDRESS,
    EMAIL_PASSWORD
)


def send_email(to_email, subject, body):
    try:
        # Create message
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        msg["Subject"] = subject

        # Attach HTML body
        msg.attach(MIMEText(body, "html"))

        # Connect to SMTP server
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()

            # Login using App Password
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            # Send email
            server.send_message(msg)

        print(f"✅ Sent to {to_email}")

    except Exception as e:
        print(f"❌ Failed for {to_email}: {e}")