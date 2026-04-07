from fastapi import FastAPI
from app.transactions import router as tx_router

# THIS LINE IS VERY IMPORTANT
app = FastAPI(title="SentinelStream")

# include transaction routes
app.include_router(tx_router)

# health check
@app.get("/health")
async def health():
    return {"status": "ok"}