#!/usr/bin/env python
from math import sqrt
from itertools import combinations


def f(p1, p2, p3):
    return p1**2 + p2**3 + p3**4


def load_primes():
    primes = []
    maxprime = sqrt(50e6)
    print maxprime
    for l in open('primes.txt', 'r'):
        primes.append(int(l))
        if primes[-1] > maxprime:
            break
    return primes


def main():
    # not right because it's legal to reuse primes
    primes = load_primes()

    answers = set()
    tot = 0
        
    for p1 in primes:
        for p2 in primes:
            for p3 in primes:
                if tot % 100000 == 0:
                    print 'Tried', tot, 'combinations'
                
                tot += 1
                v = f(p1, p2, p3)

                if v < 50e6:
                    answers.add(v)
                else:
                    break

    print len(answers)
    

if __name__ == '__main__':
    main()

