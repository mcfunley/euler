#!/usr/bin/env python
from collections import defaultdict
from operator import itemgetter
from itertools import count

# the number of cube faces visible for the cuboid is the number of cubes needed
# to contain it.

# for 3,2,1 it's 2*(3*2 + 3*1 + 2*1) = 2*11 = 22
# for 5,1,1 it's 2*(5*1 + 5*1 + 1*1) = 2*11 = 22

target = 1000

def cubes(a, b, c, l):
    return 2*(a*b + b*c + a*c) + 4*(a + b + c + l - 2)*(l - 1)

assert cubes(3,2,1,1) == 22
assert cubes(3,2,1,2) == 46
assert cubes(3,2,1,3) == 78
assert cubes(3,2,1,4) == 118
assert cubes(5,1,1,1) == 22
assert cubes(5,3,1,1) == 46
assert cubes(7,2,1,1) == 46
assert cubes(11,1,1,1) == 46


def run():
    r = 0
    a = 1
    lim = 30000
    counts = [0]*lim
    while cubes(a, a, a, 1) <= lim:
        b = a
        while cubes(a, b, a, 1) <= lim:
            c = b
            while cubes(a, b, c, 1) <= lim:
                l = 1
                while cubes(a, b, c, l) < lim:
                    n = cubes(a,b,c,l)
                    counts[n] += 1
                    l += 1
                c += 1
            b += 1
        a += 1

    for i, n in enumerate(counts, 0):
        if n == target:
            print(i, n)
            break


if __name__ == '__main__':
    run()
