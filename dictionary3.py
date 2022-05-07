#using dictionaries part 2
dictionary = {}
words = input('Please enter some lines: ')
words = words.split()
for word in words :
    dictionary[word] = dictionary.get(word, 0) + 1
print(dictionary)
for blah in dictionary :
    print(blah, dictionary[blah])
#methods for dictionaries
#eg print(dictionary.keys())
#or print(dictionary.values())
print(dictionary.values())
print(dictionary.keys())
print(dictionary.items()) #returns a tuple of they key:value pairs in the dictionary
#this allows for the use of dual iteration variables within a single for
for a,b in dictionary.items() :
    print(f'the key is actually {a} and the value is actually {b}')