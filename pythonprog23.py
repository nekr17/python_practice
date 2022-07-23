#! /usr/bin/python3.9
# pythonprog23

a = [ int(i) for i in input().split()]
a.sort()
a += [0]
s = a[0]
sch = 0
count = []
for n in a[1:]:
    sch += 1
    if n == s and s != a[sch+1]:
        count += [n]
    s = a[sch]
for counts in count:
    print(counts, end=' ')
