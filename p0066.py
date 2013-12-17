#!/usr/bin/python
from math import sqrt
from fractions import Fraction

# http://en.wikipedia.org/wiki/Pell%27s_equation

def convergent(n, ai):
    n -= 1
    s = Fraction(ai(n))
    while n > 0:
        n -= 1
        s = ai(n) + Fraction(1, s)
    return s

def is_square(x):
    return int(sqrt(x))**2 == x


def min_solution(D):
    def ai(i):
        sn = sqrt(D)
        m = 0
        d = 1
        a = a0 = int(sn)

        j = 0
        while j < i:
            j += 1
            m = d*a - m
            d = (D - m*m) / d
            a = int((a0 + m) / d)

        return a

    def solution(x):
        cf = convergent(x, ai)
        if cf.numerator**2 - D*(cf.denominator**2) == 1:
            print '%d^2 - %d*%d^2 = 1' % (cf.numerator, D, cf.denominator)
            return cf.numerator
        return -1

    i = 1
    while 1:
        xi = solution(i)
        if xi > 0:
            return xi
        i += 1


def solve():
    dmax = 1000
    xmax = -1
    ans = -1
    for D in range(2, dmax+1):
        if is_square(D):
            continue

        x = min_solution(D)
        if x > xmax:
            xmax = x
            ans = D

    return ans

if __name__ == '__main__':
    print solve()
