#parsingexample2
file = open("whatever/whatever/whatever")
for line in file:
    line = line.rstrip()
    if not line.startswith('This word'):
        continue #this means continue to the next line