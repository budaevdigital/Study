"""
Задание:
Расширьте документацию Swagger:

Добавьте в документацию теги immutable и mutable, сгруппируйте функции под тегами. Для создания тегов напишите Enum-класс с именем Tag, и в него добавьте два элемента, по числу тегов. Присвойте теги функциям, описанным в коде:
функции, которые возвращают неизменяемые типы данных, должны быть объединены тегом immutable;
функции, которые возвращают изменяемые типы данных, должны объединяться тегом mutable.
Добавьте описание ответов для каждой функции: напишите в свободной форме, какой тип данных возвращает функция.
Для каждого эндпоинта с методом GET добавьте произвольное описание через description.
Для эндпоинтов с методом POST добавьте произвольное описание через докстринг.
Каждой функции добавьте произвольное название, используя summary. Например, «Первая функция», «Вторая функция» и так далее.
Аннотируйте возвращаемые значения каждой функции.
"""
from fastapi import FastAPI
import uvicorn
from enum import Enum


# Создание объекта приложения
app = FastAPI()


# Обязательно наследуемся в таком порядке (str, Enum)
# иначе будет вызван TypeError
class Tag(str, Enum):
    IMMUTABLE = "immutable"
    MUTABLE = "mutable"


@app.get(
    "/imu",
    tags=[Tag.IMMUTABLE],
    summary="Первая функция",
    response_description="Возвращает НЕИЗМЕНЯЕМЫЙ тип данных",
    description="Функция, которая возвращает неизменяемый тип данных - Число",
)
def return_imu() -> int:
    return 243


@app.post(
    "/imu",
    tags=[Tag.IMMUTABLE],
    summary="Вторая функция",
    response_description="Возвращает НЕИЗМЕНЯЕМЫЙ тип данных",
)
def return_imu_second() -> str:
    """
    Функция, которая возвращает неизменяемый тип данных: 
    - **Строку**
    """
    return "String"


@app.get(
    "/mu",
    tags=[Tag.MUTABLE],
    summary="Третья функция",
    response_description="Возвращает ИЗМЕНЯЕМЫЙ тип данных",
    description="Функция, которая возвращает изменяемый тип данных - Список",
)
def return_mu() -> list[str]:
    return ["Первое", "Второе", "Третье"]


@app.post(
    "/mu",
    tags=[Tag.MUTABLE],
    summary="Четвертая функция",
    response_description="Возвращает ИЗМЕНЯЕМЫЙ тип данных",
)
def return_mu_second() -> set:
    """
    Функция, которая возвращает изменяемый тип данных: 
    - **Множество**
    """
    return {"Первое", "Второе", "Третье"}


if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)

