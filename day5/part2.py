#!/usr/bin/env python


def parse_boarding_pass(boarding_pass, debug=False):
    if debug: temp_pass = boarding_pass
    boarding_pass = boarding_pass.replace('F', '0')
    boarding_pass = boarding_pass.replace('B', '1')
    boarding_pass = boarding_pass.replace('L', '0')
    boarding_pass = boarding_pass.replace('R', '1')

    row = int(boarding_pass[0:7], 2)
    column = int(boarding_pass[7:], 2)

    if debug: print(f'{temp_pass}: row {row}, column {column}, seat ID {(row * 8) + column}')

    return {'row': row, 'column': column, 'seat_id': (row * 8) + column}


filename = 'day5/input.txt'
# filename = 'day5/example.txt'

with open(filename) as file:
    passes = file.readlines()

boarding_passes = list()
for line in passes:
    # boarding_passes.append(parse_boarding_pass(line.strip(), debug=True))
    boarding_passes.append(parse_boarding_pass(line.strip()))

highest = 0
for line in boarding_passes:
    if line['seat_id'] > highest:
        highest = line['seat_id']

print(f'Highest seat ID: {highest}')

seats = sorted([boarding_pass['seat_id'] for boarding_pass in boarding_passes])

for index, seat in enumerate(seats):
    if seat == seats[index + 1] - 2:
        print(f'My seat is {seat + 1}')
        break
