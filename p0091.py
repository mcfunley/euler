#!/usr/bin/env python
from itertools import product
from math import sqrt

maxcoord = 50
coords = list(product(range(maxcoord+1), range(maxcoord+1)))

def length_squared(p1, p2):
    x1, y1 = p1
    x2, y2, = p2
    return (x2 - x1)**2 + (y2 - y1)**2

def is_right_triangle(p1, p2):
    a, b, h = sorted([length_squared([0, 0], p1), length_squared([0, 0], p2), length_squared(p1, p2)])
    return h == a + b

def triangles():
    for i, p1 in enumerate(coords[1:]):
        for p2 in coords[1:][:i]:
            if p1 == p2:
                continue
            yield p1, p2

def right_triangles():
    return (t for t in triangles() if is_right_triangle(*t))

print(sum(1 for _ in right_triangles()))
