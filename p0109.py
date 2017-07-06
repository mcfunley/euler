#!/usr/bin/env python
import numpy as np
from itertools import combinations

singles = list(range(1, 21)) + [25]

board = {
    'S%d' % s: s for s in singles
}
board.update({
    'D%d' % s: s*2 for s in singles
})
board.update({
    'T%d' % s: s*3 for s in singles
})
del board['T25']

doubles = [(k, v) for k, v in board.items() if k.startswith('D')]

# have to do this in combinations of three darts to finish.

def checkout_combinations(n, choices, hist):
    if len(choices) == 0 or len(hist) == 3:
        return

    for name, v in choices.items():
        if v == n:
            yield [name] + hist
        else:
            for c in checkout_combinations(n - v, choices, [name] + hist):
                yield c


def identify(checkout):
    return ','.join(sorted(checkout[0:-1]) + [checkout[-1]])


def dedupe(checkouts):
    result = set()
    for c in checkouts:
        cid = identify(c)
        if cid not in result:
            result.add(cid)
            yield cid


def count_checkouts(n):
    total = 0

    for name, d in doubles:
        if d == n:
            total += 1
        elif d < n:
            # need to count the ways to sum to the remainder with any
            # combination of singles/doubles/triples.
            for c in dedupe(checkout_combinations(n - d, board, [name])):
                total += 1

    return total


checkouts = 0
for score in range(1, 100):
    print(score, checkouts)
    checkouts += count_checkouts(score)

print()
print(checkouts)
