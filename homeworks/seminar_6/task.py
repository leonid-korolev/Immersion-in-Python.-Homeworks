'''
Создайте модуль с функцией внутри. 
Функция получает на вход загадку, список с возможными вариантами отгадок и количество
 попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, 
если попытки исчерпаны
'''

def puzzle(text: str, answears: list[str], try_count:int) -> int:
    print(text)
    count_trying = 1

    while count_trying <= try_count:
        answear = input("Что это? ")
        if answear in answears:
            break
        if count_trying != try_count:
            print("Не угадали, пробуем еще раз")
        count_trying += 1
    else:
        count_trying = 0

    return count_trying