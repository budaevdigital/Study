"""
Задание
Вас наняла компания “FastAPI Incorporation”, чтобы вы помогли им провести самые честные выборы лучшего Python-фреймворка. Весь код уже написан, но он находится в одном файле main.py.

Проведите рефакторинг: разнесите код по файлам api.py, main.py и schemas.py.
Допишите всё необходимое, чтобы приложение осталось работоспособным.

И помните: всё, что вы увидите в коде — закрыто NDA и не подлежит разглашению!
"""

from fastapi import FastAPI
import uvicorn
from api import router

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)
