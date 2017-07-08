#!/usr/bin/env python
from sympy import primerange
from sympy.ntheory.primetest import isprime
from euler import digits
from itertools import combinations, product

# code is correct, but generating the list of ten digit primes is very time
# consuming.
# need to generate things with repeating digits and then narrow them down
# to just the primes.

def primes(n):
    return primerange(10**(n-1), 10**n)

def longest_run(p, d):
    return sum(1 for dig in digits(p) if dig == d)

def m(n, d):
    maxrun = 0
    for p in primes(n):
        maxrun = max(longest_run(p, d), maxrun)
    return maxrun

def primelist(n, d):
    longest = m(n, d)
    for p in primes(n):
        if longest_run(p, d) == longest:
            yield p

def s_slow(n, d):
    return sum(primelist(n, d))


# generating primes approach

def from_digits(ds):
    return sum(n*10**i for i, n in enumerate(reversed(ds)))

def generate_primes(n, d, m):
    # generate all primes between 10**(n-1) and 10**n that have the digit d
    # repeated at least m times

    # take all of the digits other than d
    # given n and m compute how many of them we can include in the number
    # for every configuration of non-d digits apply the cartesian product of
    # the non-d digits to the available slots
    # filter out non-prime numbers

    other_digits = set(range(10)) - {d}
    other_digit_slots = n - m
    for other_digit_configuration in combinations(range(n), other_digit_slots):
        for digits in product(other_digits, repeat=other_digit_slots):
            ds = [d]*n
            for i, od in zip(other_digit_configuration, digits):
                ds[i] = od

            if ds[0] == 0:
                # no leading zero
                continue

            v = from_digits(ds)
            if isprime(v):
                yield v

def s(n, d):
    # start with a guess for m(n, d)
    m = n - 1
    total = 0
    while total == 0 and m > 0:
        # generate primes - if none are found decrement m and try again
        for p in generate_primes(n, d, m):
            total += p

        m -= 1

    print('m(%s, %s) = %s' % (n, d, m+1))
    print('s(%s, %s) = %s' % (n, d, total))
    return total

n = 10
total = 0
for d in range(0, 10):
    total += s(n, d)

print()
print(total)
