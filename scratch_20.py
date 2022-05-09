#!/usr/bin/env python3
import argparse
import sys
import re
mypar = argparse.ArgumentParser()
mypar.add_argument('--source_gff', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--value', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--attribute', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--type', type = str, required = True, help = 'I hope this works')
args = mypar.parse_args()
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
for all in list0:
    m = re.findall(r'^[A:G:T:C][ATGC]{10,100}', all)
    list2.append(m)
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
#trying to get it to print 60 nucleotides at a time
c = int((b - a)/60)
d = (b - a) % 60
e = list(range(1, c + 1))
prev = a
sys.stdout.write(f'>{args.type}:{args.attribute}:{args.value}\n')
seq = []
if new2[6] == "+":
    for tot in e:
        sys.stdout.write(f'{fullstring5[prev:a + tot * 60]}\n')
        prev = prev + 60
        r = f'{fullstring5[prev:a + tot * 60]}'
        seq.append(r)
    sys.stdout.write(f'{fullstring5[b - d:b]}\n')
else:
    for tot in e:
        sys.stdout.write()
    sequence = fullstring5[a:b][::-1]
    sys.stdout.write(sequence)
#sys.stdout.write(f'{fullstring5[b - d:b]}\n')


