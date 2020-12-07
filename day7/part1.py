#!/usr/bin/env python
import re
from pprint import pprint


def parse_rules(rule_list, debug=False):
    rules = dict()
    for line in rule_list:
        if debug: print(f'Rule: {line}')

        # Split into outer bag and inner bag(s)
        outin = line.split(' bags contain ')
        outer = outin[0]
        if debug: print(f'Outer bag: {outer}')

        # Split inner bag(s)
        regex = r'(?P<count>\d+) (?P<color>\w+ \w+) bag'
        inner = outin[1].split(', ')
        inner_dict = dict()
        for bag in inner:
            # if debug: print(bag)
            match = re.match(regex, bag)
            if match:
                inner_dict[match.group('color')] = match.group('count')
        rules[outer] = inner_dict
        if debug: print(rules['outer'])
    return rules


filename = 'day7/example.txt'
# filename = 'day7/input.txt'

with open(filename) as file:
    data = file.readlines()

# rules = parse_rules(data, debug=True)
rules = parse_rules(data)
pprint(rules)
