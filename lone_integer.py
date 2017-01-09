""" Consider an array of n integers, A, where all but one of the integers occur in pairs. 
Find and print the lone/unique element. Use of bit manipulation is expected. """

#!/bin/python
import sys

def lonely_integer(a):
    lone = 0
    for i in a:
        lone ^= i
    return lone
    
n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)
