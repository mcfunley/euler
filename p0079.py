#!/usr/bin/python
"""
A common security method used for online banking is to ask the user for three 
random characters from a passcode. For example, if the passcode was 531278, 
they may ask for the 2nd, 3rd, and 5th characters; the expected reply would 
be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file 
so as to determine the shortest possible secret passcode of unknown length.
"""
import networkx as nx

attempts = open('keylog.txt', 'r').readlines()
attempts = list(set(attempts))

g = nx.DiGraph()
for a in attempts:
    g.add_edge(int(a[0]), int(a[1]))
    g.add_edge(int(a[1]), int(a[2]))

roots = []
leaves = []
for n in g.nodes():
    if len(g.successors(n)) == 0:
        leaves.append(n)
    if len(g.predecessors(n)) == 0:
        roots.append(n)

shortest = None
for r in roots:
    for l in leaves:
        # hamiltonian paths
        paths = [p for p in nx.all_simple_paths(g, r, l)
                 if len(p) == len(g.nodes())]
        for p in paths:
            if shortest is None or len(p) < len(shortest):
                shortest = p

print ''.join(map(str, shortest))
