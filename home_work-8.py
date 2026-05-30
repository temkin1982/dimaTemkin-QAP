import math
from dataclasses import dataclass
from typing import Iterator

"""
1. Создай класс Circle с protected атрибутом _radius.
Добавь @property для radius (с проверкой: радиус > 0),
и вычисляемые свойства area и perimeter через @property - они должны пересчитываться автоматически при изменении радиуса.
"""


class Circle:
    def __init__(self, num_radius: float) -> None:
        self._radius = num_radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Radius must be greater than 0")
        self._radius = value

    @property
    def area(self) -> float:
        return math.pi * self._radius**2

    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self._radius

    def __str__(self) -> str:
        return f"Circle with radius {self._radius}"

    def __repr__(self) -> str:
        return f"Circle(radius={self._radius})"


c = Circle(10)

print("Radius:", c.radius)
print("Area:", c.area)
print("Perimeter:", c.perimeter)

print("\nChecking __str__:")
print(c)  # calls __str__

print("\nChecking __repr__:")
print(repr(c))  # calls __repr__

print("\nChanging radius to 5:")
c.radius = 5
print("New radius:", c.radius)
print("New area:", c.area)
print("New perimeter:", c.perimeter)

print("\nTrying to set radius to 0 (should raise an error):")
try:
    c.radius = 0
except ValueError as e:
    print("Error:", e)

"""
2. Создай класс Vector с атрибутами x и y. 
Реализуй магические методы __add__ (сложение двух векторов), 
__str__ (вывод в формате "Vector(x, y)"), 
и __eq__ (сравнение). Проверь: Vector(1, 2) + Vector(3, 4) должен давать Vector(4, 6).
"""


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        sum_x = self.x + other.x
        sum_y = self.y + other.y

        return Vector(sum_x, sum_y)

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)

print(Vector(1, 2) == Vector(1, 2))  # True
print(Vector(1, 2) == Vector(2, 3))  # False

print(Vector(10, 20))


"""
3. Создай класс Temperature с @property для celsius, fahrenheit и kelvin. 
При установке значения через любое свойство должны автоматически пересчитываться остальные. 
Хранить следует только одно внутреннее значение.
"""


class Temperature:
    def __init__(self, celsius: float) -> None:
        # Храним только Цельсий как внутреннее значение
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        # Просто возвращаем внутреннее значение
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        # При установке нового значения — сохраняем его
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        # Переводим Цельсий в Фаренгейт
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> float:
        # Переводим Фаренгейт в Цельсий и сохраняем
        self._celsius = (value - 32) * 5 / 9

    @property
    def kelvin(self) -> float:
        # Переводим Цельсий в Кельвин
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value: float) -> None:
        # Переводим Кельвин в Цельсий и сохраняем
        self._celsius = value - 273.15


t = Temperature(0)
print(t.fahrenheit)  # 32
print(t.kelvin)  # 273.15

t.fahrenheit = 212
print(t.celsius)  # 100

t.kelvin = 0
print(t.celsius)  # -273.15

"""
Используй @dataclass для создания класса Point с полями x: float и y: float. 
Добавь метод distance_to(other: Point) - расстояние до другой точки. 
Затем создай дочерний @dataclass класс Point3D, добавив поле z: float, и переопредели distance_to.
"""


@dataclass
class Point:
    x: float
    y: float

    def distance_to(self, other: "Point") -> float:
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx * dx + dy * dy)


@dataclass
class Point3D(Point):
    z: float

    def distance_to(self, other: "Point3D") -> float:
        dx = other.x - self.x
        dy = other.y - self.y
        dz = other.z - self.z
        return math.sqrt(dx * dx + dy * dy + dz * dz)


p1 = Point(0, 0)
p2 = Point(3, 4)
print(p1.distance_to(p2))  # 5.0

a = Point3D(0, 0, 0)
b = Point3D(1, 2, 2)
print(a.distance_to(b))  # 3.0


"""
Создай класс-итератор Countdown, который при итерации возвращает числа от start до 0. 
Реализуй __iter__ и __next__ (при исчерпании бросай StopIteration). Проверь в цикле for и через list().
"""


class Countdown:
    def __init__(self, start: int) -> None:
        self.current = start

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.current < 0:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1

        return value


c = Countdown(5)
for i in c:
    print(i)

print(list(Countdown(5)))

c = Countdown(2)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
