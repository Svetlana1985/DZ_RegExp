# Задание №1
import re

# simple_word = input('Enter a words or text: ')
# pattern = r'\b[aA]\w+[^\s*\.,;:?!]'
# result = re.findall(pattern, simple_word)
# if re.findall(pattern, simple_word):
#     print(result)
# else:
#     print('Ошибка')

# # Задание №2
# simple_word = input('Enter a words or text: ')
# if 'new' in simple_word:
#     new_word = re.sub(r'new', 'old', simple_word)
#     print(new_word)
# else:
#     print('The text does not contain a word: "new"')

# Задание №3
import re
# str_1 = input('Введите текст: ')
# pattern = r'[-+]?\d+[^/s\.,;:!?]'
# if re.findall(pattern, str_1):
#     num = re.findall(pattern, str_1)
#     print(num)
# else:
#     print('В данной строке нет цифр')
    # Не получается правильно обработать события, то есть за цифру всегда цепляется следующая за ней буква или символ.

# Задание №4
import re
# num_tel = input('Введите номер телефона в формате "+X(XXX)XXX-XXXX": ')
# pattern = r'^\+\d\(\d{3}\)\d{3}-\d{4}$'
# if re.match(pattern, num_tel):
#     print('Номер введен верно')
# else:
#     print('Попробуйте еще раз')

#Задание #5
time_now = input('Введите время в формате "ЧЧ:ММ:СС": ')
pattern = r'^([0-2][0-3]\:[0-5][0-9]\:[0-5][0-9])$'
if re.match(pattern, time_now):
    print('Вермя введено верно')
else:
    print('Ошибка')