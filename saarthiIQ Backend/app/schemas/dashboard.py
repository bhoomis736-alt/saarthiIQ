from pydantic import BaseModel


class DashboardStats(BaseModel):
    total_candidates: int
    total_users: int
    total_interviews: int
    total_tasks: int
    total_campaigns: int