#!/usr/bin/python

def fac(n):
    s = 1
    while n > 1:
        s *= n
        n -= 1
    return s

def digits(n):
    ds = []
    while n:
        ds.append(n % 10)
        n /= 10
    return list(reversed(ds))

def digit_factorial(n):
    return sum(fac(d) for d in digits(n))

def nonrep_terms(n, stop = 62):
    terms = set()
    i = 1
    while (n not in terms) and i <= stop:
        terms.add(n)
        n = digit_factorial(n)
        i += 1
    return i - 1

chains = 0
for n in xrange(1, 1000001):
    if nonrep_terms(n) == 60:
        chains += 1

    if n % 10000 == 0:
        print n, chains

print chains

