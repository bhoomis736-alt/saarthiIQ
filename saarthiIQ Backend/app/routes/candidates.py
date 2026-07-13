from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.candidate import Candidate
from app.models.user import User
from app.schemas.candidate import (
    CandidateCreate,
    CandidateUpdate,
    CandidateResponse
)
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"]
)


# ==========================
# Create Candidate
# ==========================
@router.post("/", response_model=CandidateResponse)
def create_candidate(
    candidate: CandidateCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_candidate = Candidate(
        full_name=candidate.full_name,
        email=candidate.email,
        phone=candidate.phone,
        skills=candidate.skills,
        experience=candidate.experience,
        location=candidate.location,
        resume_url=candidate.resume_url,
        created_by=current_user.id
    )

    db.add(new_candidate)
    db.commit()
    db.refresh(new_candidate)

    return new_candidate


# ==========================
# Get All Candidates
# ==========================
@router.get("/", response_model=list[CandidateResponse])
def get_all_candidates(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    candidates = db.query(Candidate).all()
    return candidates


# ==========================
# Get Candidate By ID
# ==========================
@router.get("/{candidate_id}", response_model=CandidateResponse)
def get_candidate_by_id(
    candidate_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if candidate is None:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )

    return candidate


# ==========================
# Update Candidate
# ==========================
@router.put("/{candidate_id}", response_model=CandidateResponse)
def update_candidate(
    candidate_id: int,
    updated_candidate: CandidateUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if candidate is None:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )

    candidate.full_name = updated_candidate.full_name
    candidate.email = updated_candidate.email
    candidate.phone = updated_candidate.phone
    candidate.skills = updated_candidate.skills
    candidate.experience = updated_candidate.experience
    candidate.location = updated_candidate.location
    candidate.resume_url = updated_candidate.resume_url

    db.commit()
    db.refresh(candidate)

    return candidate


# ==========================
# Delete Candidate
# ==========================
@router.delete("/{candidate_id}")
def delete_candidate(
    candidate_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if candidate is None:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )

    db.delete(candidate)
    db.commit()

    return {
        "message": "Candidate deleted successfully"
    }