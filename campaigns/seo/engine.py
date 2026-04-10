import os
import random
from core.template_engine import load_templates, get_random_template, render_template

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")


def generate_email(data):
    service = data.get('service', 'business')  # fallback

    subject = f"Boost your {service} 🚀"

    body = render_template(
        get_random_template(load_templates("campaigns/seo/templates")),
        data
    )

    return subject, body