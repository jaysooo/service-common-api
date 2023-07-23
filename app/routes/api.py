from fastapi import APIRouter
from src.endpoints import data_endpoint

router = APIRouter()
router.include_router(data_endpoint.router)
