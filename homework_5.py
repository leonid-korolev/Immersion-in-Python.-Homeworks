'''
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''
import os.path


def file_path_split(abs_path):
    path, name = os.path.split(abs_path )
    name, extension = os.path.splitext(name)

    return path, name, extension,

file_path = r"C:\Users\leonk\Desktop\log.txt"

if os.path.exists(file_path):             # Проверка существования пути к файлу
    print(file_path_split(file_path))     # ('C:\\Users\\leonk\\Desktop', 'log', '.txt')
else:
    print('Файл не найден')



'''
Напишите однострочный генератор словаря, который принимает на вход три списка 
одинаковой длины: имена str, ставка int, премия str с указанием процентов вида 
“10.25%”. В результате получаем словарь с именем в качестве ключа и суммой премии 
в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии
'''

names = ['Иванов', 'Петров', 'Сидоров']
salary = [5000, 8000, 10000]
prize = ['2.5%', '1.5%', '5%']

print({names[i]: salary[i] + salary[i] * (float(prize[i][:-1]) / 100) for i in range(len(names))})




'''
Создайте функцию генератор чисел Фибоначчи (см. Википедию)
'''

def fibonacci(n):
    result = [0, 1]
    while n > 0:
        yield result[-1]
        result.append(result[-1] + result[-2])
        n -= 1

for i in fibonacci(int(input('Введите длину ряда: '))):
    print(i)



