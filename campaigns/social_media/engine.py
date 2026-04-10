import os
import random
from core.template_engine import load_templates, get_random_template, render_template

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")


def generate_email(data):
    templates = load_templates(TEMPLATE_PATH)
    template_str = get_random_template(templates)

    subject_options = [
        f"Grow your brand on social media 📱",
        f"{data['company']} social media strategy",
        f"Content ideas for {data['company']}"
    ]

    subject = random.choice(subject_options)
    body = render_template(template_str, data)

    return subject, body