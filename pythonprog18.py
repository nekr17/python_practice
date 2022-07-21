#! /usr/bin/python3.9
# pythonprog19

s = str(input())
 
def p(prev, count):
    print(prev, end='')
    print(count, end='')
 
prev = s[0]
count = 1
for i in s[1:]:
    if i == prev:
        count += 1
        continue
    p(prev, count)
    prev = i
    count = 1
p(prev, count)
