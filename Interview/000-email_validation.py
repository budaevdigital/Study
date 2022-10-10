"""
Функция проверяет email и приводит его к нужному формату, чтобы не возникало
дублей при регистрации пользователей, например 
"""

from typing import Tuple

list_email = {"ya": "yandex", "yandex-team": "yandex-team", "gm": "gmail"}


def to_lower_replace_email(string: str, list_email: Tuple[str, ...]) -> str:
    email_user = string.lower()
    domain = email_user.split("@")[0]
    tech_email = email_user.split("@")[1].split(".")[0]
    # Если будут использоваться домены 3-го уровня, то можно организовать проверку
    # на длину массива split по точке '.'
    domain_zone = email_user.split(".")[1]
    if tech_email in list_email:
        tech_email = tech_email.replace(tech_email, list_email[tech_email])
    return domain + "@" + tech_email + "." + domain_zone


assert (
    to_lower_replace_email("SDHwehs@gm.com", list_email) == "sdhwehs@gmail.com"
), "Функция проверки технического емайла работает не корректно!"

print(to_lower_replace_email("YAndex@yandex-team.com", list_email))
