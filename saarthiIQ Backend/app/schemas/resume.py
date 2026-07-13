from pydantic import BaseModel
from datetime import datetime


class ResumeResponse(BaseModel):
    id: int
    file_name: str
    file_path: str
    candidate_id: int
    uploaded_at: datetime

    class Config:
        from_attributes = True