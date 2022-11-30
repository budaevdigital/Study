# app/schemas/meeting_room.py

from typing import Optional
from pydantic import BaseModel, Field, validator


class MeetingRoomCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: Optional[str]

    @validator("name")
    def name_is_numeric(cls, value: str):
        if value.isnumeric():
            raise ValueError("Имя не может быть числом")
        return value
