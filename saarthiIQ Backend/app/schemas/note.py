from pydantic import BaseModel
from datetime import datetime


class NoteCreate(BaseModel):
    note: str


class NoteResponse(BaseModel):
    id: int
    candidate_id: int
    created_by: int
    note: str
    created_at: datetime

    class Config:
        from_attributes = True