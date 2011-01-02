#!/usr/bin/python
"""
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the
9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
from itertools import count

def nlen(n): return len(str(n))

powers = 0

for p in count(1):
    old = powers
    for i in count(1):
        n = i**p 
        l = nlen(n)
        if l < p:
            continue
        if l > p:
            break
        print "%d**%d" % (i, p), '=', n, 'has length', len(str(n))
        powers += 1
    if old == powers:
        break

print powers
