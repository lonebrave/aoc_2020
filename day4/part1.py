#!/usr/bin/env python

def parse_passports(data):
    passports = list()
    passport = ''
    for line in data:
        if line.strip() == '':
            passport_dict = dict()
            fields = passport.split()
            for field in fields:
                k, v = field.split(':')
                passport_dict[k] = v
            passports.append(passport_dict)
            passport = ''
        else:
            passport = passport + ' ' + line.strip()
    return passports


def validate_passport(passport, debug=False):
    if 'byr' not in passport:
        if debug: print(f'INVALID(Missing byr): {passport}')
        return False
    if 'iyr' not in passport:
        if debug: print(f'INVALID(Missing iyr): {passport}')
        return False
    if 'eyr' not in passport:
        if debug: print(f'INVALID(Missing eyr): {passport}')
        return False
    if 'hgt' not in passport:
        if debug: print(f'INVALID(Missing hgt): {passport}')
        return False
    if 'hcl' not in passport:
        if debug: print(f'INVALID(Missing hcl): {passport}')
        return False
    if 'ecl' not in passport:
        if debug: print(f'INVALID(Missing ecl): {passport}')
        return False
    if 'pid' not in passport:
        if debug: print(f'INVALID(Missing pid): {passport}')
        return False
    if debug: print(f'VALID: {passport}')
    return True


filename = 'day4/input.txt'
# filename = 'day4/example.txt'

with open(filename) as file:
    lines = file.readlines()

lines.append('')

passports = parse_passports(lines)
valid_count = 0
for passport in passports:
    if validate_passport(passport):
        # print(f'VALID: {passport}')
        valid_count = valid_count + 1
    # else:
    #     print(f'INVALID: {passport}')

print(f'{valid_count} valid passports')
