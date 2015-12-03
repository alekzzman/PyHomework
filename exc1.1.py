"""
Task:
Write a while loop that starts at the last character
 in the string and works its way backwards to the first
  character in the string, printing each letter on a
  separate line, except backwards.
  >>> bckwrd('banana')
  a
  n
  a
  n
  a
  b
"""
def bckwrd(word):
    count = len(word)
    first = 0
    while count > first:
        count = count - 1
        letter = word[count]
        print(letter)
bckwrd('banana')