#! /usr/bin/python3.9
# pythonprog25

a = int(input())
s = [a]
while a != 0:
    b = int(input())
    a += b
    s += [b]
a = 0
b = 0
for i in s:
    a = i * i
    b += a
print(b)
