# app/api/meeting_room.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_async_session
from app.crud.meeting_room import create_metting_room, get_room_id_by_name
from app.schemas.meeting_room import MeetingRoomCreate, MeetingRoomDB

router = APIRouter()


@router.post(
    "/meeting_rooms/",
    response_model=MeetingRoomDB,
    # Чтобы не показывать опциональные поля None, укажем параметр _exclude_none
    # Если надо не показывать все значения по-умолчанию - _exclude_default
    response_model_exclude_none=True,
)
async def create_new_meeting_room(
    meeting_room: MeetingRoomCreate,
    # Указываем зависимость, предоставляющую объект сессии, как параметр функции
    session: AsyncSession = Depends(get_async_session),
):
    # Вызываем функцию проверки уникальности поля name
    # и вторым параметром передаём сессию в CRUD функцию
    room_id = await get_room_id_by_name(meeting_room.name, session)
    # Если такой объект уже есть в базе - вызвать ошибку
    if room_id is not None:
        raise HTTPException(
            status_code=422,
            detail="Такая переговорная комната уже существует!",
        )
        # Вторым параметром передаём сессию в CRUD функцию
    new_room = await create_metting_room(meeting_room, session)
    return new_room
