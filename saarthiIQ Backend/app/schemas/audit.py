from datetime import datetime
from pydantic import BaseModel


class AuditResponse(BaseModel):
    id: int
    action: str
    module: str
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True