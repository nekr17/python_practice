#! /usr/bin/python3.9
# pythonprog27

lst = [ int(i) for i in input().split()]
x = int(input())
sch = -1
a = []
for i in lst:
    sch += 1
    if x == i:
        a += [sch]
if len(a) == 0:
    print('Отсутствует')
else:
    print(a)
