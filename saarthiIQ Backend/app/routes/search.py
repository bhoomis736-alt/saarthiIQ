from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.core.dependencies import get_current_user
from app.services.search_service import search_candidates

router = APIRouter(
    prefix="/search",
    tags=["Candidate Search"]
)


@router.get("/")
def search(
    name: str = None,
    email: str = None,
    location: str = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return search_candidates(
        db,
        name,
        email,
        location
    )