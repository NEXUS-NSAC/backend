from fastapi import APIRouter
from models.input import InputBaseModel, OutputBaseModel

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Hello World"}


@router.post("/generate", response_model=OutputBaseModel)
async def generate(input: InputBaseModel):
    return input
