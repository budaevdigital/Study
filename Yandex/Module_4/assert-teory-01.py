
# x = 3  
# Такой перенос строк всё испортит, при любом x утверждение вернёт True:
# assert (2 + x == 4, 'Очень длинная строка, в которой многословно '
# 					'и с лирическими отступлениями описывается, ' 
# 					'какой именно тест провален.')

def movie_quotes(name): 
	"""Возвращает цитаты известных персонажей из фильмов.""" 
	
	quotes = { 'Элли': 'Тото , у меня такое ощущение, что мы не в Канзасе!', 
			  'Шерлок': 'Элементарно, Ватсон!', 
			  'Дарт Вейдер': 'Я — твой отец.', 
			  'Thomas A. Anderson': 'Меня зовут Ханс. Ханс Кристиан Андерсен.',} 
	return quotes.get(name, 'Персонаж пока не известен миллионам.') 

# Утверждаем, что если в movie_quotes() передать 'Шерлок' - 
# функция вернёт 'Элементарно, Ватсон!'. 
assert movie_quotes('Шерлок') == 'Элементарно, Ватсон!', (
	"movie_quotes('Шерлок') не вернул ожидаемый результат!")
													
# Утверждаем, что если в movie_quotes() передать 'Thomas A. Anderson' - 
# функция вернёт 'Меня зовут Нео!'. 
assert movie_quotes('Thomas A. Anderson') != 'Меня. Зовут. Нео!', (
	"movie_quotes('Thomas A. Anderson') не вернул ожидаемый результат!") 

# Утверждаем, что если в movie_quotes передать 'Алиса Плезенс Лидделл' - 
# функция вернёт 'Всё чудесатее и чудесатее!'. 
expected_answer = 'Всё чудесатее и чудесатее!' 
assert movie_quotes('Алиса Плезенс Лидделл') == expected_answer, (
	"movie_quotes('Алиса Плезенс Лидделл') не вернул ожидаемый результат!")


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
			   f'категория: {self.age_define()}, '                
			   f'статус: {self.programmer_define()}')      
	
	def print_contact(self):         
		print(self.show_contact())


mike: Contact = Contact('Михаил Булгаков', 1891, False)  

expected_string = 'Михаил Булгаков, категория: Старейшина, статус: Нормальный'

assert mike.show_contact() == expected_string, 'Ошибка в Contact.show_contact()'