from sqlalchemy.orm import Session

from app.models.candidate import Candidate
from app.models.user import User
from app.models.interview import Interview
from app.models.task import Task
from app.models.campaign import Campaign


def get_dashboard_stats(db: Session):
    return {
        "total_candidates": db.query(Candidate).count(),
        "total_users": db.query(User).count(),
        "total_interviews": db.query(Interview).count(),
        "total_tasks": db.query(Task).count(),
        "total_campaigns": db.query(Campaign).count(),
    }