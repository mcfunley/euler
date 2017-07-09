#!/usr/bin/env python
from functools import lru_cache

@lru_cache(maxsize=1000)
def f(blocksize, rowlen):
    if rowlen < blocksize:
        # empty only
        return 1

    # one for empty
    total = 1
    for i in range(0, rowlen - blocksize + 1):
        remainder = rowlen - (i + blocksize)
        total += f(blocksize, remainder)
    return total

def solve(rowlen):
    # don't count all empty, subtract one for each
    return f(2, rowlen) + f(3, rowlen) + f(4, rowlen) - 3

print(solve(5))
print(solve(50))
