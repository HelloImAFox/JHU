#!/usr/bin/env python3
import argparse
import sys
mypar = argparse.ArgumentParser()
mypar.add_argument('--source_gff', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--value', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--attribute', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--type', type = str, required = False, help = 'I hope this works')
newlist = []
args = mypar.parse_args()
blah = str(f'{args.attribute}={args.value}')
#Try to parse through the file
for line in open(args.source_gff):
    if line.startswith('C'):
        newlist.append(line)


print(newlist[0:10])
