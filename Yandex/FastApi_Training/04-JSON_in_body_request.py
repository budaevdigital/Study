"""
Задание

Недавно вы устроились на работу программистом в аукционный дом, занимающийся продажей всякой всячины.
Ближайшее мероприятие будет посвящено продаже компьютерной техники конца XX века.

Продавцы должны подать заявки в установленной форме через Интернет.

В заявке должны быть указаны:
- категория товара,
- название лота,
- точное название модели (необязательно),
- стартовая цена (необязательно, если не указана, то считается равной 1000),
- данные продавца.

Заявки принимаются на лоты только в четырёх категориях:
- Принтеры
- Мониторы
- Доп. оборудование
- Устройства ввода

Ваша задача — написать приложение на FastAPI, которое будет обрабатывать валидные заявки и отклонять невалидные.
"""
from enum import Enum

import uvicorn
from fastapi import FastAPI, Query
from typing import Optional, Union
from pydantic import BaseModel

app = FastAPI(redoc_url=None)


class Category(str, Enum):
    PRINTERS = "Принтеры"
    MONITORS = "Мониторы"
    OTHER_EQUIPMENT = "Доп. оборудование"
    INPUT_OUTPUT = "Устройства ввода"


class SellerInfo(BaseModel):
    name: str
    surname: Union[str, list[str]]
    phone: Optional[str]
    address: Optional[str]
    age: Optional[int]
    is_staff: bool = False


class LotInfo(BaseModel):
    category: Category
    name: str
    model: Optional[str]
    start_price: int = 1000
    seller: SellerInfo


# JSON в теле пост запроса
@app.post("/lot")
def reg_lot(lot: LotInfo):
    return {"result": "Заявка принята"}


# Часть с Query параметрами
@app.post("/", tags=["product for sell"], summary="Товар на продажу")
def sell_product(
    # * позволит расположить аргументы в нужном порядке
    *,
    category: Category,
    name_lot: str = Query(
        ...,
        alias="name",
        title="Название лота",
        description="Напишите название лота",
    ),
    name_product: str = Query(
        None,
        alias="model",
        title="Название модели",
        description="Необязательно. Напишите точное название модели товара",
    ),
    price: int = Query(
        1000,
        alias="start_price",
        title="Укажите начальную цену",
        description="Необязательно. Если не указана, то стартовая цена = 1000",
    ),
    seller: SellerInfo,
) -> dict[str, str]:
    return {"result": "Заявка принята"}


if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)
