#!/usr/bin/env python
from itertools import count
from math import sqrt
from collections import OrderedDict

def proper_divisors(n):
    yield 1
    for i in range(2, (int(sqrt(n)) + 1) + 1):
        if n % i == 0:
            yield i
            yield int(n / i)


def find_qualifying_chain(n):
    chain = OrderedDict()
    first = n
    while 1:
        if n in chain:
            # cycle found
            return None

        chain[n] = 1

        n = sum(proper_divisors(n))
        if n == 1:
            return None

        if n == first:
            return list(chain.keys())

        if n > 1000000:
            return None


def run():
    longest = []
    for n in range(2, 1000000):
        chain = find_qualifying_chain(n)

        if chain:
            if len(chain) > len(longest):
                print(chain, min(chain))
                longest = chain

    print(longest)
    print(min(longest))


if __name__ == '__main__':
    run()
