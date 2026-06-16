from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime

Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    amount = Column(Float)
    status = Column(String)
    risk_score = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)