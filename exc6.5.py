"""
Task:
Write a program that maps a list
of words into a list of integers
representing the lengths of the
correponding words.
>>> a = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")
>>> lst = list(map(lambda x: len(x), a))
>>> print(lst)
[6, 6, 4, 9, 6, 9]
"""
a = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")
lst = list(map(lambda x: len(x), a))
print(lst)