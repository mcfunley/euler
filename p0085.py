#!/usr/bin/env python


def count_rectangles(n, m):
    r = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            x = r 
            r += (n - i + 1) * (m - j + 1)
    return r


class Solution(object):
    def __init__(self, m, n, r):
        self.m = m
        self.n = n
        self.r = r
        self.area = m*n

    def better(self, other):
        if other is None:
            return self

        if abs(2e6 - self.r) < abs(2e6 - other.r):
            return self

        return other


def main():
    soln = None
    
    for n in range(1, 100):
        for m in range(1, 100):
            r = count_rectangles(m, n)
            soln = Solution(m, n, r).better(soln)
            if r >= 2e6:
                return soln

if __name__ == '__main__':
    soln = main()
    print soln.m, soln.n, soln.r, soln.area

    
        

