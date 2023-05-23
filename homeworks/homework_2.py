'''
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное 
строковое представление. 
Функцию hex используйте для проверки своего результата.
'''
while True:
    try:
        result = ''
        N = int(input('Введите целое число: '))
        hex_string = hex(N)
        
        
        if N < 0:
            N *= -1       
        while N >= 1:
            res = N % 16
            result += str(res)
            N = N // 16
        
        print(f'Шестнадцатеричное  представление - {result[::-1]}, {hex_string} ')
        break
    except:
        print('Неверный ввод')



'''
Напишите программу, которая принимает две строки вида
“a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму
и произведение* дробей. Для проверки своего кода используйте модуль fractions.
'''

import math
from fractions import Fraction
import re

frac_1 = str(input('Введите первую робь вида "a/b": '))
frac_2 = str(input('Введите вторую робь вида "c/d": '))
print()
# Проверка с помощью модуля fractions 
a = Fraction(frac_1)
b = Fraction(frac_2)
print('Решение с использованием модуля fraction')
print(f"{a} + {b} = {a + b}")
print(f"{a} * {b} = {a * b}")
print()

print('Моё решение')
frac_1 = re.split('/', frac_1)
frac_2 = re.split('/', frac_2)
#print(frac_1)
#print(frac_2)
i = 0
while i < len(frac_1):
   frac_1[i] = int(frac_1[i])
   frac_2[i] = int(frac_2[i])
   i += 1


# Сложение дробей
nod = math.gcd(frac_1[1], frac_2[1])

if frac_1[1] == frac_2[1]:
   numerator = frac_1[0] + frac_2[0]
   denominator = frac_1[1]
else:
   numerator = (frac_1[0] * (frac_2[1]/nod)) + (frac_2[0] * (frac_1[1]/nod))
   denominator = nod * (frac_1[1]/nod) * (frac_2[1]/nod)
result = f'{int(numerator)} / {int(denominator)}'
#print(result)

nod_1 = math.gcd(int(numerator), int(denominator))
numerator = numerator // nod_1
denominator = denominator//nod_1
if numerator == denominator:
   print('Сумма дробей = 1')
else:
    print(f'Сумма дробей = {int(numerator)}/{int(denominator)}')

# Произведение* дробей
mult_numerator = frac_1[0] * frac_2[0]
mult_denominator = frac_1[1] * frac_2[1]
nod_2 = math.gcd(int(mult_numerator), int(mult_denominator))
mult_numerator = mult_numerator // nod_2
mult_denominator = mult_denominator // nod_2
print(f'Произведение дробей = {int(mult_numerator)}/{int(mult_denominator)}')






