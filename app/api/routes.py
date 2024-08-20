from fastapi import APIRouter, Depends
from app.models.request_models import NameRequest
from app.models.response_models import NameResponse
from app.services.service import generate_name_message

router = APIRouter()

@router.post("/name", response_model=NameResponse)
def get_name_message(request: NameRequest):
    response = generate_name_message(request.name)
    return response
