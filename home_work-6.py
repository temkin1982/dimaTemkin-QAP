from typing import Callable
import warnings
from functools import wraps


"""
1. Напишите рекурсивную функцию palindrome(s),
которая проверяет, является ли строка палиндромом.
Без срезов и reversed(), только рекурсия.
"""


def isPal(word):
    def helper(left, right):
        if left >= right:
            return True

        if word[left] != word[right]:
            return False

        return helper(left + 1, right - 1)

    return helper(0, len(word) - 1)


print(isPal("level"))
print(isPal("hello"))
print(isPal("racecar"))
print(isPal("abca"))


"""
2. Напишите функцию make_validator(min_val, max_val),
 которая возвращает функцию-валидатор. 
 Валидатор принимает число и возвращает True если оно в диапазоне, иначе False.
"""


def make_validator(min_val: int, max_val: int) -> Callable[[int], bool]:
    def validator(num: int) -> bool:
        if num < min_val or num > max_val:
            return False
        return True

    return validator


v = make_validator(1, 10)

print(v(5))  # True
print(v(0))  # False
print(v(10))  # True
print(v(11))  # False

"""
3. Напишите декоратор @retry(n), 
который при возникновении любого исключения повторяет вызов функции до n раз. 
Если все попытки провалились — пробрасывает последнее исключение
"""


def retry(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            last_error = None

            while n > attempts:
                try:
                    result = func(*args, **kwargs)
                    print(result)
                    return result
                except Exception as e:
                    last_error = e
                    attempts += 1
                    with open("errors.log", "a") as f:
                        f.write(str(e) + "\n")
                    continue

            raise last_error

        return wrapper

    return decorator


@retry(3)
def func(): ...


"""
4. Напишите декоратор @deprecated(message), 
который выводит предупреждение при вызове функции (через warnings.warn) 
и всё равно выполняет её. Сохраняйте метаданные через functools.wraps.
"""


def deprecated(message):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(message, category=DeprecationWarning)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@deprecated("This function is deprecated, please use the new version!")
def old_function():
    print("Working as usual")


old_function()

"""
5. Напишите рекурсивную функцию binary_search(lst, target) (бинарный поиск числа в списке), 
оберните её декоратором @logger, который логирует каждый вызов с параметрами.
"""


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        print(f"  args: {args}")
        print(f"  kwargs: {kwargs}")
        return func(*args, **kwargs)

    return wrapper


@logger
def binary_search(lst, target):
    def search(left, right):
        if left > right:
            return -1

        mid = (left + right) // 2

        if lst[mid] == target:
            return mid
        elif target < lst[mid]:
            return search(left, mid - 1)
        else:
            return search(mid + 1, right)

    return search(0, len(lst) - 1)


print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([10, 20, 30, 40], 25))
