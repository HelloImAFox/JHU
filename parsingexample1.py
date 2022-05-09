#parsing examples
with open('/users/christopherknuff/desktop/mbox-short.txt') as file:
line = file.readline()
for line in file:
    lin
        line.rstrip()
        if line == '': #this skips blank lines to prevent traceback
            continue
#This also skips blank lines
        words = line.split()
        if len(words) < 1:
            continue
# to look for a specific word in a line
        if not words[0] == 'From': #if first word doesnt = 0
            continue
        print(words[2])
