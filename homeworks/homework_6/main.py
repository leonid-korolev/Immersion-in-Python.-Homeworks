
from chess_module import eight_queens 
from input_coordinates import input_coord
from random_coordinates import random_coord


if __name__ == '__main__':
    #print(eight_queens(input_coord())) # input -> 1 7, 2 4, 3 2, 4 8, 5 6, 6 1, 7 3, 8 5  return -> True
    print(eight_queens(random_coord()))
