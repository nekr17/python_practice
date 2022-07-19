#! /usr/bin/python3.9
# pythonprog15
a = int(input())
b = int(input())
s = 0 # count
r = 0 # output
for i in range(a, b+1):
    if i % 3 == 0:
        c = i
        s += 1
    else:
        continue
    r += c
print(r/s)
