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

#yikes
#!/usr/bin/env python3
import argparse
import sys
mypar = argparse.ArgumentParser()
mypar.add_argument('--source_gff', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--value', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--attribute', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--type', type = str, required = True, help = 'I hope this works')
mylist =[]
query = []
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
            mylist.append(lin)
            print(lin)
            continue
        for all in mylist:
            query.append(all)
 #           sys.stdout.write(f'>{args.type}:{args.attribute}:{args.value}\n ...Seq...\n')
#print(query)

#!/usr/bin/env python3
import argparse
import sys
mypar = argparse.ArgumentParser()
mypar.add_argument('--source_gff', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--value', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--attribute', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--type', type = str, required = False, help = 'I hope this works')
mylist =[]
newlist = []
args = mypar.parse_args()
blah = str(f'{args.attribute}={args.value}')
#Try to parse through the file
value = args.value
for lin in open(args.source_gff):
    lin = lin.rstrip()
    newlist.append(lin)
    for all in newlist:
        if blah in all:
            mylist.append(all)
    print(mylist)
######
#!/usr/bin/env python3
import argparse
import sys
mypar = argparse.ArgumentParser()
mypar.add_argument('--source_gff', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--value', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--attribute', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--type', type = str, required = True, help = 'I hope this works')
args = mypar.parse_args()
blah = str(f'{args.attribute}={args.value}')
blah1 = str(f'{args.type}')
list1 =[]
for line in open(args.source_gff):
    if line.startswith('c'):
        list1.append(line)
new = [z for z in list1 if blah in z]
new1 = [x for x in new if blah1 in x]
print(str(new1))
if len(new1) == False:
    print('SOrry')

###############
#!/usr/bin/env python3
import argparse
import sys
mypar = argparse.ArgumentParser()
mypar.add_argument('--source_gff', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--value', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--attribute', type = str, required = True, help = 'I hope this works')
mypar.add_argument('--type', type = str, required = True, help = 'I hope this works')
args = mypar.parse_args()
blah = str(f'{args.attribute}={args.value}')
blah1 = str(f'{args.type}')
list1 =[]
for line in open(args.source_gff):
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
sys.stdout.write(f'>{args.type}:{args.attribute}:{args.value}\n ...Seq...\n')
new2 = new1[0].split()
print(str(new2[0:3]))
###############
!/usr/bin/env python3
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
print(fullstring5)
sys.stdout.write(f'>{args.type}:{args.attribute}:{args.value}\n ...Seq...\n')
new2 = new1[0].split()
print(str(new2[0:3]))
######
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
#print(new2[0:7])
if new2[6] == "+":
    sequence = fullstring5[a:b]
    revseq = sequence[::-1]
else:
    sequence = fullstring5[a:b]
sys.stdout.write(f'>{args.type}:{args.attribute}:{args.value}\n{revseq}\n')

####60 nucleotides per works for +
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
for tot in e:
    sys.stdout.write(f'{fullstring5[prev:a + tot * 60]}\n')
    prev = prev + 60

if new2[6] == "+":
    sequence = fullstring5[a:b]
else:
    sequence = fullstring5[a:b][::-1]
sys.stdout.write(f'{fullstring5[b - d:b]}\n')

####
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
##############
#!/usr/bin/env python3
import argparse
import sys
import re
#setting up the command line interface, it seems to have issues though with being loose in its interpretation of
#exact arguments e.g. ARS100 would return ARS1102, ARS1103 etc. more likely an issue with my code
cknuff = argparse.ArgumentParser()
cknuff.add_argument('--source_gff', type = str, required = True, help = 'Enter source .gff here')
cknuff.add_argument('--value', type = str, required = True, help = 'Enter value e.g. YAR003W')
cknuff.add_argument('--attribute', type = str, required = True, help = 'Enter attribute e.g. ID or Parent')
cknuff.add_argument('--type', type = str, required = True, help = 'Enter type here e.g. gene')
ck = cknuff.parse_args()
blah = str(f'{ck.attribute}={ck.value}')
blah1 = str(f'{ck.type}')
list0 =[]
list1 =[]
list2 =[]
#my code seems to behave better for me if I throw everything into lists and manipulate from there
#definately not pythonic and very memory inefficient
for ducks in open(ck.source_gff):
    list0.append(ducks)
    if ducks.startswith('c'):
        list1.append(ducks)
new = [z for z in list1 if blah in z]
if len(new) == False:
    print("I'm sorry nothing matches your query or you entered something incorrectly. Please re-run and try again")
    quit()
new1 = [x for x in new if blah1 in x]
if len(new1) == False:
    print("Nothing matches your query and your type is not valid. Please re-run and try again")
    quit()
for all in list0:
    jhu = re.findall(r'^[A:G:T:C][ATGC]{10,100}', all)
    list2.append(jhu)
fullstring = ' '.join(str(liststuff) for liststuff in list2)
fullstring1 = ' '.join(str(liststuff) for liststuff in fullstring)
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
thepool = list(range(1, c + 1))
prev = a
prevrev = b
if len(new1) > 1:
    sys.stdout.write('Be warned: Your query has multiple features! The first one is:\n')
sys.stdout.write(f'>{ck.type}:{ck.attribute}:{ck.value}\n')
if new2[6] == "+":
    for summertime in thepool:
        sys.stdout.write(f'{fullstring5[prev:a + summertime * 60]}\n')
        prev = prev + 60
    sys.stdout.write(f'{fullstring5[b - d:b]}\n')
else:
    for summertime in thepool:
        sys.stdout.write(f'{fullstring5[b - summertime * 60:prevrev][::-1]}\n')
        prevrev = prevrev - 60
    sys.stdout.write(f'{fullstring5[a:a + d][::-1]}\n')
########single read
#!/usr/bin/env python3
import argparse
import sys
import re
#setting up the command line interface, it seems to have issues though with being loose in its interpretation of
#exact arguments e.g. ARS100 would return ARS1102, ARS1103 etc. but more likely an issue with my code
cknuff = argparse.ArgumentParser()
cknuff.add_argument('--source_gff', type = str, required = True, help = 'Enter source .gff here')
cknuff.add_argument('--value', type = str, required = True, help = 'Enter value e.g. YAR003W')
cknuff.add_argument('--attribute', type = str, required = True, help = 'Enter attribute e.g. ID or Parent')
cknuff.add_argument('--type', type = str, required = True, help = 'Enter type here e.g. gene')
ck = cknuff.parse_args()
milk = str(f'{ck.attribute}={ck.value}')
flower = str(f'{ck.type}')
list1 =[]
list2 =[]
#my code seems to behave better for me if I throw everything into lists and manipulate from there
#definately not pythonic and very memory inefficient
for ducks in open(ck.source_gff):
    jhu = re.findall(r'^[A:G:T:C][ATGC]{10,100}', ducks)
    list2.append(jhu)
    if ducks.startswith('c'):
        list1.append(ducks)
#checking my lists for substring from command line input
new = [cookies for cookies in list1 if milk in cookies]
if len(new) == False:
    print("I'm sorry nothing matches your query or you entered something incorrectly. Please re-run and try again")
    quit()
new1 = [vase for vase in new if flower in vase]
if len(new1) == False:
    print("Nothing matches your query and your type is not valid. Please re-run and try again")
    quit()
#trying to fix my FASTA joins
fullstring = ' '.join(str(liststuff) for liststuff in list2)
fullstring1 = ' '.join(str(liststuff) for liststuff in fullstring)
fullstring2 = fullstring1.replace("[", "")
fullstring3 = fullstring2.replace("]", "")
fullstring4 = fullstring3.replace("'", "")
fullstring5 = fullstring4.replace(" ", "")
new2 = new1[0].split()
z = new2[3]
a = int(z)
zz = new2[4]
b = int(zz)
#Print 60 nucleotides at a time
c = int((b - a)/60)
d = (b - a) % 60
thepool = list(range(1, c + 1))
prev = a
prevrev = b
if len(new1) > 1:
    sys.stdout.write('Be warned: Your query has multiple features! The first one is:\n')
sys.stdout.write(f'>{ck.type}:{ck.attribute}:{ck.value}\n')
if new2[6] == "+":
    for summertime in thepool:
        sys.stdout.write(f'{fullstring5[prev:a + summertime * 60]}\n')
        prev = prev + 60
    sys.stdout.write(f'{fullstring5[b - d:b]}\n')
else:
    for summertime in thepool:
        sys.stdout.write(f'{fullstring5[b - summertime * 60:prevrev][::-1]}\n')
        prevrev = prevrev - 60
    sys.stdout.write(f'{fullstring5[a:a + d][::-1]}\n')
######
