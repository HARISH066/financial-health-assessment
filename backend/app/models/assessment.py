from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from app.database import Base


class Assessment(Base):
    __tablename__ = "assessments"

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Float, nullable=False)
    risk = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

