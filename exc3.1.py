words = []
txt = open('romeo.txt').read()
text = txt.split()
for word in text:
    if word in words:
        continue
    else:
        words.append(word)
words.sort()
print(words)