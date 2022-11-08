# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YatubeParsingItem(scrapy.Item):
    # Для дополнительно валидации, опишем модели
    author = scrapy.Field()
    text = scrapy.Field()
    date = scrapy.Field()
