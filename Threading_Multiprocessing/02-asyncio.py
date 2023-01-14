import asyncio
from datetime import datetime

# Асинхронная альтернатива requests.
import aiohttp

# Обычная функция task() преобразована в корутину.
# Об этом говорит ключевое слово async перед def.


async def task(task_id):
    # Создание новой сессии для GET-запроса.
    async with aiohttp.ClientSession() as session:
        # Выполнение GET-запроса в рамках созданной сессии.
        response = await session.get("https://python.org")
        response_html = await response.text()
        print(response_html[:15])
    print(f"Задача {task_id} выполнена.")


# Обычная функция sync_execute() преобразована в корутину верхнего уровня.
# В ней нужно сформировать список задач для цикла событий.
async def async_execute():
    # Метод ensure_future() оборачивает переданную корутину в задачу,
    # которой может управлять цикл событий.
    tasks = [asyncio.ensure_future(task(i)) for i in range(1, 11)]
    # Запуск задач до получения любого первого результата.
    await asyncio.wait(tasks)


if __name__ == "__main__":

    print("Асинхронное выполнение кода:")
    start_time = datetime.now()

    # Создание цикла событий.
    myloop = asyncio.get_event_loop()
    # В цикл событий передаётся корутина верхнего уровня async_execute().
    # Она формирует список задач для цикла и запускает их на выполнение.
    myloop.run_until_complete(async_execute())
    # Завершение цикла событий после выполнения всех задач.
    myloop.close()

    # Верхние 3 строчки, можно заменить одной...
    # asyncio.run(async_execute())

    end_time = datetime.now()
    print(f"Итоговое время выполнения: {end_time - start_time} секунд.")
