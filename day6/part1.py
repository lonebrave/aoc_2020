#!/usr/bin/env python
from pprint import pprint


# DEBUG = True
DEBUG= False


def parse_form_data(data, debug=False):
    groups = list()
    answers = set()
    for line in data:
        if line.strip() == '':
            if debug: print(answers)
            groups.append(answers)
            answers = set()
        else:
            for char in line.strip():
                answers.add(char)
    # Handle last line if not empty
    if debug: print(answers)
    groups.append(answers)
    answers = set()

    return groups


filename = 'day6/input.txt'
# filename = 'day6/example.txt'
with open(filename) as file:
    data = file.readlines()

groups = parse_form_data(data, debug=DEBUG)

if DEBUG: pprint(groups)

counts = 0
for group in groups:
    counts += len(group)

print(f'Sum of counts is {counts}.')
