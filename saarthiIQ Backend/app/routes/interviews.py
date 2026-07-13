from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.interview import Interview
from app.models.candidate import Candidate
from app.models.user import User
from app.schemas.interview import InterviewCreate, InterviewUpdate
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/interviews",
    tags=["Interview Management"]
)


@router.post("/{candidate_id}")
def schedule_interview(
    candidate_id: int,
    data: InterviewCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )

    interview = Interview(
        candidate_id=candidate_id,
        interviewer=data.interviewer,
        interview_type=data.interview_type,
        interview_date=data.interview_date
    )

    db.add(interview)
    db.commit()
    db.refresh(interview)

    return interview


@router.get("/{candidate_id}")
def get_interviews(
    candidate_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Interview).filter(
        Interview.candidate_id == candidate_id
    ).all()


@router.put("/{interview_id}")
def update_interview(
    interview_id: int,
    data: InterviewUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    interview = db.query(Interview).filter(
        Interview.id == interview_id
    ).first()

    if not interview:
        raise HTTPException(
            status_code=404,
            detail="Interview not found"
        )

    interview.status = data.status
    interview.feedback = data.feedback

    db.commit()
    db.refresh(interview)

    return interview