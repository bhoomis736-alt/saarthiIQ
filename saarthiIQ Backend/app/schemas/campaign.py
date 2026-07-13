from pydantic import BaseModel
from datetime import datetime


class CampaignCreate(BaseModel):
    campaign_name: str
    subject: str
    message: str


class CampaignUpdate(BaseModel):
    campaign_name: str
    subject: str
    message: str
    status: str


class CampaignResponse(BaseModel):
    id: int
    campaign_name: str
    subject: str
    message: str
    status: str
    created_by: int
    created_at: datetime

    class Config:
        from_attributes = True