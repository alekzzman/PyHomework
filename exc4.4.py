"""
Task:
This program counts the distribution of the hour of
the day for each of the messages. You can pull the
hour from the “From” line by finding the time string
and then splitting that string into parts using the
colon character. Once you have accumulated the counts
for each hour, print out the counts, one per line,
sorted by hour as shown below.
"""
words = []
dates = {}
hours = list()
txt = open('mbox-short.txt')
for line in txt:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        date = words[5].split(':')

        if date[0] not in dates:
                dates[date[0]] = 1
        else:
            dates[date[0]] += 1
for hour, count in dates.items():
    hours.append((hour, count))
    hours.sort()
for hour in hours:
    print(hour[0], hour[1])