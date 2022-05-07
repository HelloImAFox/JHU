#!/usr/bin/env python3
import argparse
import sys
mypar = argparse.ArgumentParser()
mypar.add_argument('--source_gff', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--value', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--attribute', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--type', type = str, required = True, help = 'I hope this works')

args = mypar.parse_args()
#Try to parse through the file
value = args.value
for lin in open(args.source_gff):
    for word in lin:
        if not f'{args.value}' in lin:
            continue
        if not f'{args.attribute}' in lin:
            continue
        line = lin.split('\t')
        if not line[2] == f'{args.type}':
            continue
        sys.stdout.write(f'{lin}\n')