from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
from sqlalchemy import Column, create_engine, String, Integer
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()


class Pep(Base):
    __tablename__ = "pep"

    id = Column(Integer, primary_key=True)
    type_status = Column(String(2))
    number = Column(Integer, unique=True)
    title = Column(String(200))
    authors = Column(String(200))


if __name__ == "__main__":
    # Зададим константу - URL по которому будем парсить данные
    URL_PEP = "https://peps.python.org/#numerical-index"
    engine = create_engine("sqlite:///sqlalchemy_pep.db")
    # Создаём модели в БД
    Base.metadata.create_all(engine)
    sessions = Session(engine)
    response = requests.get(URL_PEP)
    # Не забываем указывать дополнительный пакет для работы с данными - lxml
    soup = BeautifulSoup(response.text, features="lxml")
    section_soup = soup.find(name="section", attrs={"id": "numerical-index"})
    tablebody_soup = section_soup.find("tbody")
    tr_soups = tablebody_soup.find_all("tr")
    # Сделаем красивый прогресс-бар с tqdm
    for tr_soup in tqdm(
        tr_soups, desc="Парсинг и запись в БД", colour="magenta"
    ):
        status_pep = tr_soup.find("td").text[1:]
        number_pep = int(tr_soup.find("td").find_next_sibling().text)
        title_pep = (
            tr_soup.find("td").find_next_sibling().find_next_sibling().text
        )
        author_pep = (
            tr_soup.find("td")
            .find_next_sibling()
            .find_next_sibling()
            .find_next_sibling()
            .string
        )
        pep = Pep(
            type_status=status_pep,
            number=number_pep,
            title=title_pep,
            authors=author_pep,
        )
        sessions.add(pep)
    sessions.commit()
