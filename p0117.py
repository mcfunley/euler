#!/usr/bin/env python
from functools import lru_cache

block_sizes = [2,3,4]

@lru_cache(maxsize=1000)
def f(rowlen):
    if rowlen < min(block_sizes):
        # empty only
        return 1

    # one for empty
    total = 1
    for bs in block_sizes:
        for i in range(0, rowlen - bs + 1):
            remainder = rowlen - (i + bs)
            total += f(remainder)
    return total


print(f(5))
print(f(50))
