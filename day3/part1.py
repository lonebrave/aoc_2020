#!/usr/bin/env python

with open('day3/input.txt') as file:
    trees = [line.strip() for line in file.readlines()]

num_rows = len(trees)
num_col = len(trees[0])
row = 0
col = 0

SPACE = '.'
TREE = '#'

num_trees = 0

print(f'{num_rows} Rows')
print(f'{num_col} Columns')

while row < num_rows:
    str_position = col % num_col
    if trees[row][str_position] == TREE:
        num_trees = num_trees + 1
        print(f'{row},{col}[{str_position}] ({trees[row][str_position]}) = TREE')
    else:
        print(f'{row},{col}[{str_position}] ({trees[row][str_position]}) = SPACE')

    row = row + 1
    col = col + 3

print(f'We hit {num_trees} trees.')
