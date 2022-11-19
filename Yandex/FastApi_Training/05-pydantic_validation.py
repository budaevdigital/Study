"""
Напишите валидатор, который проверит, что в запросе к API в полях name и surname отправитель не передаёт какое-нибудь имя из вселенной «Звёздные войны» (перечень запрещённых имён сохранён в константе FORBIDDEN_NAMES).

Сообщение об ошибке может быть любым.

Для работы используйте декоратор @root_validator.
«Корневой» валидатор используется без параметров.
"""
from enum import Enum

import uvicorn
from fastapi import FastAPI
from typing import Optional, Union

from pydantic import BaseModel, root_validator

FORBIDDEN_NAMES = ["Luke Skywalker", "Darth Vader", "Leia Organa", "Han Solo"]

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

    @root_validator
    def is_name_from_star_wars(cls, values):
        is_star_wars = values["name"] + " " + values["surname"]
        if is_star_wars in FORBIDDEN_NAMES:
            raise ValueError(
                "Вы не во вселенной звездных войн! Перелогиньтесь!"
            )
        return values


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


if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)
