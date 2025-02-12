from fastapi import APIRouter
from chatbot.instances import client_openai
from data_models.Messages import Messages


completion_router = APIRouter(prefix="/get_completion")


@completion_router.post("/openai")
def openai_completion(request: Messages, model: str = "default"):
    return client_openai.get_completion(request.messages, model)
