#! /usr/bin/python3.9
# pythonprog29
a = []
b = []
c = []
s = 'e'
while s != 'end':
    a = [ s for s in input().split() ]
    s = a[0]
    b += [a]
del b[-1]
c = [row[:] for row in b]
i = 0
j = 0
for i in range(len(b)):
    for j in range(len(b[0])):
        c[i][j] = int(b[(i-1) % len(b)][j]) + int(b[(i+1) % len(b)][j]) + int(b[i][(j-1) % len(b)]) + int(b[i][(j+1) % len(b)])
for i in range(len(c)):
    for s in c[i]:
        print(s, end=' ')
    print(end="\n")
