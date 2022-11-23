# app/models/meeting_room.py

from sqlalchemy import Column, String
from app.core.db import Base


class MeetingRoom(Base):
    # nullable = Значит, что не должно быть пустым
    name = Column(String(100), unique=True, nullable=False)
