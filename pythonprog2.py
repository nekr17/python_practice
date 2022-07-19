#! /usr/bin/python3.9
# pythonprog2.py

import sys

print("Script name:", sys.argv[0])
print("Arguments:", end=" ")

for arg in sys.argv[1:]:
	print(arg, end=" ")
print()
