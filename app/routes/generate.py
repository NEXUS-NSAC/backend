from fastapi import APIRouter
from models.input import InputBaseModel

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Hello World"}


@router.post("/generate", response_model=dict)
async def generate(input: InputBaseModel):
    return input
