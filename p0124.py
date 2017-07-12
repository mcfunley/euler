#!/usr/bin/env python
from operator import itemgetter

maxrad = 100001
target_k = 10000

# maxrad = 11
# target_k = 10

rads = [{ 'r': 1, 'n': n } for n in range(maxrad)]

def sortrads():
    return sorted(rads, key=lambda d: (d['r'], d['n']))

def dump():
    for k, d in enumerate(sortrads()):
        print('%20s %20s %20s' % (d['n'], d['r'], k))
        if k == target_k:
            break

for i in range(2, maxrad):
    if rads[i]['r'] == 1:
        rads[i]['r'] = i

        for j in range(i + i, maxrad, i):
            rads[j]['r'] = rads[j]['r'] * i

print(sortrads()[target_k])

# print(sorted(rads, key=lambda d: (d['r'], d['n']))[10001])
