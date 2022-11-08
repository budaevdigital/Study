"""
Этот паук должен найти все страницы групп http://51.250.32.185/
и для каждой группы вернуть словарь из трёх полей:
 - group_name — название группы,
 - description — описание группы,
 - posts_count — количество записей в группе (в числовом формате).

Результат парсинга сохраните в файл groups.csv.
"""

import scrapy


class GroupSpider(scrapy.Spider):
    name = "group"
    URL = "51.250.32.185"
    allowed_domains = [URL]
    start_urls = [f"http://{URL}"]

    def parse(self, response):
        # Спарсим все группы со страницы и передадим их в другой меитод
        # Для дальнейшего парсинга описания групп
        # Ссылку группы можно также извлечь так: "a.group_link::attr(href)"
        all_groups = response.css("a[href^='/group/']")
        # Каждую ссылку будет обрабатывать в цикле
        # response.follow() не пропустит дубли ссылок
        for group in all_groups:
            yield response.follow(group, callback=self.parse_group)

        next_page = response.css("a:contains('Следуюшая')::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_group(self, response):
        # Здесь парсим страницу описания группы
        yield {
            "group_name": response.css("h2::text").get().strip(),
            "description": response.css("p.group_descr::text").get().strip(),
            # Спарсим количество статей:
            # избавимся от ненужных символов и преобразуем тип
            "posts_count": int(
                response.css("div.h6::text")
                .get()
                .strip()
                .replace("Записей: ", "")
            ),
        }
