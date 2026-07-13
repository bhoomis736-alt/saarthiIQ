from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.note import Note
from app.models.candidate import Candidate
from app.models.user import User
from app.schemas.note import NoteCreate
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/notes",
    tags=["Recruiter Notes"]
)


@router.post("/{candidate_id}")
def add_note(
    candidate_id: int,
    data: NoteCreate,
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

    note = Note(
        candidate_id=candidate_id,
        created_by=current_user.id,
        note=data.note
    )

    db.add(note)
    db.commit()
    db.refresh(note)

    return note