from fastapi import APIRouter, Body
from schemas import BulletIn

router = APIRouter()


@router.post("/")
def choose_framework(
    voice: BulletIn = Body(
        ...,
        examples={
            "first": {
                "summary": "FastApi - Лучший фреймворк",
                "description": "FastApi самый лучший фреймворк",
                "value": {"framework": "FastApi"},
            },
            "second": {
                "summary": "Django - Лучший фреймворк",
                "description": "Django самый лучший фреймворк",
                "value": {"framework": "Django"},
            },
            "threed": {
                "summary": "Flask - Лучший фреймворк",
                "description": "Flask самый лучший фреймворк",
                "value": {"framework": "Flask"},
            },
        },
    )
) -> dict[str, str]:
    return {"The winner is": "FastAPI"}
