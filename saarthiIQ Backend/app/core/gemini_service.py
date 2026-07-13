import json
from google import genai
from google.genai import types
from app.config import settings

# Create Gemini Client
client = genai.Client(
    api_key=settings.GEMINI_API_KEY,
    http_options=types.HttpOptions(api_version="v1")
)


def parse_resume_with_ai(resume_text: str):
    prompt = f"""
You are an expert AI Resume Parser.

Extract the following information from the resume.

Return ONLY valid JSON.

{{
    "full_name": "",
    "email": "",
    "phone": "",
    "skills": [],
    "experience": "",
    "education": "",
    "location": ""
}}

Resume:

{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    text = response.text.strip()

    # Remove markdown if Gemini returns ```json
    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    elif text.startswith("```"):
        text = text.replace("```", "").replace("```", "").strip()

   