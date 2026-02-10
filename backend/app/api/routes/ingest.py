from fastapi import APIRouter, Depends, UploadFile
from app.core.dependencies import get_ingest_service

router = APIRouter()

@router.post("/ingest")
async def ingest(file: UploadFile, service=Depends(get_ingest_service)):
    file_bytes = await file.read()
    log_text = file_bytes.decode("utf-8", errors="ignore")
    service.ingest(log_text)
    return {"status": "ok"}
