#!/usr/bin/env python
from functools import lru_cache
from itertools import count


@lru_cache(maxsize=100)
def f(minred, rowlen):
    if rowlen < minred:
        # empty only
        return 1

    # one for empty
    total = 1
    for redlen in range(minred, rowlen+1):
        for i in range(0, rowlen - redlen + 1):
            remainder = rowlen - (i + redlen) - 1
            total += f(minred, remainder)
    return total


for n in count(1):
    if f(50, n) > 1000000:
        print(n)
        break
