#! /usr/bin/python3.9
# pythonprog5

A = int(input())
B = int(input())
H = int(input())
if A <= H <= B:
	print("Это нормально")
elif A >= H:
	print("Недосып")
elif H >= B:
	print("Пересып")
