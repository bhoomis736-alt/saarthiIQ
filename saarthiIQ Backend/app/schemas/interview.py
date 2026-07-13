from pydantic import BaseModel
from datetime import datetime


class InterviewCreate(BaseModel):
    interviewer: str
    interview_type: str
    interview_date: datetime


class InterviewUpdate(BaseModel):
    status: str
    feedback: str


class InterviewResponse(BaseModel):
    id: int
    candidate_id: int
    interviewer: str
    interview_type: str
    interview_date: datetime
    status: str
    feedback: str | None = None

    class Config:
        from_attributes = True