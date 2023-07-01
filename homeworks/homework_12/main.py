from typing import TypeAlias
from student import Student
import json

LOADED_DCT: TypeAlias = dict[str, dict[str, dict[str, str]]]
SUBJECTS_FILE = 'subjects.csv'
DATA_SRC_FILE = 'students.json'


def loader(file_name: str) -> LOADED_DCT:
    with open(file_name, 'r', encoding='utf-8') as file_in:
        students_dict = json.load(file_in, parse_int=int)
    return students_dict


def gather_crowd(students_dict: LOADED_DCT) -> list[Student]:
    students_list = []
    for i_key, i_val in students_dict.items():
        try:
            if i_key.count(' ') != 2:
                raise ValueError(f'Неправильное имя студента: {i_key}')
            first_name, patronymic, second_name = i_key.split()
            tmp = Student(first_name, patronymic, second_name)
            tmp.marks = i_val['Предметы']
            tmp.tests = i_val['Тесты']
        except Exception as exc:
            print(f'\033[31m{exc.__class__.__name__}: {exc}\033[0m')
            continue
        students_list.append(tmp)
    return students_list


def main():
    result = gather_crowd(loader(DATA_SRC_FILE))
    for person in result:
        print(person)


if __name__ == '__main__':
    main()

