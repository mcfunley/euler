#!/usr/bin/python
"""
Find the sum of digits in the numerator of the 100th convergent of the continued 
fraction for e.
"""
from fractions import *

def ai(i):
    if i == 0:
        return 2

    if i % 3 == 1 or i % 3 == 0:
        return 1
    return 2*((i+1) / 3)

def convergent(n):
    n -= 1
    s = Fraction(ai(n))
    while n > 0:
        n -= 1
        s = ai(n) + Fraction(1, s)
    return s

def digits(x):
    return map(int, str(x))

print sum(digits(convergent(100).numerator))
