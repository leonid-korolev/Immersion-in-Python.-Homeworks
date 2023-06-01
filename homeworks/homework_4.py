'''
Напишите функцию для транспонирования матрицы
'''

def matrix_transposition(my_matrix: list) -> list:
    matrix_transp = [[0 for x in range(len(my_matrix))] for y in range(len(my_matrix[0]))]
    for i in range(len(my_matrix)):
        for j in range(len(my_matrix[0])):
            matrix_transp[j][i] = my_matrix[i][j]

    return matrix_transp

print(matrix_transposition([[1,2,3], [4,5,6], [7,8,9]]))


'''
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
где ключ - значение переданного аргумента, а значение - имя аргумента. 
Если ключ не хешируем, используйте его строковое представление.
'''

from collections.abc import Hashable

def parametres_to_dict(**kwargs) -> dict:
    my_dict = {}
    for key, item in kwargs.items():
        if not isinstance(item, Hashable):
            item = str(item)
        my_dict[item] = key

    return my_dict


print(parametres_to_dict(a=1, b=2, c=[3,4]))


