# app/main.py
from fastapi import FastAPI
from app.core.config import settings

# Импортируем роутер
from app.api.meeting_room import router

app = FastAPI(title=settings.app_title, description=settings.app_description)

# Подключаем роутер
app.include_router(router)
