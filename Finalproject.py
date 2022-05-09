#!/usr/bin/env python3
import argparse
import sys
import re
mypar = argparse.ArgumentParser()
#setting up the parser arguments
mypar.add_argument('--source_gff', type = str, required = True, help = 'Enter your source .gff')
mypar.add_argument('--value', type = str, required = True, help = 'Enter value e.g. YAR003W')
mypar.add_argument('--attribute', type = str, required = True, help = 'Enter attribute e.g. ID, Parent')
mypar.add_argument('--type', type = str, required = True, help = 'Enter type e.g. gene')
args = mypar.parse_args()
#values for use in
blah = str(f'{args.attribute}={args.value}')
blah1 = str(f'{args.type}')
list0 =[]
list1 =[]
list2 =[]
for line in open(args.source_gff):
    list0.append(line)
    if line.startswith('c'):
        list1.append(line)
new = [z for z in list1 if blah in z]
if len(new) == False:
    print("I'm sorry you may have entered something incorrectly. Please re-run the program and try again")
    quit()
new1 = [x for x in new if blah1 in x]
#print(str(new1))
if len(new1) == False:
    print("I'm sorry that type is not valid. Please re-run the program and try again")
    quit()
#put FASTA into a list
for all in list0:
    q = re.findall(r'^[A:G:T:C][ATGC]{10,100}', all)
    list2.append(q)
#trying to clean up the FASTA list and make it a single string, findall creates a list so I have lists in lists
fullstring = ' '.join(str(myitems) for myitems in list2)
fullstring1 = ' '.join(str(myitems) for myitems in fullstring)
fullstring2 = fullstring1.replace("[", "")
fullstring3 = fullstring2.replace("]", "")
fullstring4 = fullstring3.replace("'", "")
fullstring5 = fullstring4.replace(" ", "")
new2 = new1[0].split()
z = new2[3]
a = int(z)
zz = new2[4]
b = int(zz)
if new2[6] == "+":
    sequence = fullstring5[a:b]
else:
    sequence = fullstring5[a:b][::-1]
sys.stdout.write(f'>{args.type}:{args.attribute}:{args.value}\n{sequence}\n')