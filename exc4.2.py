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
for adr in adress:
    print(adr, adress[adr])