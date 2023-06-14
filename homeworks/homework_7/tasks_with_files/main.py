from pathlib import Path
from feel_numbers import feel_numbers
from gen_names import name_gen
from two_files_in_one import two_files_in_one
from gen_files import gen_files
from renaming_files import group_renaming_files

if __name__ == '__main__':
    #feel_numbers(3, 'file_1.txt')
    #name_gen(10, 4, 7, Path('name_gen'))
    #two_files_in_one('file_1.txt', 'name_gen', 'result.txt')
    #gen_files('bin', 5, 10, 1024, 4096, 5)
    print(group_renaming_files('test_dir', end_name='_replacement', count_serial_number=2,\
             source_file_extension='txt', end_file_extension='.xls', range_original_name=(0,3)))