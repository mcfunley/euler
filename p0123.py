#!/usr/bin/env python
from sympy import prime
from itertools import count

# ((pn - 1)**n + (pn + 1)**n) / pn**2

# remainder is 2, 2p, 2, 6p, 2, 10p, ... per problem 120
# which is [2, 2*n*p, 2, 2*n*p, ...]

# only odd-numbered primes
for n in count(1, 2):
    p = prime(n)
    if 2 * n * p >= 1e10:
        print(n, p, 2*n*p)
        break
