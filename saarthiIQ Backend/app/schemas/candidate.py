from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# Candidate Create Schema
class CandidateCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    skills: Optional[str] = None
    experience: Optional[str] = None
    location: Optional[str] = None
    resume_url: Optional[str] = None


# Candidate Update Schema
class CandidateUpdate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    skills: str
    experience: str
    location: str
    resume_url: str


# Candidate Response Schema
class CandidateResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone: str
    skills: Optional[str]
    experience: Optional[str]
    location: Optional[str]
    resume_url: Optional[str]
    status: str
    created_by: int
    created_at: datetime

    class Config:
        from_attributes = True