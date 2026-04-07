from fastapi import APIRouter, Depends
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db
from app.models import Transaction

router = APIRouter(prefix="/transactions", tags=["transactions"])

# ✅ Input model
class TransactionCreate(BaseModel):
    idempotency_key: str
    user_id: int
    amount: float

# ✅ RULE FUNCTION (MUST BE ABOVE)
def calculate_risk(amount: float) -> float:
    print("CALCULATING RISK:", amount)

    if amount > 10000:
        return 0.9
    elif amount > 5000:
        return 0.7
    else:
        return 0.1

# ✅ API
@router.post("/")
async def create_transaction(
    payload: TransactionCreate,
    db: AsyncSession = Depends(get_db)
):
    print("🔥 RULE CHECK:", payload.amount)

    risk_score = calculate_risk(payload.amount)
    status = "approved" if risk_score < 0.7 else "declined"

    tx = Transaction(
        user_id=payload.user_id,
        amount=payload.amount,
        status=status,
        risk_score=risk_score
    )

    db.add(tx)
    await db.commit()
    await db.refresh(tx)

    return {
        "status": tx.status,
        "risk_score": tx.risk_score,
        "transaction_id": tx.id,
        "processed_at": str(tx.created_at)
    }