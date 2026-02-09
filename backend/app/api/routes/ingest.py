from fastapi import APIRouter, Depends
from app.core.dependencies import get_ingest_service

router = APIRouter()

@router.post("/ingest")
def ingest(path: str, service=Depends(get_ingest_service)):
    service.ingest(path)
    return {"status": "ok"}
