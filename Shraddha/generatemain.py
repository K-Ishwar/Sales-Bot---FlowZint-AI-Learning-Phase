from pdf_generator import generate_proposal_pdf

data = {
    "client_name": "ABC Pvt Ltd",
    "budget": "₹50,000",
    "timeline": "2 weeks"
}

pdf = generate_proposal_pdf(data)

with open("proposal.pdf", "wb") as f:
    f.write(pdf)

print("Proposal PDF created!")