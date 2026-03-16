
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