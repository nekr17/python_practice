#! /usr/bin/python3.9
# pythonprog24
a = [5, 8, 4, 3, 5, 7]
m = a[0]
for i in a[1:]:
    if m > i:
        m = i
print(m)
