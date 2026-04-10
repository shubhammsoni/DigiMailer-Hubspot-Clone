from datetime import datetime


def log_email(email, status):
    with open("logs/campaign_log.txt", "a") as f:
        f.write(f"{datetime.now()} | {email} | {status}\n")