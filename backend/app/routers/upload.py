from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd

router = APIRouter(tags=["Upload"])


@router.post("/upload-financials")
async def upload_financials(file: UploadFile = File(...)):
    """
    Upload financial file (CSV / XLSX only).
    File is processed IN-MEMORY (Render-safe).
    """

    filename = file.filename.lower()

    try:
        # -----------------------------
        # CSV SUPPORT
        # -----------------------------
        if filename.endswith(".csv"):
            df = pd.read_csv(file.file)

        # -----------------------------
        # XLSX SUPPORT
        # -----------------------------
        elif filename.endswith(".xlsx"):
            df = pd.read_excel(file.file)

        # -----------------------------
        # PDF NOT SUPPORTED (CLEAR ERROR)
        # -----------------------------
        elif filename.endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail="PDF parsing not enabled yet. Please upload CSV or XLSX."
            )

        else:
            raise HTTPException(
                status_code=400,
                detail="Unsupported file format. Upload CSV or XLSX."
            )

        # -----------------------------
        # BASIC VALIDATION
        # -----------------------------
        if df.empty:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty"
            )

        return {
            "message": "File uploaded and parsed successfully",
            "filename": file.filename,
            "rows": int(df.shape[0]),
            "columns": list(df.columns)
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process file: {str(e)}"
        )
