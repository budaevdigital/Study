# Задача
# Удалите все записи со статусом 'Rejected' (не забудьте применить изменения к БД)
# и подсчитайте количество оставшихся записей.
#
# Полученное число напечатайте в консоли.
#
# Подсказка
# Для операций, которые изменяют данные (вставка, обновление, удаление), необходимо использовать метод commit(),
# иначе изменения не запишутся.
# Даже если query() выдаёт правильный результат, записи в БД не изменятся, пока не выполнен коммит.
# Подсчитать все объекты можно, применив метод count() прямо к методу query().

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import declarative_base, declared_attr, Session


class WriteBaseError(Exception):
    """Класс служащий для отлова ошибок записи в БД"""


# Класс, на основе которого создаётся декларативная база,
# называют так же, как и сам класс декларативной базы
class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class Pep(Base):
    pep_number = Column(Integer, unique=True)
    name = Column(String(200))
    status = Column(String(20))

    # метод repr будет вызван, только если метод str не определён
    def __repr__(self) -> str:
        return f"PEP {self.pep_number} {self.name}"


if __name__ == "__main__":
    engine = create_engine("sqlite:///sqlite_pep.db", echo=False)
    # Аналог миграции - создаём таблицы из моделей унаследованных от Base
    # При последующих миграциях, лучше использовать библиотеку Alembic
    Base.metadata.create_all(engine)

    pep8 = Pep(
        pep_number=8, name="Style Guide for Python Code", status="Active"
    )
    pep20 = Pep(pep_number=20, name="The Zen of Python", status="Active")
    pep216 = Pep(pep_number=216, name="Docstring Format", status="Rejected")

    with Session(engine) as session:
        session.begin()
        try:
            session.query(Pep).filter(Pep.status == "Rejected").delete()
        except:
            session.rollback()
            raise WriteBaseError("Не удалось удалить запись в БД")
        else:
            session.commit()
            print(session.query(Pep).count())
