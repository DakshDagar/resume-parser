import os
import json
import yaml
import re
from openai import OpenAI

CONFIG_PATH = "config.yaml"

def load_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        return api_key

    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            data = yaml.safe_load(f)
            return data.get("OPENAI_API_KEY")

    raise RuntimeError("OPENAI_API_KEY not found")

client = OpenAI(api_key=load_api_key())

def extract_json(text: str) -> dict:
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("Model did not return valid JSON")
    return json.loads(match.group())

def ats_extractor(resume_text: str) -> dict:
    prompt = """
You are a professional ATS resume parser.

Extract the following fields from the resume text and return ONLY valid JSON.

Required keys:
- full_name
- email
- phone
- location
- github
- linkedin
- additional_urls (array of URLs like personal website or portfolio)
- employment_details
- technical_skills
- soft_skills

Rules:
- Never invent data
- If something exists in the resume, extract it
- Use empty string "" only if the value truly does not exist
- Do NOT include markdown or explanations
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": resume_text}
        ],
        temperature=0,
        max_tokens=1400
    )

    return extract_json(response.choices[0].message.content.strip())
