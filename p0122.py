#!/usr/bin/env python
import sys

maxk = 200
m = {}


def back(xs):
    while len(xs) > 0 and xs[-1] >= maxk:
        xs = xs[:-1]

    return xs


def iterate(xs):
    if len(xs) == 0:
        return

    v = xs[-1]
    if v > maxk:
        return

    path = len(xs) - 1
    if m.get(v, 1e100) < path:
        return

    m[v] = path
    for x in xs:
        iterate(xs + [x + v])


def solve():
    xs = [1]
    while xs[-1] < maxk:
        xs.append(xs[-1]*2)
        m[xs[-1]] = len(xs) - 1

    while len(xs):
        xs = xs[:-1]
        iterate(xs)

solve()

for i in range(1, maxk+1):
    print(i, m.get(i, None))

print(sum(m[k] for k in range(1, maxk+1)))
