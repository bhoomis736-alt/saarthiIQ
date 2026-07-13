from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.resume import Resume
from app.models.user import User
from app.core.dependencies import get_current_user
from app.core.pdf_reader import extract_text_from_pdf
from app.services.ai_service import generate_ai_report

router = APIRouter(
    prefix="/ai-report",
    tags=["AI Candidate Report"]
)


@router.post("/{resume_id}")
def ai_candidate_report(
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

    report = generate_ai_report(
        resume_text
    )

    return report