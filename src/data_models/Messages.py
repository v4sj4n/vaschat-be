from pydantic import BaseModel, field_validator
from enum import Enum


class Role(str, Enum):
    user = "user"
    assistant = "assistant"
    system = "system"
    developer = "developer"


class Message(BaseModel):
    role: Role
    content: str
    @field_validator("content", mode="after")
    @classmethod
    def isNotEmpty(cls, v: str):
        if len(v.strip()) == 0:
            raise ValueError("content must not be empty")
        return v
    
class Messages(BaseModel):
    messages: list[Message]

