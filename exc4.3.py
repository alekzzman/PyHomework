"""
Task:
Revise a previous program as follows: Read and
parse the “From” lines and pull out the addresses
from the line. Count the number of messages from
each person using a dictionary.
After all the data has been read, print the person
with the most commits by creating a list of (count, email)
tuples from the dictionary. Then sort the list in reverse
order and print out the person who has the most commits.
>>> print(a[1], a[0])
cwen@iupui.edu 5
"""
words = []
adress = {}
l = list()
txt = open('mbox-short.txt')
for line in txt:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        if words[1] not in adress:
                adress[words[1]] = 1
        else:
            adress[words[1]] += 1
for adr, number in adress.items():
    l.append((number, adr))
l.sort(reverse=True)
a = l[0]
print(a[1], a[0])
