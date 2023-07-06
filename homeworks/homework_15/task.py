"""
Возьмите любые 1-3 задачи из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров.

"""
"""
Задача из семинара 10

Создайте класс прямоугольник. Класс должен принимать длину
и ширину при создании экземпляра. У класса должно быть два метода,
возвращающие периметр и площадь. Если при
создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
"""
from task_error import RectangleValueError
import logging


FORMAT = "{levelname:<8} - {asctime}: {msg}"
logging.basicConfig(format=FORMAT, style="{", filename='task.log', level=logging.INFO, encoding="UTF-8")
logger = logging.getLogger(__name__)


class Rectangle:
    def __init__(self, side1: int, side2: int = None):
        self.side1 = side1
        self.side2 = side2 if side2 is not None else side1
        if self.side2 == side1:
            logger.info(f'Задана одна сторона. Считаем, что вторая равна первой, получили квадрат.')

        if self.side1 > 0 and self.side2 > 0:
            logger.info(f'Заданы стороны: {self.side1}, {self.side2}')
            return

        else:
            logger.error(
            f'Заданы стороны: {self.side1}, {self.side2}. '
            f'Прямоугольник может быть создан только со сторонами\n положительной длины.'
            )
            raise RectangleValueError(side1, side2)

    def square(self) -> int:
        return self.side2 * self.side1


    def perimetr(self) -> int:
        return 2 * (self.side1 + self.side2)


if __name__ == '__main__':

#    rect1 = Rectangle(5, -10)
    rect2 = Rectangle(10)

#    print(f"{rect1.square()=}, {rect1.perimetr() =} ")
    print(f"{rect2.square()=}, {rect2.perimetr() =} ")


