#!/usr/bin/env python
from sympy import isprime
from itertools import permutations
from euler import from_digits, partitions

def generate_numbers(ds):
    p = 0
    for perm in permutations(ds):
        p += 1
        if p % 1000 == 0:
            print(p)
        for part in partitions(perm):
            yield [from_digits(xs) for xs in part]


def ascending_sets(ds):
    for s in generate_numbers(ds):
        if not any([a > b for a, b in zip(s, s[1:])]):
            yield s

def prime_sets(ds):
    for s in ascending_sets(ds):
        if all([isprime(x) for x in s]):
            yield s

print(sum(1 for _ in prime_sets(range(1,10))))
