"""
1. Дано целое число. Если оно является положительным, то прибавить к нему 1;
в противном случае не изменять его. Вывести полученное число.
"""
def is_positive_num(num: int):
    if num > 0:
        num += 1

    return num    

n = int(input("Please enter your number: "))
print(is_positive_num(n))

"""
2. Даны три целых числа. Найти количество положительных чисел в исходном наборе.
"""
def count_positive_number():
    count = 1
    positive_num = 0

    while count <= 3:
        num = int(input(f"Please enter number {count}: "))
        if num > 0:
            positive_num += 1
        count += 1

    return f"Count of positive numbers is: {positive_num}"


print(count_positive_number())

#OR
# def count_positive_numbers():
#     positive = 0

#     for i in range(1, 4):
#         num = int(input(f"Please enter number {i}: "))
#         if num > 0:
#             positive += 1

#     return f"Count of positive numbers is: {positive}"


# print(count_positive_numbers())

"""
3.
# Дан номер года (положительное целое число).
# Определить количество дней в этом году.
# Обычный год — 365 дней.
# Високосный год — 366 дней.
# Год является високосным, если:
#   - делится на 4,
#   - но НЕ делится на 100,
#   - ИЛИ делится на 400.
# Примеры:
#   300, 1300, 1900 — НЕ високосные.
#   1200, 2000 — високосные.
"""

def count_number_days(year: int):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 366
    else:
        return 365

print(count_number_days(2000))

"""
4.
# Найти сумму всех натуральных чисел от A до B.
# Числа A и B вводятся пользователем.
# Гарантируется, что A <= B.
"""

def sum_from_a_to_b(num_a: int, num_b: int):
    total = 0

    for i in range(num_a, num_b + 1):
       total += i
       print(i)
    
    return total

num_a = int(input("Please enter number one: "))
num_b = int(input("Please enter number tow: "))
print(sum_from_a_to_b(3, 8))

"""
5.
# Найти произведение положительных чисел,
# а также сумму и количество отрицательных
# из 10 введённых целых значений.
# Ввод значений осуществляется через input().
"""

def analyze_numbers():
    product = 1
    count_negative_numbers = 0
    sum_negative = 0

    for i in range(1, 11):
        num = int(input(f"Please enter number {i}: "))
        if num > 0:
            product *= num
        elif num < 0:
            sum_negative += num
            count_negative_numbers += 1

    return (
        f"The product of positive numbers is {product}\n"
        f"The sum of negative numbers is {sum_negative}\n"
        f"The count of negative numbers is {count_negative_numbers}"
    )


print(analyze_numbers())

"""
6.
# Дано целое число N.
# Найти сумму всех его цифр.
# Пример:
#   N = 753 → 7 + 5 + 3 = 15
"""

def sum_digits(number):
    sum_numbers = 0

    while(number > 0):
        sum_numbers += number % 10
        number = number // 10

    return sum_numbers

print(sum_digits(753))    

"""
7.
# Даны площади S1 и S2.
# Каждый год S1 увеличивается в 2 раза, S2 увеличивается в 3 раза.
# Найти, через сколько лет площадь S1 станет меньше 10% от площади S2.
"""

def years_until_ten_percent(s1, s2):
    years = 0

    while True:
        s1 *= 2
        s2 *= 3
        years += 1

        if s1 < s2 * 0.1:
            break
        
    return years

print(years_until_ten_percent(10,10))

"""
1**2 + 9**2 = 82
8**2 + 2**2
6**2 + 8**2
1**2 + 0**2 + 0**2
"""
def sum_digits_with_add(number):
    sum_numbers = 0
    last_digits = 0

    while(number > 0):
        last_digits = number % 10
        sum_numbers += last_digits ** 2
        number = number // 10

    return sum_numbers


def is_lucky_number(number: int):
    seen = set()
    total_sum = sum_digits_with_add(number)

    while total_sum != 1 and total_sum not in seen:
        seen.add(total_sum)
        total_sum = sum_digits_with_add(total_sum)

    if total_sum == 1:
        return True
    return False


check_lucky_number = int(input("Please enter a number to check if it is lucky: "))
print(is_lucky_number(check_lucky_number))