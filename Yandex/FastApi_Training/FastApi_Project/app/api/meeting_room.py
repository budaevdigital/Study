# app/api/meeting_room.py
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_async_session
from app.crud.meeting_room import (
    create_meeting_room,
    get_room_id_by_name,
    read_all_rooms_from_db,
    update_meeting_room,
    get_meeting_room_by_id,
)
from app.schemas.meeting_room import (
    MeetingRoomCreate,
    MeetingRoomDB,
    MeetingRoomUpdate,
)

# в параметре tags пропишем общий тег, который отобразится в Swagger
router = APIRouter(prefix="/meeting_rooms", tags=["Meeting Rooms"])


@router.post(
    "/",
    response_model=MeetingRoomDB,
    # Чтобы не показывать опциональные поля None, укажем параметр _exclude_none
    # Если надо не показывать все значения по-умолчанию - _exclude_default
    response_model_exclude_none=True,
)
async def create_new_meeting_room(
    meeting_room: MeetingRoomCreate,
    # Указываем зависимость, предоставляющую объект сессии как параметр функции
    session: AsyncSession = Depends(get_async_session),
):
    # Вызываем функцию проверки уникальности поля name
    await check_name_duplicate(meeting_room.name, session)
    # Вторым параметром передаём сессию в CRUD функцию
    new_room = await create_meeting_room(meeting_room, session)
    return new_room


@router.get(
    "/",
    response_model=List[MeetingRoomDB],
    response_model_exclude_none=True,
)
async def get_all_meeting_rooms(
    session: AsyncSession = Depends(get_async_session),
):
    get_rooms = await read_all_rooms_from_db(session)
    return get_rooms


# Обновление объекта передаём PATH методом
@router.patch(
    "/{meeting_room_id}",
    response_model=MeetingRoomDB,
    response_model_exclude_none=True,
)
async def partially_update_meeting_room(
    # ID обновляемого объекта
    meeting_room_id: int,
    # JSON-данные, которые отправил пользователь
    obj_in: MeetingRoomUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    # Получаем объект из БД по ID
    meeting_room = await get_meeting_room_by_id(meeting_room_id, session)

    if meeting_room is None:
        raise HTTPException(status_code=404, detail="Переговорка не найдена")

    if obj_in.name is not None:
        # Если в переданных данных, есть поле name
        # проверяем его на уникальность
        await check_name_duplicate(obj_in.name, session)

    # Когда проверки завершены - передаём в корутину
    # все необходимые для обновления данные
    meeting_room = await update_meeting_room(meeting_room, obj_in, session)
    return meeting_room


# Корутина, которая проверяет уникальность имени переговорной
async def check_name_duplicate(room_name: str, session: AsyncSession) -> None:
    # и вторым параметром передаём сессию в CRUD функцию
    room_id = await get_room_id_by_name(room_name, session)
    # Если такой объект уже есть в базе - вызвать ошибку
    if room_id is not None:
        raise HTTPException(
            status_code=422,
            detail="Такая переговорная комната уже существует!",
        )
