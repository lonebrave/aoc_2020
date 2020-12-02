#!/usr/bin/env python
from pprint import pprint

with open('day2/input.txt') as file:
    passwords = file.readlines()

valid = 0
for line in passwords:
    fields = line.strip().split()
    minimum, maximum = fields[0].split('-')
    minimum = int(minimum)
    maximum = int(maximum)
    letter = fields[1][0]
    password = fields[2]

    if (password.count(letter) >= minimum) and (password.count(letter) <= maximum):
        valid = valid + 1
print(f'{valid} valid passwords')
