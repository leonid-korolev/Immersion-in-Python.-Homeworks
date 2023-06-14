'''
Напишите функцию группового переименования файлов. Она должна:
принимать параметр желаемое конечное имя файлов. При переименовании в конце имени 
добавляется порядковый номер.
принимать параметр количество цифр в порядковом номере.
принимать параметр расширение исходного файла. Переименование должно работать 
только для этих файлов внутри каталога.
принимать параметр расширение конечного файла.
принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] 
берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, 
если оно передано. Далее счётчик файлов и расширение.
'''

import os
from pathlib import Path

# end_name                   - параметр <желаемое конечное имя файлов>
# count_serial_number        - параметр <количество цифр в порядковом номере>
# source_file_extension      - параметр <расширение исходного файла>
# end_file_extension         - параметр <расширение конечного файла>
# range_original_name        - диапазон <сохраняемого оригинального имени>

def group_renaming_files(dir_path: str, end_name: str, count_serial_number: int, 
                            source_file_extension: str, end_file_extension: str, 
                            range_original_name: tuple):
       
    file_list = os.listdir( dir_path)
    
    
    file = ()
    f_count = 0

    for file in file_list:
        file_name, file_ext = file.split('.')         
        if file_ext != source_file_extension:
            continue
        else:
            file_ext = end_file_extension
            file_name = f'{file_name[range_original_name[0]:range_original_name[1]]}'
            file_name = f'{file_name + end_name}_{f_count + 1:0{count_serial_number}}{file_ext}'            
            f_count += 1
            print(f'{file} ->  {file_name}')
            os.rename(os.path.join(dir_path, file), os.path.join(dir_path, file_name))
    
    text = ''
    if f_count == 1:
        text = 'файл переименован по шаблону'
    elif f_count == 2 or f_count == 3 or f_count == 4:
        text = 'файла переименованы по шаблону'
    else:
        text = 'файлов переименованы по шаблону'

    return f'{f_count} {text} '
            


if __name__=='__main__':

    print(group_renaming_files('test_dir', end_name='_replacement', count_serial_number=2,\
             source_file_extension='txt', end_file_extension='.xls', range_original_name=(0,3)))
    
'''
result:
data.txt ->  dat_replacement_01.xls
file_01.txt ->  fil_replacement_02.xls
notepad.txt ->  not_replacement_03.xls
3 файла переименованы по шаблону
'''