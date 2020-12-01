#!/usr/bin/env python

with open('input') as file:
    lines = file.readlines()

values = [int(line) for line in lines]

for index,num1 in enumerate(values):
    subtotal=2020-num1
    for _,num2 in enumerate(values,start=index+1):
        if num2 < subtotal:
            num3=subtotal-num2
            if num3 in values:
                print(f'{num1} * {num2} * {num3} = {num1*num2*num3}')
                break
    else:
        continue
    break
