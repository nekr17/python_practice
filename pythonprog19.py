#! /usr/bin/python3.9
# pythonprog19
a = int(input())
b = int(input())
c = 1
while c % b != 0 or c % a != 0:
    c += 1
print(c)
