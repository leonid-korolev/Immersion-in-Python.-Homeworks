

def input_coord():
    n = 8
    x = []
    y = []
    print('Введите координаты восьми ферзей через пробел: ')
    for i in range(n):
        print(f'{i+1} -> ',end='')  
        new_x, new_y = [int(s) for s in  input().split()]
        x.append(new_x)
        y.append(new_y)

    return x,y