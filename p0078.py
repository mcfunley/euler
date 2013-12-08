#!/usr/bin/python
"""
Let p(n) represent the number of different ways in which n coins can be 
separated into piles. For example, five coins can separated into piles in 
exactly seven different ways, so p(5)=7.

OOOOO
OOOO O
OOO OO
OOO O O
OO OO O
OO O O O
O O O O O

Find the least value of n for which p(n) is divisible by one million.
"""

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

n = 0
while True:
    if p(n) % 1000000 == 0:
        print n
        break
    n += 1


    
