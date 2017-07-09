#!/usr/bin/env python
from functools import lru_cache

# correct but slow solution

def placements(row, redsize):
    last = len(row) - redsize

    def empty(i):
        return all([r == 0 for r in row[i:i+redsize]])

    def free(i):
        return (i == 0 or row[i-1] == 0) and (i == last or row[last+1] == 0)

    return (i for i in range(0, last+1) if empty(i) and free(i))


def place(row):
    # place one red block of all legal sizes everywhere possible then recurse
    total = 0
    for redsize in range(3, len(row) + 1):
        for placement in placements(row, redsize):
            r = row[:]
            r[placement:placement+redsize] = [1]*redsize
            total += 1 + place(r)
    return total

def solve_slow_memory_hog(rowlen):
    row = [0] * rowlen
    return 1 + place(row)

# one for empty
# one for every position between 0 and sz - length inclusive, for lengths b/t 3 and sz
# then all solutions for the remaining array minus spacer(s)

@lru_cache(maxsize=100)
def solve(rowlen):
    if rowlen < 3:
        # empty only
        return 1

    # one for empty
    total = 1
    for redlen in range(3, rowlen+1):
        for i in range(0, rowlen - redlen + 1):
            remainder = rowlen - (i + redlen) - 1
            total += solve(remainder)
    return total

print(solve(7))
print(solve(6))
print(solve(50))
