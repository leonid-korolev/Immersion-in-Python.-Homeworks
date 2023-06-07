'''
Вспомните какие модули вы уже проходили на курсе. 
Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).
'''
# import math as mh
# from random import random as rnd
# import sys as s

'''
Создайте модуль с функцией внутри. 
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток. 
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток. 
Функция выводит подсказки “больше” и “меньше”. 
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
'''
# Сергей Ерёмкин
# def game_random(down: int, up: int, count: int):
#     for i in range(count+1):
#         comp_answer = random.randint(down, up)
#         user_input = input(f'Введите число от {down} - {up}')
#         if comp_answer == user_input:
#             return True
#             break
#     return False





# if __name__=='__main__':

#    # _, *arg = argv

#     gen.gen_fnc(*(int(i) for i in argv[1:]))

#     #gen.gen_fnc(10, 20, 5)



#Андрей Сапунов
import generate as gen
from sys import argv
import task

import task_7


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # _, *arg = argv

    # puzzle_dict = {
    # "Не лает не кусает, в дом не пускает.": ["замок", "замочек", "засов"],
    # "Красна девица, а коса на улице" : ["морковь", "морковка"],
    # "два кольца, два конца, в середине гвоздик": ["ножницы"],
    # }

    # nt.new_puzzle(puzzle_dict, 3)
    # nt.show_result()



    # try_count = task.puzzle("Не лает не кусает, в дом не пускает.", ["замок", "замочек", "засов"], 3)
    # if try_count:
    #     print(f"Угадано за {try_count} раза")
    # else:
    #     print("Не угадали (")



    # gen.gen_fnc(*(int(i) for i in argv[1:]))

    # # gen.gen_fnc(10, 20, 5)

    data = '12.01.1999'
    print(task_7.date_validator(data))