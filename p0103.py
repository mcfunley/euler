#!/usr/bin/env python
from itertools import combinations, combinations_with_replacement
import math


def generate_subsets(s):
    for i in range(1, len(s) // 2 + 1):
        for ielems in combinations(s, i):
            a = set(ielems)
            for j in range(1, len(s) - i + 1):
                for jelems in combinations(s - a, j):
                    yield a, set(jelems)


def is_special(s):
    for a, b in generate_subsets(s):
        sa = sum(a)
        sb = sum(b)
        if sa == sb:
            return False

        if len(a) > len(b) and sa <= sb:
            return False

        if len(b) > len(a) and sb <= sa:
            return False
    return True


def set_string(s):
    return ''.join([str(d) for d in sorted(s)])


def next_near_optimum(s):
    mid = int(len(s) / 2)
    middle = list(sorted(s))[mid]
    next_set = { middle }
    for elem in s:
        next_set.add(elem + middle)
    return next_set


def update_vectors(s):
    start = -4
    end = 4

    def update(vec):
        for i in reversed(range(len(s))):
            if vec[i] == end:
                continue
            for j in range(i+1, len(s)):
                vec[j] = start
            vec[i] += 1
            return vec
        return vec

    vec = [start]*len(s)
    for _ in range((end - start + 1)**len(s)):
        yield vec[:]
        vec = update(vec)


def generate_optimal_candidates(s):
    # candidates are s + a vector of additions and subtractions, the vector
    # should have a sum of < 0.
    elems = list(sorted(s))
    for vec in update_vectors(s):
        candidate = { max(1, e+v) for e, v in zip(elems, vec) }
        if len(candidate) < len(s):
            continue
        yield candidate


def find_optimal(near_optimal):
    # brute force it
    minimum = near_optimal
    for candidate in generate_optimal_candidates(near_optimal):
        if sum(candidate) < sum(minimum) and is_special(candidate):
            minimum = candidate
    return minimum


def pprint_set(s):
    return '{%s}' % (', '.join([str(d) for d in sorted(s)]))


def solve():
    s = {1}
    for n in range(1, 8):
        l = 'n = %d: %s' % (n, pprint_set(s))
        print('%-40s %s' % (l, 'special' if is_special(s) else '-'))
        optimal = find_optimal(s)
        if optimal != s:
            print('    optimal: %s (%s)' % (pprint_set(optimal), set_string(optimal)))
        s = next_near_optimum(s)

if __name__ == '__main__':
    solve()
