#!/usr/bin/env python

def min_product_sums(kmax):
    n = [2*kmax] * kmax

    def prodsum(p, s, c, start):
        # product - sum + number of factors
        k = p - s + c
        if k < kmax:
            if p < n[k]:
                n[k] = p
            for i in range(start, kmax//p * 2):
                prodsum(p*i, s+i, c+1, i)

    prodsum(1, 1, 1, 2)
    return n[2:]

print sum(set(min_product_sums(12000)))
