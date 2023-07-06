'''
Задача из ДЗ №4
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
'''

from collections.abc import Hashable


def parametres_to_dict(**kwargs) -> dict:
    """
    >>> print(parametres_to_dict(a=1, b=2, c=3))
    {1: 'a', 2: 'b', 3: 'c'}
    >>> print(parametres_to_dict(a=1, b=2, c=[3, 4]))
    {1: 'a', 2: 'b', '[3, 4]': 'c'}
    """
    my_dict = {}
    for key, item in kwargs.items():
        if not isinstance(item, Hashable):
            item = str(item)
        my_dict[item] = key

    return my_dict

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)



