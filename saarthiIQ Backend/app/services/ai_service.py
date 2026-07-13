import json
from google import genai
from google.genai import types

from app.config import settings

client = genai.Client(
    api_key=settings.GEMINI_API_KEY,
    http_options=types.HttpOptions(api_version="v1")
)


def generate_ai_report(resume_text: str):
    prompt = f"""
You are an expert Technical Recruiter.

Analyze this resume and return ONLY valid JSON.

{{
    "candidate": {{
        "full_name": "",
        "email": "",
        "phone": ""
    }},
    "resume_score": 0,
    "job_match": 0,
    "hiring_recommendation": "",
    "strengths": [],
    "weaknesses": [],
    "missing_skills": [],
    "learning_path": [],
    "recommended_jobs": [],
    "ai_summary": ""
}}

Resume:

{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()
    elif text.startswith("```"):
        text = text.replace("```", "").replace("```", "").strip()

    return json.loads(text)