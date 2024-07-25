#!/usr/bin/env python3.12

import argparse

parser = argparse.ArgumentParser(description='List handler')

parser.add_argument('list', metavar='list', type=int, nargs='+', help='List of strings')

args = parser.parse_args()

fixed_list = tuple(sorted(set(args.list)))

min_value = min(fixed_list)
max_value = max(fixed_list)

print(f'List: {fixed_list}')
print(f'Minimum: {min_value}')
print(f'Maximum: {max_value}')

