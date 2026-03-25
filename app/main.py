from fastapi import FastAPI
from pydantic import BaseModel
import uuid
from datetime import datetime

app = FastAPI(title="SentinelStream", version="Week2")

class Transaction(BaseModel):
    amount: float
    user_id: str
    merchant: str
    location: str = "India"
    device_id: str

@app.get("/")
async def root():
    return {"status": "SentinelStream Week2 LIVE ✅"}

@app.get("/user/{user_id}")
async def get_profile(user_id: str):
    return {"user_id": user_id, "country": "India", "avg_txn": 2500, "risk": 25}

@app.post("/transaction")
async def analyze(txn: Transaction):
    risk_score = 90 if txn.amount > 5000 else 35
    status = "BLOCKED" if risk_score > 80 else "APPROVED"
    return {
        "txn_id": str(uuid.uuid4()),
        "risk_score": risk_score,
        "status": status,
        "reason": f"Amount ₹{txn.amount}",
        "user_risk": 25
    }
