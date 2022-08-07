#! /usr/bin/python3.9
# pythonprog34
d = [str(i) for i in (input().lower().split())]
n = {}
r = 1
for i in d:
    for s in d:
        if s == i:
            r += 1
        else:
            continue
    n[i] = r
    r = 0
for key, value in n.items():
    print(key, value)
