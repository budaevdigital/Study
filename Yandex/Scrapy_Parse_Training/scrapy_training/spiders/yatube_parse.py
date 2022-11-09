"""
спарсить все страницы блога, из каждой записи получить имя автора,
полный текст публикации и дату публикации;
ключами словаря должны быть author, text и date.

Для анализа страницы и поиска нужных CSS или XPath-селекторов
используйте Scrapy Shell.

Результаты парсинга сохраните в файл django.csv.

Чтобы в полученных данных не было лишних символов перевода строки и пробелов,
обязательно примените к полученному тексту метод .strip().

Например, для поста с третьей страницы сайта в вашем csv-файле должна быть
создана такая запись (на её примере вы можете проверить полноту данных):

@ostryak,"10 мая. 12 часов. Полночь. Торжок. Сегодня поутру собирались. Пообедали, взяли Лаврова с собой и поехали в Торжок.",10.05.1856

"""

import scrapy
from scrapy_training.items import YatubeParsingItem


class YatubeParseSpider(scrapy.Spider):
    # Имя паука должно быть уникальным в рамках одного проекта
    name = "yatube_parse"
    URL = "51.250.32.185"
    # Задаём ограничение на домен, чтобы парсер не пошёл по внешним ссылка
    allowed_domains = [URL]
    start_urls = [f"http://{URL}/"]

    def parse(self, response):
        for body in response.css("div.card-body"):
            # Для начала нужно спарсить "сырой" текст
            text_parse = body.css("p.card-text::text").getall()
            edit_list = []
            for row in text_parse:
                # Здесь избавиться от символов перевода строк \ n
                # и лишних пробелов в списке
                edit_list.append(row.strip())
            # Преобразуем подготовленный список в строку
            result_text = "".join(edit_list)
            data = {
                # Парсим автора
                "author": body.css("strong.d-block::text").get(),
                "text": result_text,
                # Парсим дату
                "date": body.css("small.text-muted::text").get(),
            }
            yield YatubeParsingItem(data)
        # Ищем ссылку на сл. страницу
        next_page = response.css("a:contains('Следующая')::attr(href)").get()
        if next_page is not None:
            # Описываем задачу для планировщика response.follow()
            # Если ссылка есть, то загружаем страницу
            # И вызываем метод parse ещё раз
            yield response.follow(next_page, callback=self.parse)
