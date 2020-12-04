#!/usr/bin/env python

def count_trees(trees, right=1, down=1):
    num_rows = len(trees)
    num_col = len(trees[0])
    row = 0
    col = 0

    SPACE = '.'
    TREE = '#'

    num_trees = 0

    # print(f'{num_rows} Rows')
    # print(f'{num_col} Columns')

    while row < num_rows:
        str_position = col % num_col
        if trees[row][str_position] == TREE:
            num_trees = num_trees + 1
        #     print(f'{row},{col}[{str_position}] ({trees[row][str_position]}) = TREE')
        # else:
        #     print(f'{row},{col}[{str_position}] ({trees[row][str_position]}) = SPACE')

        row = row + down
        col = col + right

    return num_trees


with open('day3/input.txt') as file:
    trees = [line.strip() for line in file.readlines()]

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
answer = 1
for r, d in slopes:
    count = count_trees(trees, right=r, down=d)
    answer = answer * count
    print(f'Slope {r} right, {d} down: We hit {count} trees.')
    
print(f'Answer: {answer}')
