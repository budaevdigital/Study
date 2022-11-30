# app/crud/meeting_room.py

# Импортируем sessionmaker из файла с настройками БД
from app.core.db import AsyncSessionLocal
from app.models.meeting_room import MeetingRoom
from app.schemas.meeting_room import MeetingRoomCreate


# Функция работает с асинхронной сессией,
# поэтому ставим ключевое слово async.
# В функцию передаём схему MeetingRoomCreate
async def create_metting_room(new_room: MeetingRoomCreate) -> MeetingRoom:
    # Конвертируем новый объект MakeRoomCreate в словарь
    new_room_data = new_room.dict()

    # Создаём объект модели MeetingRoom.
    # В параметры передаём пары "ключ=значение", для этого распаковываем словарь.
    db_room = MeetingRoom(**new_room_data)

    # Создаём асинхронную сессию через контекстный менеджер
    async with AsyncSessionLocal() as session:
        # Добавляем созданный объект в сессию
        # Никакие действия с базой пока ещё не выполняются
        session.add(db_room)

        # Записываем изменения непосредственно в БД.
        # Так как сессия асинхронная, используем ключевое слово await.
        await session.commit()

        # Обновляем объект db_room - считываем данные из БД, чтобы получить его ID
        await session.refresh(db_room)

    # Возвращаем только то что созданный объект класса MeetingRoom
    return db_room
