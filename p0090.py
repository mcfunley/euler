#!/usr/bin/env python
from itertools import combinations, count


squares = [(0,1), (0,4), (0,6), (1,6), (2,5), (3,6), (4,6), (8,1)]
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 6,]
cubes = [set(c) for c in combinations(digits, 6)]


def find_match(cube1, cube2, s):
    x, y = s
    return (x in cube1 and y in cube2) or (x in cube2 and y in cube1)


def works(cube1, cube2):
    for s in squares:
        if not find_match(cube1, cube2, s):
            return False
    return True

def arrangements():
    for i, c in enumerate(cubes):
        for c2 in cubes[:i]:
            yield c, c2

def working_arrangements():
    return (a for a in arrangements() if works(*a))


print(sum(1 for _ in working_arrangements()))
