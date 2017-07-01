#!/usr/bin/env python
from scipy.misc import comb

# for n=4, the set sizes are (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (3, 1)
# there are comb(4, 1)*comb(3, 2) ways to make (1, 2) + (2, 1) and so on
# don't care about ordering so count halves.
#
# 25 = comb(4, 1) * comb(3, 1) / 2 +
#      comb(4, 1) * comb(3, 2) +
#      comb(4, 1) * comb(3, 3) +
#      comb(4, 2) * comb(2, 2) / 2

def subset_pair_count(n):
    s = 0
    for a in range(1, n):
        for b in range(1, n - a + 1):
            s += comb(n, a) * comb(n - a, b) / 2
    return int(s)

# the sets are strictly increasing, so if len(a) < len(b) we know they aren't
# equal.

def count_first_rule_required(n):
    pairs = subset_pair_count(n)

    # none of the (1, 1) pairs are equal because none of the elements are equal.
    pairs -= comb(n, 1) * comb(n - 1, 1) / 2

    # since the second rule is satisfied, none of the pairs with unequal sizes
    # are equal
    for a in range(1, n):
        for b in range(1, n - a + 1):
            if a != b:
                pairs -= comb(n, a) * comb(n - a, b) / 2

    # the remaining pairs are sets of equal size. for these we need to check
    # cases where each element in the first half of S(A) is paired with an
    # element in the second half of S(A), since these could have equal sums.
    # https://en.wikipedia.org/wiki/Catalan_number
    for i in range(2, n // 2 + 1):
        cat = 1 / (i + 1) * comb(2*i, i)
        pairs -= cat * comb(n, 2*i)

    return int(pairs)

print(count_first_rule_required(4))
print(count_first_rule_required(7))
print(count_first_rule_required(12))
