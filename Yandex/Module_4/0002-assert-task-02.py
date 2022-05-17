"""
2. Протестируйте методы programmer_define() и age_define() класса
Contact.

Тестировать нужно все состояния: в метод programmer_define() надо по 
очереди передать False и True, а в age_define() надо проверить все 
возрастные категории. 
Для проверки всех возможных вариантов создайте несколько экземпляров 
класса Contact с разными значениями полей year_birth и is_programmer.

Подсказка
----------
Создайте несколько экземпляров класса Contact, в каждом экземпляре 
задайте разные значения для year_birth и is_programmer.
Для каждого экземпляра напишите отдельный assert, вызывая проверяемый 
метод и сравнивая возвращаемое значение с ожидаемым.
"""


class Contact:
    def __init__(self, name, year_birth, is_programmer):
        self.name = name        
        self.year_birth = year_birth        
        self.is_programmer = is_programmer

    def age_define(self):
        if 1946 < self.year_birth < 1980:
            return 'Олдскул'
        if self.year_birth >= 1980:
            return 'Молодой'
        return 'Старейшина'

    def programmer_define(self):

        if self.is_programmer:
            return 'Программист'
        return 'Нормальный'

    def show_contact(self):
        return(f'{self.name}, '              
               f'возраст: {self.age_define()}, '
               f'статус: {self.programmer_define()}')

    def print_contact(self):
        print(self.show_contact())

# Создайте экземпляр класса Contact с необходимыми параметрами
# 'название переменной(экземпляра класса)' : 'тип переменной(класса)' = 'значение'
user_1: Contact = Contact('Михаил', 1800, False)
user_2 : Contact = Contact('Евгений', 1950, True)
user_3 : Contact = Contact('Дмитрий', 1989, True)
user_4 : Contact = Contact('Гвидо', 1956, True)
user_5 : Contact = Contact('Татьяна', 1988, False)

# Напишите assert, и в нём проверьте, 
# что метод programmer_define() этого экземпляра возвращает строку "Нормальный"
programmer_string_yes: str = 'Программист'
programmer_string_no: str = 'Нормальный'

# проверяем, является ли user3 программистом
assert user_3.programmer_define() == programmer_string_yes, (
    f'Ошибка в {user_3.programmer_define()=!s} отличается от {programmer_string_yes}')

# проверяем, не является ли user5 программистом
assert user_5.programmer_define() == programmer_string_no, (
    f'Ошибка в {user_3.programmer_define()=!s} отличается от {programmer_string_no}')


# Во втором assert проверьте, возвращает ли метод age_define() значение "Старейшина"
age_string_star: str = 'Старейшина'
age_string_old: str = 'Олдскул'
age_string_young: str = 'Молодой'

# проверям возрастную группу "Старейшина"
assert user_1.age_define() == age_string_star, (
    f'Ошибка в {user_1.age_define()=!s}. Не совпадает с возрастнгой группой - {age_string_star}')

# проверям возрастную группу "Олдскул"
assert user_4.age_define() == age_string_old, (
    f'Ошибка в {user_1.age_define()=!s}. Не совпадает с возрастнгой группой - {age_string_old}')

# проверям возрастную группу "Молодой"
assert user_3.age_define() == age_string_young, (
    f'Ошибка в {user_1.age_define()=!s}. Не совпадает с возрастнгой группой - {age_string_young}')

# Затем создайте другой экземпляр с другими параметрами
# И в assert проверьте, вернут ли и его методы ожидаемый результат.
# Заранее создал для этого экземпляр user_2
expected_string: str = 'Евгений, возраст: Олдскул, статус: Программист'
# проверяем вызов функции print_contact у пользователя user_2
assert user_2.show_contact() == expected_string, (
    f'Ошибка в {user_2.show_contact()!s}. Не соответствует значению - {expected_string}')

user_1.print_contact()
user_2.print_contact()
user_3.print_contact()
user_4.print_contact()
user_5.print_contact()

print('Тестирование пройдено!')