#!/usr/bin/env python
import numpy as np
from sympy import factorint
from sympy.ntheory.generate import prime

def n(primes, exponents):
    return np.prod(np.power(primes, exponents).astype(object))

primes = np.array([prime(n) for n in range(1, 15)])

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
solutions_required = 4000000
divisors_needed = solutions_required * 2 - 1

for exps in gen_exponents(len(primes)):
    v = n(primes, exps)
    divisors_v2 = np.prod([2*e + 1 for e in exps])

    if divisors_v2 >= divisors_needed:
        ans = min(ans, v)

print(ans)
