from sqlalchemy.orm import Session
from app.models.audit import Audit


def log_action(
    db: Session,
    action: str,
    module: str,
    user_id: int
):
    log = Audit(
        action=action,
        module=module,
        user_id=user_id
    )

    db.add(log)
    db.commit()