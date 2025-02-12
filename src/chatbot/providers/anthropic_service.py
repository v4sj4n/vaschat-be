from anthropic import Anthropic
from data_models.Messages import Message, Role, Messages
import logging


class AnthropicService:
    client = None
    system_message = "You are a short and concise chatbot, you like to give witty and quirky answers like a gen z."

    def __init__(self, api_key: str):
        self.client = Anthropic(api_key=api_key)

    def get_completion(self, messages: Messages, model: str):
        model = "claude-3-haiku-20240307" if model == "default" else model

        try:
            formatted_messages = [
                {
                    "role": "user" if msg.role == Role.user else "assistant",
                    "content": msg.content,
                }
                for msg in messages
            ]
            print(formatted_messages)
            response = self.client.messages.create(
                system=self.system_message,
                model=model,
                temperature=0,
                messages=formatted_messages,
                max_tokens=1024,
            )
            return Message(role=Role.assistant, content=response.content[0].text)
        except Exception as e:
            logging.error(f"Error: {e}")
            return "Error: Unable to connect to Anthropic API"
