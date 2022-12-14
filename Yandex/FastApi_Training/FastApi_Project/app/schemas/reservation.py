# app/schemas/reservation.py

from datetime import datetime, timedelta
from pydantic import BaseModel, Extra, root_validator, validator, Field


FROM_TIME = (datetime.now() + timedelta(minutes=10)).isoformat(
    timespec="minutes"
)
TO_TIME = (datetime.now() + timedelta(hours=10)).isoformat(timespec="minutes")


# Базовый класс, от которого будем наследоваться
class ReservationRoomBase(BaseModel):
    from_reserve: datetime = Field(..., example=FROM_TIME)
    to_reserve: datetime = Field(..., example=TO_TIME)

    class Config:
        # Запрещает передавать параметры, которые не будут описаны в схеме
        extra = Extra.forbid


class ReservationRoomUpdate(ReservationRoomBase):
    @validator("from_reserve")
    def check_from_reserve_later_than_now(cls, value):
        if value <= datetime.now():
            raise ValueError(
                "Время начала бронирования не "
                "может быть меньше текущего времени"
            )
        return value

    @root_validator(skip_on_failure=True)
    def check_from_reserve_before_to_reserve(cls, values):
        if values["from_reserve"] >= values["to_reserve"]:
            raise ValueError(
                "Время начала бронирования, "
                "не может быть больше его окончания"
            )
        return values


# наследуемся от ReservationRoomUpdate с его валидаторами
class ReservationRoomCreate(ReservationRoomUpdate):
    meetingroom_id: int


# Pydantic-схема для валидации объектов из БД
# но нельзя наследоваться от ReservationRoomCreate, т.к. унаследуется и валидаторы
# и при получении старых объектов из БД, у нас будет ошибка валидации по дате:
# старые записи по дате будут уже меньше текущей даты
class ReservationRoomDB(ReservationRoomBase):
    id: int
    meetingroom_id: int

    # разрешим сериализацию объектов из БД
    class Config:
        orm_mode = True
