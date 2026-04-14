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

# ✅ INPUT MODEL
class TransactionCreate(BaseModel):
    idempotency_key: str
    user_id: int
    amount: float
    location: str = "India"

# ✅ RULE ENGINE
def calculate_risk(amount: float) -> float:
    if amount > 10000:
        return 0.9
    elif amount > 5000:
        return 0.7
    else:
        return 0.1

@router.post("/")
async def create_transaction(
    payload: TransactionCreate,
    db: AsyncSession = Depends(get_db)
):
    try:
        reasons = []

        # 🔁 IDEMPOTENCY CHECK
        existing = await redis_client.get(payload.idempotency_key)
        if existing:
            return json.loads(existing)

        # 🔢 RULE + ML
        rule_score = calculate_risk(payload.amount)
        ml_score = predict_risk_ml(payload.amount)
        risk_score = (rule_score + ml_score) / 2

        # 💰 AMOUNT CHECK
        if payload.amount > 5000:
            reasons.append("High transaction amount")

        # 🌍 LOCATION CHECK
        if payload.location.lower() != "india":
            risk_score += 0.2
            reasons.append("Unusual location")

        # 🌙 TIME CHECK
        current_hour = datetime.now().hour
        if 0 <= current_hour <= 5:
            risk_score += 0.2
            reasons.append("Transaction at unusual time")

        # 🔁 FREQUENCY CHECK
        try:
            user_key = f"user:{payload.user_id}:count"
            count = await redis_client.incr(user_key)
            if count > 5:
                risk_score += 0.3
                reasons.append("Too many transactions in short time")
        except:
            pass

        # 🎯 FINAL SCORE
        risk_score = round(min(risk_score, 1.0), 2)

        # 📊 DECISION + RISK LEVEL
        if risk_score > 0.8:
            status = "blocked"
            risk_level = "HIGH"
        elif risk_score > 0.6:
            status = "declined"
            risk_level = "MEDIUM"
        else:
            status = "approved"
            risk_level = "LOW"

        # 🚨 DEMO-FRIENDLY USER FLAG (INSTANT)
        user_flag = "NORMAL"
        try:
            if risk_score > 0.7:
                await redis_client.incr(f"user:{payload.user_id}:risk")
                user_flag = "SUSPICIOUS"
        except:
            pass

        # 💾 SAVE TO DB
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
            "risk_level": risk_level,
            "reason": reasons,
            "user_flag": user_flag,
            "transaction_id": tx.id,
            "processed_at": str(tx.created_at)
        }

        # ⚡ CACHE RESPONSE
        await redis_client.set(payload.idempotency_key, json.dumps(response))

        return response

    except Exception as e:
        return {"error": str(e)}