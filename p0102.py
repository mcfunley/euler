#!/usr/bin/env python
import numpy as np
from itertools import combinations


def magnitude(vector):
   return np.sqrt(np.dot(np.array(vector),np.array(vector)))


def norm(vector):
   return np.array(vector)/magnitude(np.array(vector))


def intersection_point(origin, vector, line):
    p1, p2 = line
    vector = norm(vector)

    v1 = np.array([0, 0]) - p1
    v2 = p2 - p1
    v3 = np.array([-vector[1], vector[0]])
    t1 = np.cross(v2, v1) / np.dot(v2, v3)
    t2 = np.dot(v1, v3) / np.dot(v2, v3)
    if t1 >= 0.0 and t2 >= 0.0 and t2 <= 1.0:
        return origin + t1 * vector
    return None


def triangles():
    for l in open('p102_triangles.txt', 'r').readlines():
        nums = [int(x) for x in l.split(',')]
        yield list(zip(*[iter(nums)] * 2))


def midpoint(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return (x1 + x2) / 2, (y1 + y2) / 2

def contains_origin(triangle):
    p1, p2, p3 = triangle
    s1mid = np.array(midpoint(p1, p2))

    origin = np.array([0, 0])
    intersections = 0
    for segment in combinations(triangle, 2):
        ip = intersection_point(origin, s1mid, [np.array(p) for p in segment])
        if ip is not None:
            intersections += 1

    return intersections % 2 == 1


print(sum(1 for t in triangles() if contains_origin(t)))
