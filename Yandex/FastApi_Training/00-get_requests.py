"""
Задание:
Напишите функцию multiplication(), которая будет обрабатывать GET-запросы к эндпоинту /multiplication.

Функция должна принимать три query-параметра:

length — обязательный, целое число;
width — обязательный, целое число;
depth — необязательный, целое число.
В ответе должно возвращаться целое число — произведение полученных параметров.

Добавьте все возможные аннотации.

Чтобы проверить документацию и сделать запросы через Swagger, перейдите по стандартному адресу /docs.
"""

from fastapi import FastAPI
import uvicorn
from typing import Optional

# Создание объекта приложения
app = FastAPI()


@app.get("/multiplication")
def multiplication(
    length: int, width: int, depth: Optional[int] = None
) -> int:
    result = length * width
    if depth is not None:
        result *= depth
    return result
