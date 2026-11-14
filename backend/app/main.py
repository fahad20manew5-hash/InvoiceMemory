
from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from .database import engine

app = FastAPI(
    title="InvoiceMemory API",
    description="Smart Invoice and Price Tracking System",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "app": "InvoiceMemory",
        "message": "ذاكرة الفاتورة تعمل",
        "status": "online"
    }


@app.get("/api/health")
def health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected"
        }

    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail={
                "status": "unhealthy",
                "database": "disconnected"
            }
        )
