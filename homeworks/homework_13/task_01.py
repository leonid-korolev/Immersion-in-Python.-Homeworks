"""
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации. Поднимайте исключения внутри основного кода.
Например нельзя создавать прямоугольник со сторонами отрицательной длины.

"""
"""
Задача из семинара 10

Создайте класс прямоугольник. Класс должен принимать длину
и ширину при создании экземпляра. У класса должно быть два метода,
возвращающие периметр и площадь. Если при
создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
"""

from task_error import RectangleValueError


class Rectangle:
    def __init__(self, side1: int, side2: int = None):
        self.side1 = side1
        self.side2 = side2 if side2 is not None else side1
        if self.side1 > 0 and self.side2 > 0:
            return
        else:
            raise RectangleValueError(side1, side2)

    def square(self) -> int:
        return self.side2 * self.side1

    def perimetr(self) -> int:
        return 2 * (self.side1 + self.side2)


if __name__ == '__main__':
    rect1 = Rectangle(5, -10)
    rect2 = Rectangle(10)

    print(f"{rect1.square()=}, {rect1.perimetr() =} ")
    print(f"{rect2.square()=}, {rect2.perimetr() =} ")
