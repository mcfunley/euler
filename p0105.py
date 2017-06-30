#!/usr/bin/env python
from p0103 import is_special


def sets():
    for l in open('p105_sets.txt', 'r').readlines():
        yield { int(n) for n in l.strip().split(',') }


rs = 0
for s in sets():
    if is_special(s):
        rs += sum(s)

print(rs)
