#!/usr/bin/env python
from euler import digits
from gmpy2 import comb

def is_asc(n):
    ds = digits(n)
    return all([a <= b for a, b in zip(ds, ds[1:])])

def is_desc(n):
    ds = digits(n)
    return all([a >= b for a, b in zip(ds, ds[1:])])

def count_asc(nums):
    return sum(1 for n in nums if is_asc(n))

def count_desc(nums):
    return sum(1 for n in nums if is_desc(n))

# (1-9)00...
# 11 -> (1-9)11 = 9*
# 45 -> (1-4)45 = C(1,1) + C(2, 1) + C(3, 1) + ... + C(9, 1)
# 54 -> (5-9)54 = same

n = 100
print(comb(n+10, n) + comb(n+9, n) - (n*10 + 2))
