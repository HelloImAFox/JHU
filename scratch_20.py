#!/usr/bin/env python3
import argparse
import sys
import re
mypar = argparse.ArgumentParser()
mypar.add_argument('--source_gff', type = str, required = True, help = 'Enter source .gff here')
mypar.add_argument('--value', type = str, required = True, help = 'Enter value e.g. YAR003W')
mypar.add_argument('--attribute', type = str, required = True, help = 'Enter attribute e.g. ID or Parent')
mypar.add_argument('--type', type = str, required = True, help = 'Enter type here e.g. gene')
args = mypar.parse_args()
blah = str(f'{args.attribute}={args.value}')
blah1 = str(f'{args.type}')
list0 =[]
list1 =[]
list2 =[]
leng = len(args.value)
leng1 = len(args.attribute)
for line in open(args.source_gff):
    list0.append(line)
    if line.startswith('c'):
#        line = line.strip()
        list1.append(line)
new = [z for z in list1 if blah in z]
if len(new) == False:
    print("I'm sorry nothing matches your query or you entered something incorrectly. Please re-run and try again")
    quit()
new1 = [x for x in new if blah1 in x]
for all in new1:
    cool = all.strip('\t')
    cool = cool.split()
    cool = cool[8].split(';')
    if len(cool[0]) > (leng + leng1 + 1):
        new1.remove(all)
newnew = ' '.join(str(myitems) for myitems in new1)
newnew = re.sub('\t', ' ', newnew)

newnew = newnew.split(' ')
final = []
try:
    if newnew[0] != newnew[9]:
        final.append(new1[0])
        new1 = final
    elif newnew[0] == newnew[9]:
        new1 = new1
except:
    pass
#for alll in new1:
#    newlist.append(alll)
#    if len(newlist) > 1: #and cool1[0] != cool1[9]:
#        pass
if len(new1) == False:
    print("Nothing matches your query and your type is not valid. Please re-run and try again")
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
prevrev = b
if len(new1) > 1:
    sys.stdout.write('Be warned: Your query has multiple features! The first one is:\n')
sys.stdout.write(f'>{args.type}:{args.attribute}:{args.value}\n')
if new2[6] == "+":
    for tot in e:
        sys.stdout.write(f'{fullstring5[prev:a + tot * 60]}\n')
        prev = prev + 60
    sys.stdout.write(f'{fullstring5[b - d:b]}\n')
else:
    for tot in e:
        sys.stdout.write(f'{fullstring5[b - tot * 60:prevrev][::-1]}\n')
        prevrev = prevrev - 60
    sys.stdout.write(f'{fullstring5[a:a + d][::-1]}\n')
if len(new1) >= 2:
    new3 = new1[1].split()
    z = new3[3]
    a = int(z)
    zz = new3[4]
    b = int(zz)
#trying to get it to print 60 nucleotides at a time
    c = int((b - a)/60)
    d = (b - a) % 60
    e = list(range(1, c + 1))
    prev = a
    prevrev = b
    if len(new1) > 1:
        sys.stdout.write('Be warned: Your query has multiple features! The second one is:\n')
    sys.stdout.write(f'>{args.type}:{args.attribute}:{args.value}\n')
    if new3[6] == "+":
        for tot in e:
            sys.stdout.write(f'{fullstring5[prev:a + tot * 60]}\n')
            prev = prev + 60
        sys.stdout.write(f'{fullstring5[b - d:b]}\n')
    else:
        for tot in e:
            sys.stdout.write(f'{fullstring5[b - tot * 60:prevrev][::-1]}\n')
            prevrev = prevrev - 60
        sys.stdout.write(f'{fullstring5[a:a + d][::-1]}\n')
####
if len(new1) >= 3:
    new4 = new1[2].split()
    z = new4[3]
    a = int(z)
    zz = new4[4]
    b = int(zz)
#trying to get it to print 60 nucleotides at a time
    c = int((b - a)/60)
    d = (b - a) % 60
    e = list(range(1, c + 1))
    prev = a
    prevrev = b
    if len(new1) > 1:
        sys.stdout.write('Be warned: Your query has multiple features! The Third one is:\n')
    sys.stdout.write(f'>{args.type}:{args.attribute}:{args.value}\n')
    if new4[6] == "+":
        for tot in e:
            sys.stdout.write(f'{fullstring5[prev:a + tot * 60]}\n')
            prev = prev + 60
        sys.stdout.write(f'{fullstring5[b - d:b]}\n')
    else:
        for tot in e:
            sys.stdout.write(f'{fullstring5[b - tot * 60:prevrev][::-1]}\n')
            prevrev = prevrev - 60
        sys.stdout.write(f'{fullstring5[a:a + d][::-1]}\n')
#print(lasttime)