#!/usr/bin/python
import networkx as nx

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

g = nx.DiGraph()
for r in range(0, len(matrix)):
    for c in range(0, len(matrix[0])):
        n = node(r, c)
        g.add_node(n)

        if c < max_col:
            # right path
            g.add_edge(n, node(r, c+1), weight=matrix[r][c+1])
        if r < max_row:
            # down path
            g.add_edge(n, node(r+1, c), weight=matrix[r+1][c])

start = node(0,0)
end = node(max_row, max_col)

path = nx.weighted.dijkstra_path(g, start, end)
weight = matrix[0][0]
print weight, '->',
for a, b in zip(path, path[1:]):
    w = g.edge[a][b]['weight']
    print w, '->', 
    weight += w

print
print weight
