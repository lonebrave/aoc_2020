#!/usr/bin/env python

with open('input') as file:
    lines = file.readlines()

values = set([int(line) for line in lines])

for num in values:
    num2=2020-num
    if num2 in values:
        print(f'{num} * {num2} = {num*num2}')
        break
