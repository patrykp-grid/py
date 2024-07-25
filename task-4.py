#!/usr/bin/env python3.12

import argparse

parser = argparse.ArgumentParser(description='This is a characters in word counter')

parser.add_argument('word', type=str, help='The word to count characters in')

args = parser.parse_args()

word_dict = {}

for char in args.word:
    if char in word_dict:
        word_dict[char] += 1
    else:
        word_dict[char] = 1

print(word_dict)
