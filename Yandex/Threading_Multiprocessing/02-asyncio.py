import asyncio
from datetime import datetime

import aiohttp


async def task(task_id):
    async with aiohttp.ClientSession() as session:
        response = await session.get('https://python.org')
        response_html = await response.text()
        print(response_html[:15])
    print(f"Задача {task_id} выполнена!")


async def async_execute():
    tasks = [asyncio.ensure_future(task(i)) for i in range(1, 11)]
    await asyncio.wait(tasks)


if __name__ == "__main__":
    ioloop = asyncio.get_event_loop()
    print("Асинхронное выполнение кода:")
    start_time = datetime.now()
    ioloop.run_until_complete(async_execute())
    ioloop.close()
    end_time = datetime.now()
    print(f"Итоговое время выполнения: {end_time - start_time} секунд")
