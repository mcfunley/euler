#!/usr/bin/env python
from euler import digits
from operator import itemgetter

def generate_interesting():
    for n in range(1, 5000):
        for exp in range(2, 10):
            v = n**exp
            ds = digits(v)
            if len(ds) > 1 and sum(ds) == n:
                yield n, exp, v

for i, (n, e, v) in enumerate(sorted(list(generate_interesting()), key=itemgetter(2)), 1):
    print(i, '%s**%s = %s' % (n, e, v))
