# app/models/meeting_room.py

from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from app.core.db import Base


class MeetingRoom(Base):
    # nullable = Значит, что не должно быть пустым
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    # Установим связь между моделями через relationship по принципу OneToMany
    # в модели Relationship ссылка на таблицу MeetingRoom через ForeignKey
    # В relationship прописываем строку, а не передаём класс - иначе, в случае
    # двухстороннего доступа от модели к модели будут циклические импорты
    reservations = relationship("Reservation", cascade="delete")
