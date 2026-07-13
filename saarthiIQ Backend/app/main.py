from fastapi import FastAPI

from app.database import Base, engine

# Models
from app.models.user import User
from app.models.candidate import Candidate
from app.models.resume import Resume
from app.models.note import Note
from app.models.interview import Interview
from app.models.campaign import Campaign
from app.models.audit import Audit

# Routes
from app.routes.auth import router as auth_router
from app.routes.users import router as users_router
from app.routes.candidates import router as candidates_router
from app.routes.resume import router as resume_router
from app.routes.parser import router as parser_router
from app.routes.resume_score import router as resume_score_router
from app.routes.job_match import router as job_match_router
from app.routes.skill_gap import router as skill_gap_router
from app.routes.ai_report import router as ai_report_router
from app.routes.dashboard import router as dashboard_router
from app.routes.search import router as search_router
from app.routes.notes import router as notes_router
from app.routes.interviews import router as interview_router
from app.routes.campaigns import router as campaigns_router
from app.routes.tasks import router as tasks_router
from app.routes.audit import router as audit_router
from app.routes.analytics import router as analytics_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SaarthiIQ API",
    version="1.0.0"
)

# Register Routes
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(candidates_router)
app.include_router(resume_router)
app.include_router(parser_router)
app.include_router(resume_score_router)
app.include_router(job_match_router)
app.include_router(skill_gap_router)
app.include_router(ai_report_router)
app.include_router(dashboard_router)
app.include_router(search_router)
app.include_router(notes_router)
app.include_router(interview_router)
app.include_router(campaigns_router)
app.include_router(tasks_router)
app.include_router(audit_router)
app.include_router(analytics_router)


@app.get("/")
def root():
    return {
        "status": "Running",
        "application": "SaarthiIQ Backend",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    return {
        "message": "Backend is healthy"
    }