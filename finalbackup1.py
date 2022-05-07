#Currently working
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
    lin.rstrip()
    print(lin)
######
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
    lin.strip()
    for word in lin:
        if not 'ID=YAR003W' in lin:
            continue