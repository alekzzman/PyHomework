"""
Task:
Write a program that categorizes each mail message
by which day of the week the commit was done. To
do this look for lines that start with “From”, then
look for the third word and keep a running count of
each of the days of the week. At the end of the program
print out the contents of your dictionary (order does not matter).
>>> print(days)
{'Fri': 20, 'Sat': 1, 'Thu': 6}
"""
words = []
days = {}
txt = open('mbox-short.txt')
for line in txt:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        if words[2] not in days:
                days[words[2]] = 1
        else:
            days[words[2]] += 1
print(days)