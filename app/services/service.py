from app.models.response_models import NameResponse

def generate_name_message(name: str) -> NameResponse:
    message = f"{name}, that is a great name."
    return NameResponse(message=message)
