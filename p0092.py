#!/usr/bin/env python

def digits(n):
    def g(n):
        while n:
            yield n % 10
            n //= 10
    return list(g(n))

def nextnum(n):
    return sum([d*d for d in digits(n)])

lookup1 = set()
lookup89 = set()

def is_89(n):
    original = n
    while 1:
        if n in lookup1:
            lookup1.add(original)
            return False
        if n in lookup89:
            lookup89.add(original)
            return True
        if n == 1:
            lookup1.add(original)
            return False
        if n == 89:
            lookup89.add(original)
            return True
        n = nextnum(n)

c = 0
for n in range(1, 10000000):
    if n % 1000 == 0:
        # print(c, n)
        pass
    if is_89(n):
        c += 1

print(c)
