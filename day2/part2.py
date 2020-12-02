#!/usr/bin/env python
from pprint import pprint

with open('day2/input.txt') as file:
    passwords = file.readlines()

valid = 0
for line in passwords:
    fields = line.strip().split()
    first, second = fields[0].split('-')
    first = int(first) - 1
    second = int(second) - 1
    letter = fields[1][0]
    password = fields[2]

    if (password[first] == letter) ^ (password[second] == letter):
        valid = valid + 1
print(f'{valid} valid passwords')
