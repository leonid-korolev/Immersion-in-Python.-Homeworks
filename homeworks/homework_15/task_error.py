class RectangleException(Exception):
    pass


class RectangleValueError(RectangleException):
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return f'Прямоугольник может быть создан только со сторонами положительной длины.'
