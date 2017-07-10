#!/usr/bin/env python
from numpy import polydiv, polymul, flip
from numpy.polynomial.polynomial import polypow

# figuring out the formula for the remainders like so:

# for n in range(10000):
#     p = flip(polypow([-1, 1], n) + polypow([1, 1], n), 0)
#     _, r = polydiv(p, [2, 0, 0])
#     if len(r) > 1:
#         print(int(r[0]))

# reveals a pattern in the remainders for increasing n:

# [2, 2a, 2, 6a, 2, 10a, 2, 14a, ...]

# need to pick the (odd) remainder formula that will maximize the remainder for
# a given a. That's:
#

s = 0
for a in range(3, 1001):
    s += 2*a*((a - 1) // 2)
print(s)
