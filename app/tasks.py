import time
from app.celery_app import celery_app

@celery_app.task
def check_transaction_task(amount, user_id, merchant):
    time.sleep(5)
    risk = 90 if amount > 5000 else 35
    status = "BLOCKED" if risk > 70 else "APPROVED"

    return {
        "user_id": user_id,
        "merchant": merchant,
        "risk": risk,
        "status": status,
        "message": "Background task complete"
    }
