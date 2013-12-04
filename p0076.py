#!/usr/bin/python
"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""
from math import exp

# http://en.wikipedia.org/wiki/Partition_%28number_theory%29

cache = {}

def g(k):
    return k * (3*k - 1) / 2

def p(n):
    if n == 0:
        return 1
    if n < 0:
        return 0

    if n in cache:
        return cache[n]

    n_next = 1
    k = 1
    s = 0
    while 1:
        sign = (-1)**(k-1)
        s += sign * p(n - g(k))
        s += sign * p(n - g(-k))
        k += 1
        
        if n - g(k) < 0:
            break

    cache[n] = s
    return s

for i in [1,2,3,4,5,6]:
    print p(i)
print p(100) - 1
