# app/crud/reservation.py
from typing import Optional
from datetime import datetime
from sqlalchemy import and_, between, or_, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.base import CRUDBase
from app.models.reservation import Reservation


class CRUDReservation(CRUDBase):
    async def get_reservations_at_the_same_time(
        self,
        # Через * обозначим что все дальнейшие параметры должны передаваться по
        # ключу. И расположим  параметры со значением по-умолчанию перед
        # значениями без параметра по-умолчанию
        *,
        from_reserve: datetime,
        to_reserve: datetime,
        meetingroom_id: int,
        # Опциональный параметр - id объекта бронирования
        reservation_id: Optional[int] = None,
        session: AsyncSession,
    ) -> list[Reservation]:

        select_stmt = select(Reservation).where(
            Reservation.meetingroom_id == meetingroom_id,
            or_(
                between(
                    from_reserve,
                    Reservation.from_reserve,
                    Reservation.to_reserve,
                ),
                between(
                    to_reserve,
                    Reservation.from_reserve,
                    Reservation.to_reserve,
                ),
                and_(
                    from_reserve <= Reservation.from_reserve,
                    to_reserve >= Reservation.to_reserve,
                ),
            ),
        )
        # Если передан id бронирования, то проверим условие
        if reservation_id is not None:
            select_stmt = select_stmt.where(Reservation.id != reservation_id)
        reservations = await session.execute(select_stmt)
        reservations = reservations.scalars().all()
        return reservations

    async def get_future_reservations_for_room(
        self, room_id: int, session: AsyncSession
    ):
        reservations = await session.execute(
            # Получим все объекты Reservation
            select(Reservation).where(
                # где id равен запрашиваему room_id
                Reservation.meetingroom_id == room_id,
                #  И время окончания бронирования больше текущего времени
                Reservation.to_reserve > datetime.now(),
            )
        )
        reservations = reservations.scalars().all()
        return reservations


reservation_crud = CRUDReservation(Reservation)
