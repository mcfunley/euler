#!/usr/bin/python
"""
The cube, 41063625 (3453), can be permuted to produce two other cubes:
56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest
cube which has exactly three permutations of its digits which are also
cube.

Find the smallest cube for which exactly five permutations of its
digits are cube.
"""
from itertools import count

def key(n):
    return reduce(lambda a, b: a+b, sorted(str(n)))

d = {}
for i in count(0):
    cube = i**3
    k = key(cube)
    d.setdefault(k, []).append(cube)
    
    if len(d[k]) == 5:
        print min(d[k])
        break

