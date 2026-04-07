from fastapi import APIRouter, Depends
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
import json  # ✅ IMPORTANT

from app.db import get_db
from app.models import Transaction
from app.redis_client import redis_client

router = APIRouter(prefix="/transactions", tags=["transactions"])

# ✅ Input model
class TransactionCreate(BaseModel):
    idempotency_key: str
    user_id: int
    amount: float

# ✅ RULE FUNCTION
def calculate_risk(amount: float) -> float:
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
    print("KEY:", payload.idempotency_key)

    # 🔥 STEP 1: CHECK REDIS
    existing = await redis_client.get(payload.idempotency_key)

    if existing:
        print("⚡ Returning cached response")
        return json.loads(existing)   # ✅ SAFE

    # 🔥 STEP 2: CALCULATE RISK
    risk_score = calculate_risk(payload.amount)
    status = "approved" if risk_score < 0.7 else "declined"

    # 🔥 STEP 3: SAVE TO DB
    tx = Transaction(
        user_id=payload.user_id,
        amount=payload.amount,
        status=status,
        risk_score=risk_score
    )

    db.add(tx)
    await db.commit()
    await db.refresh(tx)

    response = {
        "status": tx.status,
        "risk_score": tx.risk_score,
        "transaction_id": tx.id,
        "processed_at": str(tx.created_at)
    }

    # 🔥 STEP 4: STORE IN REDIS
    await redis_client.set(payload.idempotency_key, json.dumps(response))

    return response