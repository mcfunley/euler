#!/usr/bin/env python
from itertools import count
from math import log

digits = range(1, 10)
digitset = set(digits)

def is_pandigital(n):
    s = { int(d) for d in str(n) }
    return len(digitset - s) == 0

def is_ordered_pandigital(n):
    s = str(n)
    if len(s) < len(digits):
        return False

    for d in digits:
        if s[d-1] != str(d):
            return False
    return True

def generate_fibs():
    yield 1
    yield 1

    f2 = 1
    f1 = 1
    for k in count(3):
        f = f2 + f1
        f2 = f1
        f1 = f
        yield f

def first_nine(n):
    m = int(log(n, 10))
    if m < 9:
        return n
    return int(n / 10**(m - 8))

def last_nine(n):
    return n % 1000000000


def find(p):
    for k, fib in zip(count(1), generate_fibs()):
        if p(fib):
            return k, fib

if __name__ == '__main__':
    print(find(lambda n: is_pandigital(last_nine(n))))
    print(find(lambda n: is_pandigital(first_nine(n))))
    print(find(lambda n: is_pandigital(first_nine(n)) and is_pandigital(last_nine(n)))[0])
