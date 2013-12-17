#!/usr/bin/python
from math import sqrt
import sys



def cf_period(n):
    sn = sqrt(n)
    alist = []

    # http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

    m = 0
    d = 1
    a = a0 = int(sn)

    if sn - a0 == 0:
        # not irrational
        return 0
    
    while 1:
        alist.append(a)

        if a == 2*a0:
            break

        m = d*a - m
        d = (n - m*m) / d
        a = int((a0 + m) / d)

    alist = alist[1:]
    print 'sqrt(%d)=[%d, %s],' % (n, a0, tuple(alist)), 'period=%d' % len(alist)
    return len(alist)

nmax = 13
nmax = 10000
odd = 0

for n in range(2, nmax+1):
    if cf_period(n) % 2 == 1:
        odd += 1

print odd
