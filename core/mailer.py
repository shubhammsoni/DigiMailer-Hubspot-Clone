import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.settings import EMAIL_CONFIG
from core.logger import log_email


def send_email(to_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_CONFIG["EMAIL"]
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'html'))

        server = smtplib.SMTP(EMAIL_CONFIG["SMTP_SERVER"], EMAIL_CONFIG["SMTP_PORT"])
        server.starttls()
        server.login(EMAIL_CONFIG["EMAIL"], EMAIL_CONFIG["PASSWORD"])

        server.send_message(msg)
        server.quit()

        print(f"✅ Sent to {to_email}")
        log_email(to_email, "SUCCESS")

    except Exception as e:
        print(f"❌ Failed for {to_email}: {e}")
        log_email(to_email, f"FAILED: {e}")