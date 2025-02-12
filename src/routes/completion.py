from fastapi import APIRouter
from chatbot.instances import client_openai, client_anthropic
from data_models.Messages import Messages


completion_router = APIRouter(prefix="/get_completion")


@completion_router.post("/openai")
def openai_completion(request: Messages, model: str = "default"):
    return client_openai.get_completion(request.messages, model)


@completion_router.post("/anthropic")
def anthropic_completion(request: Messages, model: str = "default"):
    return client_anthropic.get_completion(request.messages, model)
