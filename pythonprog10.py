#! /usr/bin/python3.9
# pythonprog10

a=int(input()) # first number
b=str(input()) # sign
c=int(input()) # second number
if b== '+':
    print(a+c)
elif b== '-':
    print(a-c)
elif b== '*':
    print(a*c)
elif b== '/':
    if c == 0:
        print('Деление на ноль!')
    else:
        print(a/c)
elif b== 'div':
    if c== "0":
        print('Деление на ноль!')
    else:
        print(a//c)
elif b== 'pow':
    print(a**c)
elif b== 'mod':
    if c== 0:
        print('Деление на ноль!')
    else:
        print(a%b)
