#! /usr/bin/python3.9
# pythonprog7

a, b=(int(i) for i in input().split())
print(a, b, "a i b")
s=0
if a % 2 == 0:
    a+=1
for i in range(a, b + 1, 2):
    s += i
    print(s)
print(s)
