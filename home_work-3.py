import math_utils as m
"""
1. Напиши код который выведет таблицу умножения до 10 на N 
(введенное с клавиатуры) в таком формате
  3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 27
"""

def print_multiplication_table(num: int) -> str:
    res = " | ".join(str(i * num) for i in range(1, 10))
    return res

    # or:
    # for i in range(1, 10):
    #     print(i * num, end=" | ")


num = int(input("Please enter a number: "))
print(print_multiplication_table(num))

# print_multiplication_table(num)

"""
2. Попроси пользователя ввести имя и возраст. 
Выведи фразу: «Через 10 лет тебе будет <X> лет, <ИМЯ>!»
"""
def tell_future_age(name: str, age: int) -> str:
    res = f"Через 10 лет тебе будет {age + 10} лет, {name}!"
    return res

name = input("What is your name? ")
age = int(input("How old are you? "))
print(tell_future_age(name=name, age=age))


"""
3. Даны два списка цен в долларах и курс валюты. 
Используй map чтобы перевести все цены в рубли. 
Затем используй zip чтобы создать словарь {товар: цена_в_рублях}:

items = ['хлеб', 'молоко', 'кофе']
prices_usd = [1.5, 2.0, 8.0]
rate = 3.2
"""

def get_items_prices_in_rub(product_items: list, prices: list):
    rate = 3.2
    prices_rub = list(map(lambda p: p * rate, prices))

    return dict(zip(product_items, prices_rub))



product_items = ['bread', 'milk', 'coffee']
prices_usd = [1.5, 2.0, 8.0]  

print(get_items_prices_in_rub(product_items, prices_usd))

"""
4. Напиши функцию fizzbuzz(n) которая принимает число и возвращает строку: 
'Fizz' если делится на 3, 'Buzz' если делится на 5, 'FizzBuzz' если делится на оба, иначе само число в виде строки. 
Вызови её для чисел от 1 до 20 через map.
"""

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)

result = list(map(fizzbuzz, range(1,21))) 
print(result)   

"""
5. Напиши функцию *args с именем my_stats которая принимает любое
 количество чисел и возвращает сразу три значения — минимум, максимум и среднее.
"""

def my_stats(*args):
    min_num = min(args)
    max_num = max(args)
    avg = sum(args) / len(args)

    return f"The minimum number is {min_num}, the maximum number is {max_num}, and the average is {avg}"

print(my_stats(1, 5, 10, 20))

"""
6. Напиши функцию build_profile(**kwargs) 
которая принимает любые именованные аргументы и возвращает словарь
 с этими данными плюс автоматически добавляет ключ 'registered': True. Добавь к функции docstring.
"""

def build_profile(**kwargs):
    """
    Build a user profile from any named arguments.
    Automatically adds the key 'registered': True.
    Returns a dictionary with all profile data.
    """
    profile = kwargs.copy()
    profile["registered"] = True
    return profile

print(build_profile(name='Dima', age=44, city='Akko'))


"""
7. Создай модуль math_utils.py с тремя функциями: square(n) — возводит в квадрат, 
cube(n) — возводит в куб, is_even(n) — возвращает True/False. 
В main.py импортируй модуль, попроси пользователя ввести число через input, 
примени все три функции и выведи результаты. Защити вызовы конструкцией if __name__ == "__main__".
"""

if __name__ == "__main__":
    
    n = int(input("Please enter your number: "))
    print(m.square(n))
    print(m.cube(n))
    print(m.is_even(n))
