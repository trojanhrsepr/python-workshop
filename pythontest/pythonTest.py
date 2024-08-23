wordList = ["name", "namea", "nameb"]
wordList1 = []
for string1 in wordList:
    string1 = string1[0].upper() + string1[1:-1] + string1[-1].upper()
    print(string1)
    wordList1.append(string1)
    wordList1.append(123)
print(wordList)
print(wordList1)

# Parallel iterator
for elm1, elm2 in zip(wordList1, wordList):
    print(elm1, elm2)

# Import itertools

import itertools

for e1, e2 in itertools.zip_longest(wordList, wordList1, fillvalue=0):
    print(e1, e2)
