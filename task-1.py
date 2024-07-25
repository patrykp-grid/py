#!/usr/bin/env python3.12

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the file to find extention of')

pargs = parser.parse_args()

if(len(pargs.filename.split('.')) < 2):
	raise Exception('No extension found')

print(pargs.filename.split('.')[-1])
