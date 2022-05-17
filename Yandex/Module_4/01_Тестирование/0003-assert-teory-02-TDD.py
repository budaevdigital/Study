# Тестирующая функция принимает на вход тестируемую функцию 
def test_invert(invertaser):     
	"""Тест алогритма инвертирования строки."""
	     
	# Напечатать информацию о тесте из docstring     
	print(f'{test_invert.__doc__}') 
	     
	# Напечатать имя тестируемой функции     
	print(f'Тестирование алгоритма {invertaser.__name__}')
	      
	source = 'Попугай'
	inversed = 'йагупоП'
	  
	# Проверяем утверждение, что вызов invertaser('Попугай')     
	# вернёт строку 'йагупоП'     
	# В сообщении об ошибке указываем название тестируемой функции     
	# и инвертируемую строку     
	assert invertaser(source) == inversed, (         
		f'Алгоритм в {invertaser.__name__} работает неправильно '         
		f'сo строкой "{source}" ')

	# Следующий тест: передадим в тестируемую функцию пустую строку     
	source = ''     
	# Ожидаемый результат работы тестируемой функции: пустая строка     
	inversed = '' 
	     
	# Проверяем утверждение: вызов функции с пустой строкой вернёт     
	#  пустую строку     
	assert invertaser(source) == inversed, (         
		f'Алгоритм {invertaser.__name__} работает неправильно с пустой строкой')
		
	# Если ислючение в assert не сработало -     
	# на экран будет выведено сообщение об успешном прохождении теста     
	print(f'Тест для {invertaser.__name__} пройден успешно')


# Ниже - несколько функций, инвертирующих строку. 
# Их и будем тестировать. 
def recursion_invertor(text):     
	"""Инвертирует строчку рекурсивно."""     
	if len(text) == 0:         
		return text     
	return recursion_invertor(text[1:]) + text[0]  

def slice_invertor(text):     
	"""Инвертирует строчку срезом."""     
	return text[::-1]  
	
def iterator_invertor(text):     
	"""Инвертирует строчку обратной итерацией."""     
	return ''.join(reversed(text))  
	
def reverselist_invertor(text):     
	"""Инвертирует строчку переворотом списка."""     
	inversed_list = list(text)     
	inversed_list.reverse()     
	return ''.join(inversed_list)  


# Вызов тестирующей функции для каждой функции-инвертора
test_invert(recursion_invertor) 
test_invert(slice_invertor) 
test_invert(iterator_invertor) 
test_invert(reverselist_invertor)


# Проверка самого теста с помощью заведомо нерабочей функции
def unworked_sort(array):     
	"""Функция не делает ничего."""     
	...

# Если тест словит ошибку, значит с ним всё впорядке
test_invert(unworked_sort)