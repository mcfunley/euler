#!/usr/bin/env python
from itertools import combinations, permutations
from collections import defaultdict
from euler import is_perfect_square


words = [w[1:-1] for w in open('p098_words.txt', 'r').read().split(',')]


def anagrams():
    index = defaultdict(list)
    for w in words:
        index[''.join(sorted(w))].append(w)

    for ans in [l for l in index.values() if len(l) > 1]:
        for pair in combinations(ans, 2):
            yield pair


def ciphers(word):
    digits = list(range(10))
    letters = set(word)
    for p in permutations(digits, len(letters)):
        yield { l: d for l, d in zip(letters, p) }


def anagram_ciphers(pair):
    a, b = pair
    for c in ciphers(a):
        if c[a[0]] != 0 and c[b[0]] != 0:
            yield c


def cipher_value(word, cipher):
    m = 1
    s = 0
    for l in reversed(word):
        s += cipher[l] * m
        m *= 10
    return s


def square_ciphers(pair):
    a, b = pair
    for c in anagram_ciphers(pair):
        av = cipher_value(a, c)
        bv = cipher_value(b, c)

        if is_perfect_square(av) and is_perfect_square(bv):
            yield c, { a: av, b: bv }


if __name__ == '__main__':
    largest = 0
    largest_pair = None

    for pair in anagrams():
        for cipher, results in square_ciphers(pair):
            print('%-70s %s' % (cipher, results))

            m = max(results.values())
            if m > largest:
                largest_pair = results
                largest = m

    print(largest_pair, largest)
