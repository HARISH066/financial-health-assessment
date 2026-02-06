from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from app.database import Base

class Assessment(Base):
    __tablename__ = "assessments"

    id = Column(Integer, primary_key=True, index=True)
    revenue = Column(Float)
    expenses = Column(Float)
    profit = Column(Float)
    profit_margin = Column(Float)
    cash_flow_ratio = Column(Float)
    score = Column(Float)
    risk = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
