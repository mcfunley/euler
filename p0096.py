#!/usr/bin/env python
from io import StringIO

def puzzles(debug=False):
    puzzle = []
    for l in open('p096_sudoku.txt', 'r').readlines():
        if 'Grid' in l:
            if len(puzzle):
                yield Puzzle(puzzle, debug)
                puzzle = []
            continue

        puzzle.append([int(d) for d in l.strip()])

    yield Puzzle(puzzle, debug)


def matrix_to_string(matrix):
    buf = StringIO()
    for i, row in enumerate(matrix):
        for grp in zip(*[iter(row)]*3):
            buf.write('%d %d %d | ' % grp)
        buf.seek(buf.tell() - 2)
        buf.write(' \n')

        if i == 2 or i == 5:
            buf.write('-' * (len('9 9 9')*3 + 6))
            buf.write('\n')

    return buf.getvalue()


class Puzzle(object):
    def __init__(self, matrix, debug=False):
        self.debug = print if debug else lambda *xs: None
        self.matrix = matrix
        self.original = [row.copy() for row in matrix.copy()]
        self.visited = {}
        self.failed_moves = [[set() for _ in row] for row in self.matrix]

    def is_fixed(self, i, j):
        return self.original[i][j] != 0


    def gridvalues(self, i, j):
        start_i = int(i / 3) * 3
        start_j = int(j / 3) * 3
        for ci in range(3):
            for cj in range(3):
                yield self.matrix[start_i + ci][start_j + cj]


    def legal_moves(self, i, j):
        if self.is_fixed(i, j):
            return []

        column_vals = { row[j] for row in self.matrix } - {0}
        row_vals = set(self.matrix[i]) - {0}
        square_vals = set(self.gridvalues(i, j)) - {0}

        not_tried = {
            d for d in range(1, 10) if d not in self.failed_moves[i][j]
        }

        return list(not_tried - (column_vals | row_vals | square_vals))


    def fail_move(self, i, j, n):
        self.failed_moves[i][j].add(n)


    def backtrack(self, i, j):
        if (i, j) == (0, 0):
            raise Exception()

        self.failed_moves[i][j] = set()
        del self.visited['%s,%s' % (i, j)]

        if i > 0:
            i, j = i - 1, j
        else:
            i, j = 8, j - 1

        if not self.is_fixed(i, j):
            self.failed_moves[i][j].add(self.matrix[i][j])
            self.matrix[i][j] = 0

        return i, j


    def next_coord(self, i, j):
        if (i, j) == (8, 8):
            return None

        if i < 8:
            return i + 1, j
        return 0, j + 1


    def advance(self, guess, i, j):
        self.matrix[i][j] = guess
        return self.next_coord(i, j)


    def visit(self, legal, i, j):
        legal = set(legal)
        failed = set(self.failed_moves[i][j])

        k = '%s,%s' % (i, j)
        if k not in self.visited:
            self.visited[k] = [[failed, legal]]
            return False

        sets = self.visited[k]
        for f, s in sets:
            if s == legal and f == failed:
                return True

        self.visited[k].append([failed, legal])
        return False


    def solve(self):
        coord = (0, 0)

        while coord:
            i, j = coord

            m = self.legal_moves(*coord)
            self.debug('at: (%s, %s)' % coord, 'with moves', m,
                       'and failed moves', self.failed_moves[i][j])

            if self.visit(m, *coord):
                self.debug('    visited before, going back')
                coord = self.backtrack(*coord)
            elif self.is_fixed(*coord):
                # it's a fixed value, we have to go forward
                self.debug('    fixed as %s, moving forward' %
                           self.original[i][j])
                coord = self.next_coord(*coord)
            elif len(m) == 0:
                # no choices left, go back
                coord = self.backtrack(*coord)
                self.debug('    backtrack to (%s, %s)' % coord)
            else:
                # try the first choice
                coord = self.advance(m[0], *coord)
                if coord:
                    self.debug('    setting to %s' % m[0],
                               'and advancing to (%s, %s)' % coord)

        return self


    def top_left_three(self):
        row = self.matrix[0]
        return row[0]*100 + row[1]*10 + row[2]


    def __str__(self):
        orig = matrix_to_string(self.original)
        current = matrix_to_string(self.matrix)

        buf = StringIO()
        for ol, cl in zip(orig.splitlines(), current.splitlines()):
            print('%s     %s' % (ol.strip(), cl.strip()), file=buf)
        return buf.getvalue()

s = 0
for i, p in enumerate(puzzles()):
    p.solve()
    s += p.top_left_three()
    print('Solved', i+1)

print(s)
