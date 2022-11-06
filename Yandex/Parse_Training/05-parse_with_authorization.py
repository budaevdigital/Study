import requests
from bs4 import BeautifulSoup

LOGIN_URL = "http://51.250.32.149/login/"

if __name__ == "__main__":
    cookie_data = {"username": "test_parser_user", "password": "testpassword"}
    # Создадим экземпляр класса Session (он сохраняет cookie с которым
    # будем работать)
    session = requests.Session()
    # Тут проходит АУТЕНТИФИКАЦИЯ, где получаем от сервера csrftoken в cookie
    response = session.get(LOGIN_URL)
    response.encoding = "utf-8"
    # print(session.cookies.get_dict()) # Это csrftoken в cookie
    soup = BeautifulSoup(response.text, features="lxml")
    # Тут парсим csrfmiddlewaretoken из формы для АВТОРИЗАЦИИ при парсинге
    token_tag = soup.find(name="input", attrs={"name": "csrfmiddlewaretoken"})
    token = token_tag["value"]
    # print(token) # Это csrfmiddlewaretoken из формы
    cookie_data["csrfmiddlewaretoken"] = token
    response = session.post(LOGIN_URL, data=cookie_data)
    response.encoding = "utf-8"
    print(response.status_code)
