#!/usr/bin/python
"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d <= 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
"""
import math
from euler import gcd

#max_d = 8
max_d = 1000000
fractions = []


def reduced(n, d):
    return gcd(n, d) == 1

rightmost = None
rightmost_v = 2. / 5
for d in xrange(2, max_d + 1):
    # we're looking for a number between the current winner and 3/7. 
    lo = int(rightmost_v * d)
    hi = int(math.ceil(3. / 7 * d))
    
    if lo < 1:
        continue

    for n in xrange(lo, hi):
        val = float(n) / d
        if reduced(n, d) and val > rightmost_v:
            rightmost = (n, d)
            rightmost_v = val

    if d % 10000 == 0:
        print d, rightmost, (3/7.) - rightmost_v

print rightmost
