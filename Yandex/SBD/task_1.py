"""
Саша разрабатывает игру «Отгадай слово». В этой игре, 
игрок должен отгадать загаданное слово из N букв за несколько попыток.

В данный момент перед Сашей стоит задача написать логику 
проверки величины совпадения попытки игрока с загаданным словом.

Более формально, пусть есть строка 
S — загаданное слово и строка 
Q — попытка игрока. Обе строки имеют одинаковую длину N. 

Для каждой позиции 1≤i≤N строки Q, нужно вычислить тип совпадения в этой позиции со строкой S.

Если Qi=Si, то в позиции i тип совпадения должен быть равен correct.

Если Qi≠Si, но существует другая позиция 1≤j≤N, такая что Qi=Sj, 
то в позиции i тип совпадения должен быть равен present.

-   Каждую букву строки S можно использовать не более чем в одном совпадении типа correct или present.
-   Приоритет всегда отдается типу correct.
-   Из всех возможных вариантов использования в типе present программа Саши выбирает самую левую позицию в строке Q.

В остальных позициях тип совпадения должен быть равен absent.

## Формат ввода

В первой строке задана строка S (1≤∣∣S∣∣≤106) — загаданное слово.

Во второй строке задана строка Q (|Q|=|S|) — попытка игрока.

Гарантируется, что строки S и Q содержат только заглавные латинские буквы.

## Формат вывода

Выведите N строк. В строке i должна находиться одна из строк correct, present или absent — результат совпадения в позиции i строки Q со строкой S.
"""

# quess_word = input().upper()
# user_word = input().upper()

# if len(quess_word) == len(user_word):
#     for i in range(len(quess_word)):
#         if quess_word[i] == user_word[i]:
#             print('correct')
#         elif user_word[i] in quess_word and i != (len(quess_word)-1):
#             print('present')
#         else:
#             print('absent')

quess_word = input().upper()
user_word = input().upper()

letter_is_used = [False] * len(quess_word)

for i in range(len(quess_word)):
    letter_is_find = False
    if quess_word[i] == user_word[i]:
        print('correct')
        letter_is_used[i] = True
    elif quess_word[i] != user_word[i]:
        for l in range(len(quess_word)):
            if quess_word[l] == user_word[i] and quess_word[l] != user_word[l] and not letter_is_used[l] and i != (len(quess_word)-1):
                print('present')
                letter_is_used[l] = False
                letter_is_find = True
                break
        if not letter_is_find:
            print('absent')
