from sqlalchemy.orm import Session
from app.models.candidate import Candidate


def search_candidates(
    db: Session,
    name: str = None,
    email: str = None,
    location: str = None
):
    query = db.query(Candidate)

    if name:
        query = query.filter(
            Candidate.full_name.ilike(f"%{name}%")
        )

    if email:
        query = query.filter(
            Candidate.email.ilike(f"%{email}%")
        )

    if location:
        query = query.filter(
            Candidate.location.ilike(f"%{location}%")
        )

    return query.all()