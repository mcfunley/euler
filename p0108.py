#!/usr/bin/env python
import numpy as np
from sympy import factorint
from sympy.ntheory.generate import prime

# 1/x + 1/y = 1/n
# y/xy + x/xy = 1/n
# (x + y)/xy = 1/n
# xy / (x + y) = n

# http://www.math.psu.edu/treluga/311w/gcdTheoremGuide.pdf

# we want the greatest common divisor of integers x and y,
# g = gcd(x, y),
# so x = da, y = db and gcd(a, b) = 1
# n = damdb / (da + db)
# n = ddab / d(a + b)
# n = dab / (a + b)

# we can deduce that (a+b) divides d, so
# d = k(a + b) where k is a positive integer

# k(a + b)ab / (a + b) = n
# n = kab
# y = db = k(a + b)b = kb(a+ b)
# x = ka(a + b)

# for integers k, a, b

def values(k, a, b):
    return k*a*(a + b), k*b*(a + b), k*a*b

# want n = the first number with 1000 divisors
# how do we count divisors?
# https://www.math.upenn.edu/~deturck/m170/wk2/numdivisors.html

# In general, if you have the prime factorization of the number n,
# then to calculate how many divisors it has, you take all the exponents
# in the factorization, add 1 to each, and then multiply these "exponents + 1"s together.

def divisors(n):
    return np.prod([ e+1 for _, e in factorint(n).items() ])

# but counting up counting divisors takes too long -- need to generate candidates
# from lists of primes

# say n = p0^e * p1^f * p2^g
# it has (e+1)*(f+1)*(g+1) divisors
# if e < f, then we can find a smaller number with as many divisors by
# choosing a larger e and a smaller f.
# so we want e < f < g and so on.

# note that that means the answer must be even, because it'd contain the factor
# 2^e with e > 1.

# how many primes do we need?
# At most p0^1 * ... p9^1 because (1+1)^10 = 1024, which is more than 1000.

# so we want to take a vector of the first ten primes, and a vector of their
# exponents starting at zero and increment until we find the first n larger
# than 1000.

def n(primes, exponents):
    return np.prod(np.power(primes, exponents).astype(object))

primes = np.array([prime(n) for n in range(1, 11)])

def gen_exponents(size):
    def gen(exprange, maxlen, exps):
        if len(exps) == maxlen:
            yield exps
        elif len(exps) == 0:
            for e in exprange:
                for exps2 in gen(exprange, maxlen, [e]+exps):
                    yield exps2
        else:
            for xi in [x for x in exprange if x >= exps[0]]:
                for exps2 in gen(exprange, maxlen, [xi]+exps):
                    yield exps2

    return gen(range(5), size, [])


ans = 1e100
divisors_needed = 1000 * 2 - 1

for exps in gen_exponents(len(primes)):
    v = n(primes, exps)
    divisors_v2 = np.prod([2*e + 1 for e in exps])

    if divisors_v2 >= divisors_needed:
        ans = min(ans, v)

print(ans)
