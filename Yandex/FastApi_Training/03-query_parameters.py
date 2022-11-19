"""
Задание:
Обработайте GET-запрос.

Эндпоинт /math-sum должен принимать и обрабатывать GET-запросы с единственным query-параметром add. В этом параметре может быть передан список дробных чисел (float).

Числа в списке должны быть строго больше 0 и строго меньше 9.99.

В ответе верните сумму чисел из списка, округлённую до двух знаков после запятой.

Добавьте параметру add название и описание — придумайте их самостоятельно.
"""
from fastapi import Query, FastAPI
import uvicorn

app = FastAPI(redoc_url=None)


@app.get(
    "/math-sum",
    tags=["Summary float number"],
    summary="Сумма округлённая до двух знаков",
    response_description=(
        "Сумма вещественных чисел, "
        "округленная до двух знаков. Каждое число от 0 до 9.99"
    ),
)
def muath_float_number(
    add: list[float] = Query(
        ...,
        gt=0,
        lt=9.99,
        alias="summ",
        title="Сумма чисел",
        description="Можно передать список чисел",
    )
) -> float:
    return round(sum(add), 2)


if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)
