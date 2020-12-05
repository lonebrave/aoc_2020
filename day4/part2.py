#!/usr/bin/env python
import re


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


def validate_byr(passport, debug=False):
    if 'byr' not in passport:
        if debug: print(f'INVALID(Missing byr): {passport}')
        return False
    if re.fullmatch(r'\d{4}', passport['byr']):
        year = int(passport['byr'])
        if year < 1920 or year > 2002:
            if debug: print(f'INVALID(byr outside of valid range): {passport}')
            return False
    return True


def validate_iyr(passport, debug=False):
    if 'iyr' not in passport:
        if debug: print(f'INVALID(Missing iyr): {passport}')
        return False
    if re.fullmatch(r'\d{4}', passport['iyr']):
        year = int(passport['iyr'])
        if year < 2010 or year > 2020:
            if debug: print(f'INVALID(iyr outside of valid range): {passport}')
            return False
    return True


def validate_eyr(passport, debug=False):
    if 'eyr' not in passport:
        if debug: print(f'INVALID(Missing eyr): {passport}')
        return False
    if re.fullmatch(r'\d{4}', passport['eyr']):
        year = int(passport['eyr'])
        if year < 2020 or year > 2030:
            if debug: print(f'INVALID(eyr outside of valid range): {passport}')
            return False
    return True


def validate_hgt(passport, debug=False):
    if 'hgt' not in passport:
        if debug: print(f'INVALID(Missing hgt): {passport}')
        return False
    if re.fullmatch(r'\d{3}cm', passport['hgt']):
        num = int(passport['hgt'][0:3])
        if not(num >= 150 and num <= 193):
            if debug: print(f'INVALID(hgt outside valid cm values): {passport}')
            return False
    elif re.fullmatch(r'\d{2}in', passport['hgt']):
        num = int(passport['hgt'][0:2])
        if not(num >= 59 and num <= 76):
            if debug: print(f'INVALID(hgt outside valid in values): {passport}')
            return False
    else:
        if debug: print(f'INVALID(hgt invalid): {passport}')
        return False
    return True


def validate_hcl(passport, debug=False):
    if 'hcl' not in passport:
        if debug: print(f'INVALID(Missing hcl): {passport}')
        return False
    if not re.fullmatch(r'#[0-9a-f]{6}', passport['hcl']):
        if debug: print(f'INVALID(hcl not valid): {passport}')
        return False
    return True


def validate_ecl(passport, debug=False):
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if 'ecl' not in passport:
        if debug: print(f'INVALID(Missing ecl): {passport}')
        return False
    if passport['ecl'] not in colors:
        if debug: print(f'INVALID(ecl not valid): {passport}')
        return False
    return True


def validate_pid(passport, debug=False):
    if 'pid' not in passport:
        if debug: print(f'INVALID(Missing pid): {passport}')
        return False
    if not re.fullmatch(r'\d{9}', passport['pid']):
        if debug: print(f'INVALID(pid does not match regex): {passport}')
        return False
    return True


def validate_passport(passport, debug=False):
    if not(validate_byr(passport, debug)):
        return False
    if not(validate_iyr(passport, debug)):
        return False
    if not(validate_eyr(passport, debug)):
        return False
    if not(validate_hgt(passport, debug)):
        return False
    if not(validate_hcl(passport, debug)):
        return False
    if not(validate_ecl(passport, debug)):
        return False
    if not(validate_pid(passport, debug)):
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
