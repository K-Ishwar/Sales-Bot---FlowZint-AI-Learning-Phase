from pathlib import Path

from jinja2 import Template
from weasyprint import HTML


def generate_proposal_pdf(data):

    template_path = (
        Path(__file__).parent /
        "proposal_template.html"
    )

    with open(template_path, "r", encoding="utf-8") as file:
        html_template = file.read()

    template = Template(html_template)

    rendered_html = template.render(
        client_name=data["client_name"],
        requirements=data["requirements"],
        service=data["service"],
        price=data["price"]
    )

    pdf_bytes = HTML(
        string=rendered_html
    ).write_pdf()

    return pdf_bytes