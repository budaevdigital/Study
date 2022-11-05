# Задача
# Во всех записях, у которых status == 'Active', замените значение поля status на 'Final'.
# Примените изменения к БД. Подсчитайте общее количество записей со статусом 'Final'.
#
# Полученное число напечатайте в консоли.
#
# Подсказка
# В методе update() используется словарь, где в качестве ключа указывается поле, которое нужно обновить


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
        return f"PEP {self.pep_number} {self.name} {self.status}"


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
            session.query(Pep).filter(Pep.status == "Active").update(
                {"status": "Final"}
            )
        except:
            session.rollback()
            raise WriteBaseError("Не удалось удалить запись в БД")
        else:
            session.commit()
            print(session.query(Pep).filter(Pep.status == "Final").count())
            print(session.query(Pep).all())
