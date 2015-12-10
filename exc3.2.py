"""
Task:
Write a program to read through the mail box data and
when you find line that starts with “From”, you will split
the line into words using the split function. We are
interested in who sent the message, which is the second
word on the From line.
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

You will parse the From line and print out the second word
for each From line, then you will also count the number of
From (not From:) lines and print out a count at the end.
>>> print(adress)
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu
rjlowe@iupui.edu
zqian@umich.edu
rjlowe@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
gsilver@umich.edu
gsilver@umich.edu
zqian@umich.edu
gsilver@umich.edu
wagnermr@iupui.edu
zqian@umich.edu
antranig@caret.cam.ac.uk
gopal.ramasammycook@gmail.com
david.horwitz@uct.ac.za
david.horwitz@uct.ac.za
david.horwitz@uct.ac.za
david.horwitz@uct.ac.za
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
louis@media.berkeley.edu
ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There are 27 adresses in the list
"""
words = []
lines = []
count = 0
txt = open('mbox-short.txt').read()
line = txt.split('\n')
for word in line:
    if word.startswith('From '):
        words = word.split()
        lines.append(words[1])
        count += 1
for adress in lines:
    print(adress)
print('There are', count, 'adresses in the list')