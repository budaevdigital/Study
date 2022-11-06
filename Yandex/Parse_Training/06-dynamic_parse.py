from sqlalchemy.util.langhelpers import attrsetter
from requests_html import HTMLSession
from bs4 import BeautifulSoup


if __name__ == "__main__":
    URL = "https://httpbin.org"
    # Создадим сессию, через которую будут переправлять все запросы
    session = HTMLSession()
    response = session.get(URL)
    soup = BeautifulSoup(response.html.html, "lxml")
    swagger = soup.find(attrs={"id": "swagger-ui"})
    print(swagger.prettify())
