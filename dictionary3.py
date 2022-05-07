#using dictionaries part 2
dictionary = {}
words = input('Please enter some lines: ')
words = words.split()
for word in words :
    dictionary[word] = dictionary.get(word, 0) + 1
print(dictionary)
