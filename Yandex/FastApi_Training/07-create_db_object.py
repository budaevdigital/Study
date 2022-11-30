"""
Вы заступили на вахту программистом на сверхсекретной базе.
Никакой связи с миром нет: есть только зашифрованный радиоканал, но дешифратор не работает.

Допишите программу, которая будет обрабатывать входящие сообщения,
декодировать их (сам декодер уже написан) и сохранять в БД в таблице
news (якобы сохранять: в задании это делать не нужно).

Вот пример входящего сообщения:
{
  "title": "1053-1086-1074-1072-1103-32-1074-1077-1088-1089-1080-1103-32-1103-1079-1099-1082-1072-32-80-121-116-104-111-110-33",
  "message": "1042-1085-1091-1082-32-1043-1091-1080-1076-1086-32-1074-1072-1085-32-1056-1086-1089-1089-1091-1084-1072-32-1087-1088-1077-1076-1089-1090-1072-1074-1080-1083-32-1087-1086-1095-1090-1077-1085-1085-1077-1081-1096-1077-1081-32-1087-1091-1073-1083-1080-1082-1077-32-80-121-116-104-111-110-32-52-46-48"
}

В комментариях описано, что нужно сделать в той или иной части программы.
"""


from fastapi import FastAPI
from pydantic import BaseModel, Field
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


app = FastAPI()
Base = declarative_base()


class SecretMessage(BaseModel):
    # Опишите Pydantic-схему для зашифрованных сообщений.
    # Все поля - обязательные.
    title: str = Field(..., min_length=1)
    message: str = Field(..., min_length=1)


class ReadyNews(Base):
    # Опишите модель SQLAlchemy для хранения данных в БД.
    # Дополнительных классов создавать не нужно.
    # Таблицу назовите `news`, в ней должен быть столбец id.
    __tablename__ = "news"
    id = Column(Integer, primary_key=True)
    title = Column(String())
    message = Column(String())


def decoder(data: dict[str, str]) -> dict[str, str]:
    """
    Сверхсекретный декодер.
    Здесь всё работает, ничего менять не надо!
    """
    decoded_data = {}
    for key, value in data.items():
        decoded_str = (chr(int(chunk)) for chunk in value.split("-"))
        decoded_data[key] = "".join(decoded_str)
    return decoded_data


@app.post("/super-secret-base")
def reciever(encoded_news: SecretMessage):

    # Передайте сообщение в декодер.
    decoder_news = decoder(encoded_news).dict()

    # Создайте переменную ready_news - объект класса ReadyNews
    # из дешифрованного сообщения.
    # В параметры передаём пары "ключ=значение", для этого распаковываем словарь.
    ready_news = ReadyNews(**decoder_news)
    # Здесь мог бы быть код, сохраняющий сообщение в базу данных,
    # но его писать не надо.

    # Эндпоинт возвращает объект класса ReadyNews.
    # Здесь ничего менять не надо.
    return ready_news
