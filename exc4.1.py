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