# app/api/validators.py
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.meeting_room import meeting_room_crud
from app.models.meeting_room import MeetingRoom


# Корутина, которая проверяет уникальность имени переговорной
async def check_name_duplicate(room_name: str, session: AsyncSession) -> None:
    # и вторым параметром передаём сессию в CRUD функцию
    room_id = await meeting_room_crud.get_room_id_by_name(room_name, session)
    # Если такой объект уже есть в базе - вызвать ошибку
    if room_id is not None:
        raise HTTPException(
            status_code=422,
            detail="Такая переговорная комната уже существует!",
        )


# Корутина, которая проверяет, существует ли объект в БД с таким ID
async def check_meeting_room_exists(
    meeting_room_id: int, session: AsyncSession
) -> MeetingRoom:
    # Получаем объект из БД по ID
    meeting_room = await meeting_room_crud.get(meeting_room_id, session)
    if meeting_room is None:
        raise HTTPException(status_code=404, detail="Переговорка не найдена")
    return meeting_room
