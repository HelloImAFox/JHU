#using dictionaries part 2
dictionary = {}
words = input('Please enter some lines: ')
zork = words.replace('"', '')
zorg = zork.split()
for word in zorg :
    dictionary[word] = dictionary.get(word, 0) + 1
print(dictionary)
for blah in dictionary :
    print(blah, dictionary[blah])
