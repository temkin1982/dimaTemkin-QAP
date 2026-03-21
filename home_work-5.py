from typing import List

"""
1. Используя filter() и lambda, 
отфильтруйте из списка [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] только нечетные числа.
"""

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers_list))

print(odd_numbers)


"""
2. Напишите функцию apply_operations(numbers, *operations), 
которая принимает список чисел и произвольное количество lambda-функций, 
последовательно применяя каждую ко всему списку.
"""

def apply_operations(numbers: list, *operations) -> List[int]:

    for op in operations:
        numbers = op(numbers)

    return numbers    

print(apply_operations(
    [1, 2, 3],
    lambda nums: [x * 2 for x in nums],
    lambda nums: [x + 1 for x in nums]
))

"""
3. Напишите генератор chunked(lst, size), 
который разбивает список на куски заданного размера и поочередно их выдает.
Например, chunked([1,2,3,4,5], 2) → [1,2], [3,4], [5].
"""

from typing import Iterator, List

def chunked(lst: list, size: int) -> Iterator[List[int]]:
    i = 0
    while i < len(lst):
        yield lst[i:i + size]
        i += size


lst = [1, 2, 3, 4, 5]
size = 2
print(list(chunked(lst, size)))

"""
4. Напишите генератор prime_numbers(), 
который бесконечно генерирует простые числа. Выведите первые 20.
"""

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_numbers() -> Iterator[List[int]]:
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


gen = prime_numbers()
result = [next(gen) for _ in range(20)]
print(result)


"""
5. Напишите функцию safe_convert(value, type_func), 
которая пытается преобразовать value с помощью переданной функции (например, int, float). 
При ошибке возвращает None.
"""
from typing import Any, Callable


def safe_convert(value: Any, type_func: Callable) -> Any | None:
    try:
        result = type_func(value)
        return result
    except Exception:
        return None

print(safe_convert("123", int))
print(safe_convert("3.14", float))
print(safe_convert("abc", int))
print(safe_convert("10.5", int))
print(safe_convert(123, str))  


"""
6. Создайте собственный класс исключения NegativeNumberError. 
Напишите функцию sqrt_safe(n), которая считает квадратный корень из числа, 
но при отрицательном n выбрасывает NegativeNumberError с понятным сообщением.
"""
import math

class NegativeNumberError(Exception):
    pass

def sqrt_safe(n: int) -> int:
    if n < 0:
        raise NegativeNumberError("Cannot take the square root of a negative number")
    
    return  math.sqrt(n)


print(sqrt_safe(9))
print(sqrt_safe(0))
print(sqrt_safe(-5))


"""
7. Напишите функцию-калькулятор calculator(a, b, op), 
где op — строка ("+", "-", "*", "/"). 
Обработайте все возможные исключения: деление на ноль, неизвестная операция, некорректные типы аргументов.
"""

def calculator(a: float, b: float, op: str) -> float:

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments 'a' and 'b' must be numbers")

    if op not in ["+", "-", "*", "/"]:
        raise ValueError(f"Unknown operation: {op}")

    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero is not allowed")


print(calculator(10, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(10, 5, "*"))
print(calculator(10, 5, "/"))

calculator(10, 0, "/")

calculator(10, 5, "%")

calculator("abc", 5, "+")
