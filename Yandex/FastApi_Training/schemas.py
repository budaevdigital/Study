from enum import Enum
from pydantic import BaseModel, Field


class SelectFramework(str, Enum):
    DJANGO = "Django"
    FLASK = "Flask"
    FASTAPI = "FastApi"


class BulletIn(BaseModel):
    framework: SelectFramework = Field(..., example="FastApi")

    class Config:
        title = "Самый лучший фреймворк"
