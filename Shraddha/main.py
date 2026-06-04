from pdf_parser import extract_text_from_pdf
from pdf_generator import generate_proposal_pdf


# ------------------
# Test PDF Generator
# ------------------

proposal_data = {
    "client_name": "CODE ORBIT Pvt Ltd",

    "requirements":
    """
    Build a modern website with payment integration,
    admin dashboard, analytics and SEO support.
    """,

    "service": "Website Development",

    "price": "₹50,000"
}

pdf_bytes = generate_proposal_pdf(
    proposal_data
)

with open(
    "proposal.pdf",
    "wb"
) as file:
    file.write(pdf_bytes)

print("Proposal PDF Generated")


# ------------------
# Test PDF Parser
# ------------------

text = extract_text_from_pdf(
    "proposal.pdf"
)

print("\nExtracted Text:\n")
print(text)