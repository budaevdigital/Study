# app/api/endpoints/reservation.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_async_session
from app.crud.reservation import reservation_crud
from app.api.validators import (
    check_meeting_room_exists,
    check_reservation_intersections,
    check_reservation_before_edit,
)
from app.schemas.reservation import (
    ReservationRoomDB,
    ReservationRoomUpdate,
    ReservationRoomCreate,
)


router = APIRouter()


# у объекта Reservation нет опциональных полей, поэтому нет
# параметра response_model_exclude_none=True
@router.post("/", response_model=ReservationRoomDB)
async def create_reservation(
    reservation: ReservationRoomCreate,
    session: AsyncSession = Depends(get_async_session),
):
    await check_meeting_room_exists(reservation.meetingroom_id, session)
    await check_reservation_intersections(
        # Т.к. валидатор принимает **kwargs, аргументы нужно передать
        # с указанием ключей
        **reservation.dict(),
        session=session
    )
    new_reservation = await reservation_crud.create(reservation, session)
    return new_reservation


@router.get("/", response_model=list[ReservationRoomDB])
async def get_all_reservation(
    session: AsyncSession = Depends(get_async_session),
):
    reservations = await reservation_crud.get_multi(session)
    return reservations


@router.delete("/{reservation_id}", response_model=ReservationRoomDB)
async def delete_reservation(
    reservation_id: int, session: AsyncSession = Depends(get_async_session)
):
    reservation = await check_reservation_before_edit(reservation_id, session)
    reservation = await reservation_crud.remove(reservation, session)
    return reservation


@router.patch("/{reservation_id}", response_model=ReservationRoomDB)
async def update_reservation(
    reservation_id: int,
    obj_in: ReservationRoomUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    # Проверяем, что объект бронирования уже существует
    reservation = await check_reservation_before_edit(reservation_id, session)
    # Проверяем, что нет пересечений с другими бронированиями
    await check_reservation_intersections(
        # Новое время бронирования, распаковываем на ключевые аргументы
        **obj_in.dict(),
        reservation_id=reservation_id,
        meetingroom_id=reservation.meetingroom_id,
        session=session
    )
    reservation = await reservation_crud.update(
        db_obj=reservation, obj_in=obj_in, session=session
    )
    return reservation
