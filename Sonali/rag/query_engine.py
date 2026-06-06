from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)

def analyze_rfp(rfp_text):

    prompt = f"""
You are an RFP analyst.

Return ONLY valid JSON.

Schema:
{{
  "project_type": "",
  "budget": "",
  "timeline": "",
  "summary": ""
}}

RFP:
{rfp_text}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=300
    )

    raw = response.choices[0].message.content.strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON returned"}


if __name__ == "__main__":

    sample_rfp = """
    We need a CRM system for our sales team.
    Budget is $50,000.
    Expected completion time is 3 months.
    """

    result = analyze_rfp(sample_rfp)

    print(result)
    print(type(result))