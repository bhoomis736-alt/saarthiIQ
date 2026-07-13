from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import json

from app.database import get_db
from app.models.resume import Resume
from app.models.user import User
from app.core.dependencies import get_current_user
from app.core.pdf_reader import extract_text_from_pdf
from app.core.gemini_service import client

router = APIRouter(
    prefix="/skill-gap",
    tags=["AI Skill Gap Analysis"]
)


@router.post("/{resume_id}")
def skill_gap_analysis(
    resume_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    resume = db.query(Resume).filter(
        Resume.id == resume_id
    ).first()

    if resume is None:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    resume_text = extract_text_from_pdf(
        resume.file_path
    )

    prompt = f"""
You are an expert Career Coach and Technical Recruiter.

Analyze the following resume.

Return ONLY valid JSON.

{{
    "current_skills": [],
    "missing_skills": [],
    "learning_path": [],
    "estimated_learning_time": ""
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