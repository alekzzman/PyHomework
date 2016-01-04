"""
Task:
Define the insertion sort function
>>> print(a)
[12, 53, 97, 111, 555, 675]
"""
a = [111,53,12,555,675,97]
b = len(a)
for number in range(1,b):
    value = a[number]
    position = number
    while position>0 and a[position-1]>value:
        a[position]= a[position -1]
        position -= 1
        print(a[number])
    a[position] = value
print(a)