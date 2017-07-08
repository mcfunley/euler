#!/usr/bin/env python
from euler import digits
from itertools import count

def is_bouncy(n):
    ds = digits(n)
    asc = all([a <= b for a, b in zip(ds, ds[1:])])
    desc = all([a >= b for a, b in zip(ds, ds[1:])])
    return not (asc or desc)

bouncy = 0
for n in count(1):
    if is_bouncy(n):
        bouncy += 1

    if n % 10000 == 0:
        print(n, bouncy / n)

    if bouncy / n >= .99:
        print(n, bouncy / n)
        break
