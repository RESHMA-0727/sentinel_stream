from fastapi import FastAPI
from pydantic import BaseModel
import uuid
from app.cache import get_user_profile

app = FastAPI()

class Transaction(BaseModel):
    amount: float
    user_id: str
    merchant: str

@app.get("/")
async def root():
    return {"status": "Week3 Day1 ✅"}

@app.post("/transaction")
async def analyze(txn: Transaction):
    profile = get_user_profile(txn.user_id)
    risk = 90 if txn.amount > 5000 else 35
    final = (risk + profile["risk"]) / 2
    status = "🚫 BLOCKED" if final > 60 else "✅ APPROVED"
    
    return {
        "txn_id": str(uuid.uuid4()),
        "risk": round(final),
        "status": status,
        "cache": "HIT"
    }
