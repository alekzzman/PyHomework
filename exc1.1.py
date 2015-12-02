"""
Task:
Write a while loop that starts at the last character
 in the string and works its way backwards to the first
  character in the string, printing each letter on a
  separate line, except backwards.
  >>> word = 'banana'
  a
  n
  a
  n
  a
  b
"""
word = 'banana'
count = len(word)
first = 0
while count > first:
    count = count - 1
    letter = word[count]
    print(letter)