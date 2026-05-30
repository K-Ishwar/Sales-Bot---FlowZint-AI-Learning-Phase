from extract_pdf import extract_text_from_pdf

pdf_files = [
    "sample1.pdf",
    "sample2.pdf",
    "sample3.pdf"
]

for pdf_file in pdf_files:

    print("\n" + "=" * 50)
    print(f"Testing {pdf_file}")
    print("=" * 50)

    with open(pdf_file, "rb") as f:
        pdf_bytes = f.read()

    extracted_text = extract_text_from_pdf(pdf_bytes)

    print(extracted_text)