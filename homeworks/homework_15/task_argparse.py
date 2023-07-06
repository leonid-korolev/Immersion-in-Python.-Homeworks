import argparse


parser = argparse.ArgumentParser(description='')
parser.add_argument('numbers', metavar='N', type=float, nargs=2)
args = parser.parse_args()
print(f'Переданы значения: {args}')
