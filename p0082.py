#!/usr/bin/python
import networkx as nx
import sys

data = """131,673,234,103,18
201,96,342,965,150
630,803,746,422,111
537,699,497,121,956
805,732,524,37,331
""".splitlines()
data = open('matrix.txt', 'r').readlines()

matrix = [map(int, l.split(',')) for l in data]

max_row = len(matrix) - 1
max_col = len(matrix[0]) - 1

def node(r, c):
    return '(%d, %d) %d' % (r, c, matrix[r][c])

def node_self_size(n):
    return int(n.split(' ')[2])

g = nx.DiGraph()
for r in range(0, len(matrix)):
    for c in range(0, len(matrix[0])):
        n = node(r, c)
        g.add_node(n)

        if r > 0:
            # up path
            g.add_edge(n, node(r-1, c), weight=matrix[r-1][c])

        if c < max_col:
            # right path
            g.add_edge(n, node(r, c+1), weight=matrix[r][c+1])

        if r < max_row:
            # down path
            g.add_edge(n, node(r+1, c), weight=matrix[r+1][c])

def path_string(path):
    return ' -> '.join([str(node_self_size(n)) for n in path])

def path_weight(path):
    weight = node_self_size(path[0])
    for a, b in zip(path, path[1:]):
        weight += g.edge[a][b]['weight']
    return weight

best = None
best_weight = sys.maxint
for r_start in range(0, len(matrix)):
    for r_end in range(0, len(matrix)):
        node_start = node(r_start, 0)
        node_end = node(r_end, max_col)
        path = nx.weighted.dijkstra_path(g, node_start, node_end)
        w = path_weight(path)
        if w < best_weight:
            best_weight = w
            best = path

    print '%d of %d' % (r_start+1, len(matrix))

print path_string(best)
print best_weight
