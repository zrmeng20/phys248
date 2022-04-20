#!/usr/bin/python

import sys
#print(sys.argv)

try:
    a = float(sys.argv[1])
except IndexError:
    print("Provide value for number a as argument. Using a= 10 as default")
    a=10

# a = 5
b = a + 5
print(b)
