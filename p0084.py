#!/usr/bin/env python
import re
from itertools import cycle, count
import random
from collections import defaultdict
from operator import itemgetter


class Roll(list):
    def __init__(self):
        sides = 4
        self.append(random.randint(1, sides))
        self.append(random.randint(1, sides))

    def is_double(self):
        return self[0] == self[1]
    

    
class Board(object):
    def __init__(self):
        self.squares = re.sub('\s+', ' ', """
        GO A1 CC1 A2 T1 R1 B1 CH1 B2 B3 JAIL
        C1 U1 C2 C3 R2 D1 CC2 D2 D3 
        FP E1 CH2 E2 E3 R3 F1 F2 U2 F3 G2J
        G1 G2 CC3 G3 R4 CH3 H1 T2 H2
        """).strip().split(' ')

        self.positions = {
            k: n for k, n in zip(self.squares, count(0))
        }

    def get_square_for(self, square, rule):
        if isinstance(rule, int):
            return self.move_places(square, rule)

        if isinstance(rule, Roll):
            return self.move_places(square, sum(rule))

        if isinstance(rule, basestring):
            return rule

        if hasattr(rule, '__call__'):
            return rule(self, square)

        raise Exception("Don't know how to process %s" % rule)

    def move_places(self, square, n):
        pos = self.positions[square] + n
        return self.squares[pos % len(self.squares)]


    
def next_of_type(kind):
    def getsquare(board, square):
        while not square.startswith(kind):
            square = board.move_places(square, 1)
        return square
    return getsquare
    


class Game(object):
    def __init__(self):
        self.board = Board()

        self._community_chest = ['GO', 'JAIL',] + [0]*14
        self._chance = [0]*6 + [
            'GO', 'JAIL', 'C1', 'E3', 'H2', 'R1',
            next_of_type('R'),
            next_of_type('R'),
            next_of_type('U'),
            -3,
        ]

        random.shuffle(self._community_chest)
        random.shuffle(self._chance)

    def _take_card(self, lst):
        c = lst.pop()
        lst.insert(0, c)
        return c

    def chance(self):
        return self._take_card(self._chance)

    def community_chest(self):
        return self._take_card(self._community_chest)


        
class Player(object):
    def __init__(self, game):
        self.square = 'GO'
        self.rolls = []
        self.game = game

    def next_roll(self):
        r = Roll()
        self.rolls.append(r)
        self.rolls = self.rolls[-3:]
        return r

    def third_double(self):
        return all([r.is_double() for r in self.rolls]) and len(self.rolls) == 3

    def move(self):
        r = self.next_roll()
        if self.third_double():
            self.square = 'JAIL'
            return

        self.square = self.game.board.get_square_for(self.square, r)
        if self.square == 'G2J':
            self.square = 'JAIL'
            return

        self.maybe_take_card()

    def maybe_take_card(self):
        original_square = self.square
        
        if self.square.startswith('CH'):
            self.take_card(self.game.chance())
        elif self.square.startswith('CC'):
            self.take_card(self.game.community_chest())

        # if we moved, we may need to take another card
        if original_square != self.square:
            self.maybe_take_card()

    def take_card(self, card):
        self.square = self.game.board.get_square_for(self.square, card)


def sim(moves):
    result = defaultdict(int)
    
    g = Game()
    p = Player(g)
    for _ in range(moves):
        p.move()
        result[p.square] += 1

    return result


def main():
    counters = defaultdict(int)
    
    for _ in range(10000):
        for k, n in sim(400).items():
            counters[k] += n

    total = float(sum(counters.values()))
    pdf = { k: n / total for k, n in counters.items() }

    b = Board()
    answer = []
    for k, p in list(reversed(sorted(pdf.items(), key=itemgetter(1))))[:3]:
        print k, p
        answer.append('%02d' % b.positions[k])

    print
    print ''.join(answer)
    

if __name__ == '__main__':
    main()

