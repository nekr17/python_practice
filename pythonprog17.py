#! /usr/bin/python3.9
# pythonprog17
s = str(input())
a = 0
b = 0
c = 0
a1 = "a"
b1 = "b"
c1 = "c"
for i in s:
    if i == 'a' or i == 'A':
            while i == "a" or i == "A":
                a += 1
                break
    if a != 0:
        print(a1, a, end="")
    if i == 'b' or i == 'B':
            while i == "b" or i == "B":
                b += 1
                break
    if b != 0:
        print(b1, b, end="")
    if i == 'c' or i == 'C':
            while i == "c" or i == "C":
                c += 1
                break
    if c != 0:
        print(c1, c, end="")
