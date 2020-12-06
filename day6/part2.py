#!/usr/bin/env python
from pprint import pprint


# DEBUG = True
DEBUG= False


def parse_form_data(data, debug=False):
    groups = list()
    group = list()

    for line in data:
        if line.strip() == '':
            if debug: print(group)
            groups.append(group)
            group = list()
        else:
            group.append({char for char in line.strip()})
    
    # Handle last line if not empty
    if debug: print(group)
    groups.append(group)

    return groups


filename = 'day6/input.txt'
# filename = 'day6/example.txt'
with open(filename) as file:
    data = file.readlines()

groups = parse_form_data(data, debug=DEBUG)

if DEBUG:
    print('== GROUPS ==')
    pprint(groups)

counts = 0
for group in groups:
    intersection = set.intersection(*group)
    if DEBUG:
        print('== INTERSECTION ==')
        pprint(intersection)
        # break
    counts += len(intersection)

print(f'Sum of counts is {counts}.')
