from fastapi import APIRouter
from routes import generate

router = APIRouter()

router.include_router(generate.router, prefix="/generate", tags=["generate"])
