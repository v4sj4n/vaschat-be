import os
from dotenv import load_dotenv
from chatbot.providers import openai_provider


load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
anthropic_key = os.getenv("ANTHROPIC_API_KEY")  # to be implemented
google_key = os.getenv("GOOGLE_API_KEY")  # to be implemented
mistral_key = os.getenv("MISTRAL_API_KEY")  # to be implemented
cohere_key = os.getenv("COHERE_API_KEY")  # to be implemented


client_openai = openai_provider.OpenAIClient(api_key=openai_key)
