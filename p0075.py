#!/usr/bin/python
from math import sqrt
import sys
from numpy import array, dot
from euler import gcd

stop = 1500000
triangles = {}

for m in xrange(2, int(sqrt(stop / 2)) + 1):
    for n in xrange(1, m + 1):
        if (n + m) % 2 == 1 and gcd(n, m) == 1:
            a = m*m + n*n
            b = m*m - n*n
            c = 2*m*n
            p = a+b+c
            while p <= stop:
                triangles[p] = triangles.setdefault(p, 0) + 1
                p += a + b + c

print len([x for x in triangles.itervalues() if x == 1])

sys.exit(0)

# see
# http://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples

A = array([1, -2, 2, 2, -1, 2, 2, -2, 3])
B = array([1, 2, 2, 2, 1, 2, 2, 2, 3])
C = array([-1, 2, 2, -2, 1, 2, -2, 2, 3])
A.shape = B.shape = C.shape = (3,3)

stop = 120
# [514605 386588 643637]

def iterate(triple):
    n = 0
    if sum(triple) <= stop:
        n = count(triple)
    if sum(triple * 2) <= stop:
        n = 1 + count(triple*2)
    return n

def count(triple):
    print triple
    left = dot(A, triple)
    mid = dot(B, triple)
    right = dot(C, triple)

    return 1 + iterate(left) + iterate(mid) + iterate(right)
    

print count(array([3,4,5]))

sys.exit(0)


# Choose n and c. Then solve system of two equations:
# a + b = n - c
# a^2 + b^2 = c^2
#
# by substitution, b = n - c - a. solving for a,
# a^2 + (n - c - a)^2 = c^2
# a^2 + (n - (c+a))(n - (c+a)) = c^2
# a^2 + (n^2 - 2n(c+a) + (c+a)^2) = c^2
# a^2 + (n^2 - 2nc - 2na + c^2 + 2ac + a^2) = c^2
# 2*(a**2) + 2*(c - n)*a + (n**2 - 2*n*c)
#
# Using the quadratic formula,
# (-(2*c - 2*n) +/- sqrt((2*c - 2*n)**2 - 4*2*(n**2 - 2*n*c))) / 4

# a = (-(n-c) +/- sqrt((n-c)^2 - 2n^2 + 4nc)) / 2
# a = ((c - n) +/- sqrt(n^2 - 2nc + c^2 - 2n^2 + 4nc)) / 2
# a = ((c - n) +/- sqrt(2nc + c^2 - n^2)) / 2
# 
# Then by substitution:
# b = n - c - a

nmax = 1500000
#nmax = 120
single_solutions = 0
for n in xrange(1, nmax+1):
    solutions = 0
    for c in xrange(1, n/2):
        x = (2*c - 2*n)**2 - 8*n*(n - 2*c)
        if x < 0:
            continue
        t = sqrt(x)
        p = 2*(n - c)

        a = (p + t) / 4
        b = (p - t) / 4

        if (a - int(a)) + (b - int(b)) != 0:
            continue

        solutions += 1

    if solutions == 1:
        single_solutions += 1

    if n % 10000 == 0:
        print n, single_solutions

print single_solutions


