#! /usr/bin/python3.9
# pythonprog11

word=str(input())

if word == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    import math
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(s)
elif word == "прямоугольник":
    a = int(input())
    b = int(input())
    print(a*b)
elif word == "круг":
    print("write radius:")
    r = int(input())
    print(2*3.14*r)
