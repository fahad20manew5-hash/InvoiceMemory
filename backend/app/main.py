
from fastapi import FastAPI

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
    return {"status": "healthy"}
  
