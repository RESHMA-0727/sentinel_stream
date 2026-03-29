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

from app.tasks import check_transaction_task
from celery.result import AsyncResult
from app.celery_app import celery_app

@app.post("/background-check")
def background_check():
    task = check_transaction_task.delay(7200, "user_101", "amazon")
    return {
        "message": "Task submitted",
        "task_id": task.id
    }

@app.get("/task-status/{task_id}")
def task_status(task_id: str):
    task_result = AsyncResult(task_id, app=celery_app)
    return {
        "task_id": task_id,
        "status": task_result.status,
        "result": task_result.result if task_result.ready() else None
    }
