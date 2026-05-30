from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(filename, title, content):
    pdf = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    elements = [
        Paragraph(title, styles["Title"]),
        Paragraph(content, styles["BodyText"])
    ]

    pdf.build(elements)


create_pdf(
    "sample1.pdf",
    "ABC Corporation RFP",
    "We need a login system and dashboard."
)

create_pdf(
    "sample2.pdf",
    "Healthcare RFP",
    "The application should manage patients and appointments."
)

create_pdf(
    "sample3.pdf",
    "Ecommerce RFP",
    "The platform should support payments and inventory."
)

print("PDFs created successfully!")