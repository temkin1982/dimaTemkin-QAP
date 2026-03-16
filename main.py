
import random


"""
Задача 1: привести числа -1.6 и 2.99 к целому типу

"""

first_num = -1.6
second_num = 2.99

first_num_int, second_num_int = int(first_num), int(second_num)

print(first_num_int, second_num_int)

"""
Задача 2: заменить символ "#" на символ "/" в строке "www.my_site.com/#about"

"""
before_str = "www.my_site.com#about"
after_str = before_str.replace('#', '/')

print(after_str)

"""
Задача 3: добавить "ing" к слову "stroka"

"""
word = "stroka"
new_word = word + "ing"

print(new_word)


"""
Задача 4: в строке "Ivanov Ivan" поменять местами слова => "Ivan Ivanov"Задача"

"""
name = "Ivanov Ivan"
name_after_change = name.split()
name = f'{name_after_change[1]} {name_after_change[0]}'
print(name)


"""
Задача 5: удалить пробелы в начале и в конце строки
"""

with_space_str = "  hello world  "
withOut_space = with_space_str.strip()

print(withOut_space)

"""
Задача 6: создать словарь school с количеством учеников в 10 разных классах

"""
school_dict = {f"{i}{j}": random.randint(21, 30)
               for i in range(1, 12)
               for j in "abcd"}
print(school_dict)
school_dict = {
    "1a": 22, 
    "1b": 24, 
    "2a": 22,
    "2b": 24,
    "3a": 23,
    "3b": 21,
    "4a": 19,
    "4b": 25,
    "5a": 27,
    "5b": 26
    }


"""
Задача 7: создать список и извлечь из него второй элемент

"""

number_list = [12, 32, 23, 45, 66, 45, 54]

print(number_list[1])

"""
Задача 8: вывести, входит ли строка 1 в строку 2 (пример: "employ" в "employment")

"""
employ = "employ"
employment = "employment"

print(employ in employment)

"""
Задача 9: Вывести нужные символы
x = "My name is Agent Smith"
print(x[?])      # y
print(x[?:?:?])  # nesgt

"""
x = "My name is Agent Smith"
print(x[1])
print(x[3:16:3])


"""
Задача 10*: найти число без пары в списке

"""

numbers = [1, 5, 2, 9, 2, 9, 1]

for n in numbers:
    if numbers.count(n) == 1:
        print(n)
        break

"""
OR

"""

numbers = [1, 5, 2, 9, 2, 9, 1]

result = 0
for n in numbers:
    result ^= n

print(result) 
    



