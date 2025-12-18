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
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
        raise ValueError("Model did not return valid JSON")


def ats_extractor(resume_text: str) -> dict:
    prompt = """
You are a professional ATS resume parser.

Extract the following fields from the resume text and return ONLY valid JSON.

Required keys:
- full_name
- email
- github
- linkedin
- employment_details
- technical_skills
- soft_skills

Do not include explanations or markdown.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": resume_text}
        ],
        temperature=0,
        max_tokens=1200
    )

    content = response.choices[0].message.content.strip()
    return extract_json(content)
