#!/usr/bin/env python
from itertools import combinations, permutations, count

digits = range(1, 10)
ops = ['+', '-', '*', '/']


def groupings(ds):
    a, b, c, d = ds
    yield [[a, b], [c, d]]
    yield [[[a, b], c], d]
    yield [[a, [b, c]], d]
    yield [a, [[b, c], d]]
    yield [a, [b, [c, d]]]


def expressions_for_grouping(g):
    if not isinstance(g, list):
        yield str(g)
        return

    left, right = g
    for lexpr in expressions_for_grouping(left):
        for rexpr in expressions_for_grouping(right):
            for op in ops:
                yield '(%s %s %s)' % (lexpr, op, rexpr)


def expressions_for_permutation(ds):
    for g in groupings(ds):
        for expression in expressions_for_grouping(g):
            yield expression

def generate_expressions(ds):
    for p in permutations(ds):
        for e in expressions_for_permutation(p):
            yield e

def positive_integer_targets(ds):
    for e in generate_expressions(ds):
        try:
            result = eval(e)
        except ZeroDivisionError:
            continue
        if result == int(result) and result > 0:
            yield int(result), e

def unique_targets(ds):
    targets = set()
    for result, e in positive_integer_targets(ds):
        targets.add(result)
    return targets

def longest_run(ds):
    targets = sorted(unique_targets(ds))
    for i, t in zip(count(1), targets):
        if i != t:
            return i - 1
    return targets[-1]

def find_longest_run():
    longest = -1
    longest_digits = []
    for ds in combinations(digits, 4):
        r = longest_run(ds)
        if r > longest:
            longest = r
            longest_digits = ds
        print(ds, r)
    return longest_digits, longest

if __name__ == '__main__':
    print(find_longest_run())
