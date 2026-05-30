import io
import pdfplumber


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    try:
        all_text = []

        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:

            for page in pdf.pages:

                text = page.extract_text()

                if text:
                    text = text.replace("\xa0", " ")
                    text = text.strip()

                    all_text.append(text)

        return "\n".join(all_text)

    except Exception as e:
        print(f"Error: {e}")
        return ""