#using dictionaries
dic = {}
dic['one'] = 1
dic['two'] = 'too'
dic['ace'] = 'aces'
#print(dic)
#Using dictionary to count 
dictionary = {}
names = ['blah', 'whatever', 'blah', 'new', 'hey', 'whatever', 'blah', 'blah']
for name in names :
    if name not in dictionary :
        dictionary[name] = 1
    else:
        dictionary[name] = dictionary[name] + 1
print(dictionary)
#.get() method, a faster way to do the above
#dictionary.get(KEY eg 'name', default eg 0) or dictionary.get(name, 0)
dictionarie = {}
names = ['blah', 'whatever', 'blah', 'new', 'hey', 'whatever', 'blah', 'blah']
for name in names :
    dictionarie[name] = dictionarie.get(name, 0) + 1
print(dictionarie)