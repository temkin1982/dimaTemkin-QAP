from typing import List, Any

"""
1. Создай класс Library с атрибутом класса books = [] и методами add_book(title),
remove_book(title) и show_books(). Продемонстрируй, что список книг общий для всех объектов класса.
"""


class Library:
    books = []

    def add_book(self, title: str) -> None:
        Library.books.append(title)

    def remove_book(self, title: str) -> None:
        Library.books.remove(title)

    def show_books(self) -> List[str]:
        return Library.books


lib1 = Library()
lib1.add_book("Harry Potter")
lib2 = Library()

print(lib2.show_books())


"""
2. Создай иерархию: базовый класс Employee с атрибутами name и salary, методом get_info().
 Дочерние классы Manager (добавляет department) и Developer (добавляет language). Каждый переопределяет get_info().
"""


class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def get_info(self) -> str:
        return f"Employee: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str) -> None:
        super().__init__(name, salary)
        self.department = department

    def get_info(self) -> str:
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"


class Developer(Employee):
    def __init__(self, name: str, salary: float, language: str) -> None:
        super().__init__(name, salary)
        self.language = language

    def get_info(self) -> str:
        return (
            f"Developer: {self.name}, Salary: {self.salary}, Language: {self.language}"
        )


m = Manager("Alex", 5000, "Sales")
d = Developer("Dima", 6000, "Python")

print(m.get_info())
print(d.get_info())


"""
3. Реализуй класс Stack (стек) с протектед атрибутом _items = [] 
и методами push(item), pop(), peek() (посмотреть верхний элемент), is_empty() и size().
"""


class Stack:
    def __init__(self) -> None:
        self._items = []

    def push(self, item: Any) -> None:
        self._items.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            item = self._items.pop()
            return item

    def peek(self) -> Any:
        return self._items[-1]

    def is_empty(self) -> bool:
        return not self._items

    def size(self) -> int:
        return len(self._items)


"""
4. Создай класс Vehicle с методом move(), выводящим "Moving...". 
Создай дочерние классы Car, Boat и Plane, каждый переопределяет move() по-своему. 
Напиши функцию start_journey(vehicle), которая вызывает move() у любого переданного транспорта - продемонстрируй полиморфизм.
"""


class Vehicle:
    def move(self) -> None:
        print("Moving.....")


class Car(Vehicle):
    def move(self) -> None:
        print("Moving Car")


class Boat(Vehicle):
    def move(self) -> None:
        print("Moving Boat")


class Plane(Vehicle):
    def move(self) -> None:
        print("Moving Plane")


def start_journey(vehicle) -> None:
    vehicle.move()


car = Car()
start_journey(car)


"""
5. Создай класс Student с атрибутами name и grades (список оценок). 
Добавь методы add_grade(grade), average() (средняя оценка), highest() и lowest(). Защити grades через одиночное подчёркивание.
"""


class Student:
    def __init__(self, name: str) -> None:
        self.name = name
        self._grades = []

    def add_grade(self, grade: int) -> None:
        self._grades.append(grade)

    def average(self) -> float:
        count_grades = len(self._grades)
        sum_all_grades = 0
        if count_grades == 0:
            return 0
        else:
            for grade in self._grades:
                sum_all_grades += grade

        return sum_all_grades / count_grades

    def highest(self) -> int | None:
        if len(self._grades) == 0:
            return None

        return max(self._grades)

    def lowest(self) -> int | None:
        if len(self._grades) == 0:
            return None

        return min(self._grades)


s = Student("Dima")
s.add_grade(90)
s.add_grade(75)
s.add_grade(100)

print(s.average())
print(s.highest())
print(s.lowest())


s2 = Student("Alex")
print(s2.average())
print(s2.highest())
print(s2.lowest())
