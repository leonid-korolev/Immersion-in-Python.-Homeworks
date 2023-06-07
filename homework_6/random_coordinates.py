from random import randint
from chess_module import eight_queens 

def random_coord():
    n = 8
    x = []
    y = []
    i = 0
    result = 0
    while i < n:    
        new_x = randint(1,n) 
        new_y = randint(1,n)
        if new_x  in x or new_y in y:
            continue
        else:
            x.append(new_x)
            y.append(new_y) 
            print(f'[{new_x}, {new_y}]')
        i += 1 
    
     
    return x,y

