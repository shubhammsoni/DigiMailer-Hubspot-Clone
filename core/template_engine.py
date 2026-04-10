import os
import random
from jinja2 import Template


def load_templates(template_folder):
    templates = []

    for file in os.listdir(template_folder):
        if file.endswith(".html"):
            with open(os.path.join(template_folder, file), "r") as f:
                templates.append(f.read())

    return templates


def get_random_template(templates):
    return random.choice(templates)


def render_template(template_str, data):
    template = Template(template_str)
    return template.render(**data)