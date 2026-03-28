import os

from datetime import datetime
from file_utils import read_lines, write_lines, count_words
from typing import Callable
from zoneinfo import ZoneInfo

"""
1. Напиши функцию copy_file(source: str, destination: str) -> bool которая читает содержимое файла source и записывает его в destination. 
Возвращает True если успешно. Проверь что файл-копия создался.
"""

def copy_file(source: str, destination: str) -> bool:
    if not os.path.exists(source):
        return False
    
    with open(source, 'r') as f:
        data = f.read()

    with open(destination, "w") as f:
        f.write(data)    

    
    return os.path.exists(destination)

    """
    or
    
    with open("newfile.txt", "w") as f:
         f.write("Hello")

    shutil.copy("newfile.txt", "new_destination.txt")     
    """
result = copy_file("source.txt", "destination.txt")
print(result)
print(open("destination.txt").read())

"""
2. Создай файл grades.txt где каждая строка содержит имя студента и его оценку через запятую:
Анна,85
Иван,72
Петр,91
Напиши код который читает файл и добавляет в конец каждой строки статус: 
'отлично' если оценка >= 90, 'хорошо' если >= 75, иначе 'удовлетворительно'. Сохрани результат в новый файл grades_with_status.txt.
"""

with open("grades.txt", "w") as f:
    f.write("Anna,85\n")
    f.write("Ivan,72\n")
    f.write("Pitar,91\n")

with open("grades.txt", "r") as file:
    with open("grades_with_status.txt", 'w') as out:
            for line in file:
                try:
                    if ',' not in line:
                        print(f"Invalid line, skipping:{line}")
                        continue

                    name, grade = line.strip().split(",")
                    grade = int(grade)
                    if grade >= 90:
                        status = "Great"
                    elif grade >= 75:
                        status = "Good"
                    else:
                        status = "satisfactorily"

                    out.write(f"{name},{grade} = {status}\n")  
                except:
                    print(f"Invalid line, skipping:{line}")
                    continue         

print(open("grades_with_status.txt").read())


"""
3. Напиши функцию age_calculator(birth_date_str: str) -> int 
которая принимает дату рождения в формате 'dd/mm/yyyy' (input)  и возвращает полных лет.
"""

def age_calculator(birth_date_str: str) -> int:
    birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")

    date_now = datetime.now(ZoneInfo("Asia/Jerusalem"))

    age = date_now.year - birth_date.year

    if (date_now.month, date_now.day) < (birth_date.month, birth_date.day):
        age -= 1


    return age


birth_date = input("Enter your birth date in the format dd/mm/yyyy: ")
print(age_calculator(birth_date))


"""
4.Напиши модуль file_utils.py с тремя полностью аннотированными функциями:

def read_lines(filename): ...
def write_lines(filename, lines): ...
def count_words(filename): ... # count_words считает сколько раз каждое слово встречается в файле и возвращает словарь.
В main.py импортируй и протестируй все три.
"""


# 1. Создаём тестовый файл
write_lines("test.txt", [
    "Hello world\n",
    "Hello Dima\n",
    "Python is great\n"
])

# 2. Читаем строки
lines = read_lines("test.txt")
print("Lines from file:")
print(lines)

# 3. Считаем слова
words = count_words("test.txt")
print("\nWord count:")
print(words)


"""
5. Напиши функцию password_checker(correct_password) 
которая возвращает вложенную функцию check(password). 
Вложенная принимает пароль и возвращает True если совпадает, иначе False.
"""



def password_checker(correct_password: str) -> Callable[[str], bool]:
    user_password = correct_password

    def check(password: str) -> bool:
        return user_password == password
    
    return check

checker = password_checker("qwerty")
print(checker("qwerty"))
print(checker("12345"))


