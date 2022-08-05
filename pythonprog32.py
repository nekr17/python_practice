#! /usr/bin/python3.9
# pythonprog32
lst = [int(i) for i in input().split()]

def modify_list(l):
    x = []
    j = 0
    for i in l:
        if i % 2 == 0:
            j = int(i / 2)
            x.append(j)
    del l[:]
    for i in x:
        l.append(i)
modify_list(lst)
print(lst)
