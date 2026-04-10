from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
import json
from datetime import datetime

from app.db import get_db
from app.models import Transaction
from app.redis_client import redis_client
from app.ml_model import predict_risk_ml

router = APIRouter(prefix="/transactions", tags=["transactions"])

# ✅ SAFE INPUT MODEL (location optional)
class TransactionCreate(BaseModel):
    idempotency_key: str
    user_id: int
    amount: float
    location: str = "India"   # ✅ default prevents crash

# ✅ RULE ENGINE
def calculate_risk(amount: float) -> float:
    if amount > 10000:
        return 0.9
    elif amount > 5000:
        return 0.7
    else:
        return 0.1

# ✅ MAIN API
@router.post("/")
async def create_transaction(
    payload: TransactionCreate,
    db: AsyncSession = Depends(get_db)
):
    try:
        print("🔥 Processing transaction")

        # 🔁 REDIS CHECK
        existing = await redis_client.get(payload.idempotency_key)
        if existing:
            print("⚡ Returning cached response")
            return json.loads(existing)

        # 🔢 RULE + ML
        rule_score = calculate_risk(payload.amount)
        ml_score = predict_risk_ml(payload.amount)

        risk_score = (rule_score + ml_score) / 2

        # 🌍 LOCATION CHECK (SAFE)
        location = payload.location.lower() if payload.location else "india"
        if location != "india":
            print("🌍 Suspicious location")
            risk_score += 0.2

        # 🌙 TIME CHECK
        current_hour = datetime.now().hour
        if 0 <= current_hour <= 5:
            print("🌙 Suspicious time")
            risk_score += 0.2

        # 🔁 FREQUENCY CHECK (SAFE)
        try:
            user_key = f"user:{payload.user_id}:count"
            count = await redis_client.incr(user_key)
            if count > 5:
                print("⚠️ Too many transactions")
                risk_score += 0.3
        except Exception:
            print("Redis incr failed, skipping frequency check")

        # 🎯 FINAL SCORE
        risk_score = round(min(risk_score, 1.0), 2)

        # ✅ DECISION
        if risk_score > 0.8:
            status = "blocked"
        elif risk_score > 0.6:
            status = "declined"
        else:
            status = "approved"

        print("FINAL:", risk_score, status)

        # 💾 SAVE DB
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

        # ⚡ STORE REDIS
        await redis_client.set(payload.idempotency_key, json.dumps(response))

        return response

    except Exception as e:
        print("ERROR:", str(e))
        return {"error": str(e)}