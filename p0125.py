#!/usr/bin/env python
from itertools import count
from euler import digits
import math

def is_palindrome(n):
    ds = digits(n)
    return ds == list(reversed(ds))


limit = int(math.sqrt(1e8))
psum = 0
results = set()

for i in range(1, limit+1):
    v = i**2

    for j in range(i + 1, limit + 1):
        v += j**2

        if v > 1e8:
            break

        if is_palindrome(v) and v not in results:
            psum += v
            results.add(v)

print(psum)
