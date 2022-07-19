#! /usr/bin/python3.9
# pythonprog13
for i in range(6):
    a = int(input())
    if a < 10:
        continue
    if a > 100:
        break
    print(a)
