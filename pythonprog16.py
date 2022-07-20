#! /usr/bin/python3.9
# pythonprog16
genome = str(input())
s = 0
s2 = 0
for i in genome:
    s2 +=1
    if i == "c" or i == "C" or i == "G" or i == "g":
        s += 1
print((s/s2)*100)
