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
###
#!/usr/bin/env python3
import argparse
import sys
import re
import os
mypar = argparse.ArgumentParser()
mypar.add_argument('-i', '--usrinput', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--value=', type = str, required = True, help = 'I hope this works')

args = mypar.parse_args()
#Try to parse through the file
value = args.value
for lin in open(args.usrinput):
    for value in lin:
        if not value in lin:
            continue
        sys.stdout.write(f'{lin}\n')
######
#!/usr/bin/env python3
import argparse
import sys
import re
import os
mypar = argparse.ArgumentParser()
mypar.add_argument('--source', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--value', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--attribute', type = str, required = True, help = 'I hope this works')
#mypar.add_argument('--attribute', type = str, required = True, help = 'I hope this works')

args = mypar.parse_args()
#Try to parse through the file
value = args.value
for lin in open(args.source):
    for word in lin:
        if not f'{args.value}' in lin:
            continue
        if not f'{args.attribute}' in lin:
            continue
        sys.stdout.write(f'{lin}\n')
####
#!/usr/bin/env python3
import argparse
import sys
import re
import os
mypar = argparse.ArgumentParser()
mypar.add_argument('-i', '--usrinput', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--value', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--attribute', type = str, required = True, help = 'I hope this works')

args = mypar.parse_args()
#Try to parse through the file
value = args.value
for lin in open(args.usrinput):
    for word in lin:
        if not f'{args.value}' in lin:
            continue
        if not f'{args.attribute}' in lin:
            continue
        sys.stdout.write(f'{lin}\n')

##
#!/usr/bin/env python3
import argparse
import sys
import re
import os
mypar = argparse.ArgumentParser()
mypar.add_argument('--source_gff', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--value', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--attribute', type = str, required = True, help = 'I hope this works')
#mypar.add_argument('--attribute', type = str, required = True, help = 'I hope this works')

args = mypar.parse_args()
#Try to parse through the file
value = args.value
for lin in open(args.source_gff):
    for word in lin:
        if not f'{args.value}' in lin:
            continue
        if not f'{args.attribute}' in lin:
            continue
        sys.stdout.write(f'{lin}\n')