"""
Task:
Write a program to read through
a mail log, build a histogram using
a dictionary to count how many messages
have come from each email address, and print
the dictionary.
>>> print(adr, adress[adr])
david.horwitz@uct.ac.za 4
louis@media.berkeley.edu 3
wagnermr@iupui.edu 1
zqian@umich.edu 4
gopal.ramasammycook@gmail.com 1
antranig@caret.cam.ac.uk 1
stephen.marquard@uct.ac.za 2
cwen@iupui.edu 5
gsilver@umich.edu 3
ray@media.berkeley.edu 1
rjlowe@iupui.edu 2
"""
words = []
adress = {}
txt = open('mbox-short.txt')
for line in txt:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        if words[1] not in adress:
                adress[words[1]] = 1
        else:
            adress[words[1]] += 1
help(dict)