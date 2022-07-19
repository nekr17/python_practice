#! /usr/bin/python3.9
# pythonprog9
# square of a triangle
a=int(input())
b=int(input())
c=int(input())
import math
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print(s)
