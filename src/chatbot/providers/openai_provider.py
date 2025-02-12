from openai import OpenAI
from data_models.Messages import Message, Role, Messages


class OpenAIClient:
    client = None
    system_message = Message(
        role=Role.developer,
        content="You are a short and concise chatbot, you like to give witty and quirky answers like a gen z.",
    )

    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def get_completion(self, messages: Messages, model: str):
        model = "gpt-3.5-turbo-16k" if model == "default" else model

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            temperature=0,
            messages=[self.system_message, *messages],
        )
        return Message(role=Role.assistant, content=response.choices[0].message.content)
