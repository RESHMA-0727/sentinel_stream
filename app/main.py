from fastapi import FastAPI, HTTPException
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

@app.post("/transaction")
async def analyze(txn: Transaction):
    risk_score = 90 if txn.amount > 5000 else 35
    status = "BLOCKED" if risk_score > 80 else "APPROVED"
    return {
        "txn_id": str(uuid.uuid4()),
        "risk_score": risk_score,
        "status": status,
        "reason": f"High value txn: ₹{txn.amount}"
    }
