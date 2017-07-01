#!/usr/bin/env python
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import numpy as np

# this is a minimum spanning tree problem.

def graph(encoding):
    def row(l):
        return np.array([0 if w == '-' else int(w) for w in l.split(',')])

    # take upper trianguler, convert to csr matrix
    m = np.array([row(l) for l in encoding.splitlines()])
    return csr_matrix(np.triu(m))


def savings(g):
    mst = minimum_spanning_tree(g)
    return int(np.sum(g) - np.sum(mst))

def solve(g):
    print('Original:')
    print(g.toarray().astype(int))
    print('MST:')
    print(minimum_spanning_tree(g).toarray().astype(int))
    print('\nSavings:', savings(g))


if __name__ == '__main__':
    sample = """
-,16,12,21,-,-,-
16,-,-,17,20,-,-
12,-,-,28,-,31,-
21,17,28,-,18,19,23
-,20,-,18,-,-,11
-,-,31,19,-,-,27
-,-,-,23,11,27,-
""".strip()

    solve(graph(sample))
    print()
    solve(graph(open('p107_network.txt', 'r').read()))
