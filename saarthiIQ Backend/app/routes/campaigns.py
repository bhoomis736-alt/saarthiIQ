from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.campaign import Campaign
from app.models.user import User
from app.schemas.campaign import CampaignCreate, CampaignUpdate
from app.core.dependencies import get_current_user
from app.services.email_service import send_email
from app.models.candidate import Candidate

router = APIRouter(
    prefix="/campaigns",
    tags=["Email Campaigns"]
)


@router.post("/")
def create_campaign(
    data: CampaignCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    campaign = Campaign(
        campaign_name=data.campaign_name,
        subject=data.subject,
        message=data.message,
        created_by=current_user.id
    )

    db.add(campaign)
    db.commit()
    db.refresh(campaign)

    # Send email to all candidates
    candidates = db.query(Candidate).all()

    sent = 0

    for candidate in candidates:
        if candidate.email:
            success = send_email(
                candidate.email,
                campaign.subject,
                campaign.message
            )

            if success:
                sent += 1

    return {
        "message": "Campaign created successfully",
        "emails_sent": sent
    }

@router.get("/")
def get_campaigns(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Campaign).all()


@router.get("/{campaign_id}")
def get_campaign(
    campaign_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    campaign = db.query(Campaign).filter(
        Campaign.id == campaign_id
    ).first()

    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")

    return campaign


@router.put("/{campaign_id}")
def update_campaign(
    campaign_id: int,
    data: CampaignUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    campaign = db.query(Campaign).filter(
        Campaign.id == campaign_id
    ).first()

    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")

    campaign.campaign_name = data.campaign_name
    campaign.subject = data.subject
    campaign.message = data.message
    campaign.status = data.status

    db.commit()
    db.refresh(campaign)

    return campaign


@router.delete("/{campaign_id}")
def delete_campaign(
    campaign_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    campaign = db.query(Campaign).filter(
        Campaign.id == campaign_id
    ).first()

    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")

    db.delete(campaign)
    db.commit()

    return {"message": "Campaign deleted successfully"}
