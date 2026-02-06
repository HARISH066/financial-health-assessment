from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from app.database import SessionLocal
from app.models import Assessment

router = APIRouter()

@router.post("/analyze-csv")
def analyze_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV allowed")

    df = pd.read_csv(file.file)

    if df.empty:
        raise HTTPException(status_code=400, detail="CSV is empty")

    revenue = df["revenue"].sum()
    expenses = df["expenses"].sum()
    profit = revenue - expenses
    profit_margin = profit / revenue if revenue else 0
    cash_flow_ratio = revenue / expenses if expenses else 0

    score = round(min(100, profit_margin * 100), 2)
    risk = "Low" if score > 60 else "Medium" if score > 40 else "High"

    db = SessionLocal()

    record = Assessment(
        revenue=revenue,
        expenses=expenses,
        profit=profit,
        profit_margin=profit_margin,
        cash_flow_ratio=cash_flow_ratio,
        score=score,
        risk=risk
    )

    db.add(record)
    db.commit()
    db.refresh(record)
    db.close()

    return {
        "metrics": {
            "revenue": revenue,
            "expenses": expenses,
            "profit": profit,
            "profit_margin": profit_margin,
            "cash_flow_ratio": cash_flow_ratio
        },
        "assessment": {
            "score": score,
            "risk": risk
        }
    }
