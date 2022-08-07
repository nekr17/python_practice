#! /usr/bin/python3.9
# pythonprog33
d = {}
k, i = 0, 0
while k != '' and i != '':
    print('put key')
    k = input()
    print('put value')
    i = input()
    d[k] = i
del d['']

def update_dictionary(d, key, value):
    sch1 = 0
    sch2 = 0
    for i in d:
        if i == key:
            sch1 += 1
            d[key] = value
        else:
            continue
    if sch1 == 0:
        d[2*key] = value
    print(d)
r, t = input().split()
update_dictionary(d, r, t)
