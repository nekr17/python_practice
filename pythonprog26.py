#! /usr/bin/python3.9
# pythonprog26
n = int(input())
s = []
for i in range(n+1):
        s += [i] * i 
print(s[:n+1])
