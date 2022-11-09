# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy import create_engine, Column, Integer, String, Text, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import datetime as dt

from scrapy.exceptions import DropItem

Base = declarative_base()


class MondayPost(Base):
    __tablename__ = "mondaypost"

    id = Column(Integer, primary_key=True)
    author = Column(String(50))
    date = Column(Date)
    text = Column(Text)


class ScrapyTrainingPipeline:
    def open_spider(self, spider):
        # Создаём движок алхимии
        engine = create_engine("sqlite:///sqlite.db")
        # Создадим разметку таблиц под модели
        Base.metadata.create_all(engine)
        # Создаём сессию, как атрибут объекта
        self.session = Session(engine)

    def process_item(self, item, spider):
        post_date = dt.datetime.strptime(item["date"], "%d.%m.%Y")
        # Запишем в БД только посты, которые были сделаны в Понедельник (0)
        if post_date.weekday() == 0:
            post = MondayPost(
                author=item["author"], date=post_date, text=item["text"]
            )
            self.session.add(post)
            self.session.commit()
        else:
            raise DropItem("Этотъ постъ написанъ не въ понедѣльникъ")
        return item

    def close_spider(self, spider):
        self.session.close()
