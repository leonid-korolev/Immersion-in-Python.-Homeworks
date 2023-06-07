import random as rnd

def gen_fnc(low: int = 1, hight: int = 50, try_count: int = 5) -> bool:
    result = False
    num = rnd.randint(low, hight + 1)

    serch_count = 0
    while serch_count < try_count:
        ask_value = int(input(f"Введите число от {low} до {hight}: "))
        if ask_value == num:
            print("Вы угадали")
            result = True
            break
        if ask_value < num:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")
        serch_count += 1
    else:
        print("Попытки закончились")

    return result