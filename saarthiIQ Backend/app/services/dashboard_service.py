from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.candidate import Candidate
from app.models.resume import Resume


def get_dashboard_data(db: Session):
    total_candidates = db.query(Candidate).count()
    total_resumes = db.query(Resume).count()

    dashboard = {
        "total_candidates": total_candidates,
        "total_resumes": total_resumes,

        # Future Analytics
        "average_resume_score": 0,
        "highly_recommended": 0,
        "recommended": 0,
        "consider": 0,

        "top_skills": [],
        "recent_uploads": []
    }

    return dashboard