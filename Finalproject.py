#!/usr/bin/env python3
import argparse
import sys
import re
import os
mypar = argparse.ArgumentParser()
mypar.add_argument('-i', '--usrinput', type = str, required = True, help = 'I hope this works')
args = mypar.parse_args()
#Try to parse through the file
for lin in open(args.usrinput):
    for word in lin:
        if not 'Parent=YAR003W' in lin:
            continue
        else:
            print(lin)

        #if not 'CDS' in lin:
         #   continue
        #print(lin)