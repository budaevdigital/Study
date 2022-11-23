# app/core/db.py

# Все классы и функции для асинхронной работы
# находятся в модуле sqlalchemy.ext.asyncio
from sqlalchemy import Integer, Column
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker, declared_attr

from app.core.config import settings


class PreBase:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(settings.database_url)

# Создадим асинхронную сессии
# Для работы, нужно постоянно открывать и закрывать
# сессии (для каждого запроса), поэтому применим
# функцию sessionmaker
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)
