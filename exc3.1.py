"""
Task:
Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function.

For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list.

When the program completes, sort and print the resulting words in alphabetical order.
>>> print(words)
['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
"""
words = []
txt = open('romeo.txt').read()
text = txt.split()
for word in text:
    if word in words:
        continue
    else:
        words.append(word)
words.sort()
print(words)