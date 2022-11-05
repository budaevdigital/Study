# Задача
# При помощи метода session.query() определите в базе данных количество объектов модели Pep,
# у которых значение поля status равно 'Active'.
#
# Напечатайте в консоли полученное число.
#
# Подсказка
# - Создайте объект сессии для работы с ORM.
# - Используйте метод сессии query(), а также методы filter() и count()
#       для получения нужного результата.
# - Обратите внимание на синтаксис фильтрации элементов:
#       указывается атрибут модели, затем пишется нужное выражение, например, равенство.


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

    # Закомментил, т.к. модели в базе уже созданы
    # with Session(engine) as session:
    #     session.begin()
    #     try:
    #         session.add(pep8)
    #         session.add(pep20)
    #         session.add(pep216)
    #     except:
    #         session.rollback()
    #         raise WriteBaseError("Не удалось сделать запись в БД")
    #     else:
    #         session.commit()

    search_result = (
        Session(engine).query(Pep).filter(Pep.status == "Active").count()
    )
    print(search_result)
    print(type(search_result))
