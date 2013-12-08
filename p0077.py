#!/usr/bin/python
"""
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five 
thousand different ways?
"""
primes = []
f = open('primes.txt', 'r')
for p in f.xreadlines():
    primes.append(int(p))
    if len(primes) > 100:
        break

goal = 5000
target = primes[0]
while True:
    ways = { 0: 1 }
    for x in primes:
        for i in xrange(x, target+1):
            ways[i] = ways.setdefault(i - x, 0) + ways.setdefault(i, 0)

    # print ways, target

    if ways[target] >= goal:
        print target
        break

    target += 1
    

        
