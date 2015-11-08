#!/usr/bin/env python
from itertools import count
    
def int_shortest_path(a, b, c, introots):
    # the shortest straight line distance across is the hypotenuse of a right
    # triangle formed by two of the walls.
    sp = min([
        (d1 + d2)**2 + d3**2
        for d1, d2, d3 in [
                (a, b, c),
                (a, c, b),
                (c, b, a),
        ]
    ])
    return sp in introots
    

def integer_solutions(M):
    introots = { x**2 for x in xrange(1, M**2 + 2*(M**2)) }
    print len(introots)
    solutions = 0
    for m in xrange(1, M+1):
        for n in xrange(m, M+1):
            for p in xrange(n, M+1):
                if int_shortest_path(m, n, p, introots):
                    solutions += 1
    return solutions


if __name__ == '__main__':
    for M in count(101):
        solutions = integer_solutions(M)
        print M, solutions
        if solutions >= 1e6:
            break
        
