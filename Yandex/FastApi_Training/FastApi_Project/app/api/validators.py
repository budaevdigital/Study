# app/api/validators.py
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.meeting_room import meeting_room_crud
from app.crud.reservation import reservation_crud
from app.models import MeetingRoom, Reservation


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


async def check_reservation_intersections(**kwargs) -> None:
    reservation = await reservation_crud.get_reservations_at_the_same_time(
        **kwargs
    )
    if reservation:
        raise HTTPException(status_code=422, detail=str(reservation))


async def check_reservation_before_edit(
    reservation_id: int, session: AsyncSession
) -> Reservation:
    reservation = await reservation_crud.get(
        # Для лучшего понимания, можно передавать параметры по ключу
        obj_id=reservation_id,
        session=session,
    )
    if not reservation:
        raise HTTPException(status_code=404, detail="Бронь не найдена!")
    return reservation
