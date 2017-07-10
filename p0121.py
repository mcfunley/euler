#!/usr/bin/env python
from itertools import combinations
import numpy as np

def win_prob(turns):
    s = 0
    for blues in range(turns // 2 + 1, turns + 1):
        for winning_trials in combinations(range(1, turns+1), blues):
            probabilities = ([1/(t+1) for t in range(1, turns+1)
                              if t in set(winning_trials)] +
                             [t/(t+1) for t in range(1, turns+1)
                              if t not in set(winning_trials)])
            s += np.prod(probabilities)
    return s

print(win_prob(4))
print(win_prob(15))
print(int(1/win_prob(15)))
