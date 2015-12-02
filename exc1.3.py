"""
Task:
Encapsulate this code in a function named count,
and generalize it so that it accepts the string
and the letter as arguments.
>>> count('banana', 'a')
3
"""
def count(word, letter):
    result = 0
    for symb in word:
        if symb == letter:
            result = result + 1
    print(result)
count('banana', 'a')