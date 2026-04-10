import pandas as pd
import argparse
import importlib
import time
from core.mailer import send_email


def load_campaign_engine(campaign_name):
    try:
        module_path = f"campaigns.{campaign_name}.engine"
        module = importlib.import_module(module_path)
        return module.generate_email
    except Exception as e:
        print(f"❌ Campaign '{campaign_name}' not found: {e}")
        exit()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--campaign", required=True, help="Campaign name (seo, social_media)")

    args = parser.parse_args()
    campaign_name = args.campaign

    generate_email = load_campaign_engine(campaign_name)

    data = pd.read_csv("data/input.csv")

    for _, row in data.iterrows():
        row_data = row.to_dict()

        subject, body = generate_email(row_data)

        send_email(row_data["email"], subject, body)

        time.sleep(10)  # prevent spam blocking

    print("✅ Campaign Completed!")


if __name__ == "__main__":
    main()