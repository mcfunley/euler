#!/usr/bin/python
import sys
from itertools import chain


def find_solutions(arms, digits, a, current):
    digits = set(digits)
    current = current[:]

    solutions = []
    for d in digits:
        if a == 1:
            # first arm, the second digit can be chosen arbitrarily
            edigits = digits - set([d])
            for e in edigits:
                fdigits = edigits - set([e])
                for f in fdigits:
                    remaining = fdigits - set([f])
                    ss = find_solutions(arms, remaining, a+1, [[d, e, f]])
                    solutions.extend(ss)
        else:
            # subsequent arms, the second digit is the last digit of
            # the previous arm.
            e = current[-1][-1]
            if a == arms:
                # last arm, the last digit is the second digit of 
                # the first arm
                f = current[0][1]
                if sum([d,e,f]) == sum(current[0]):
                    return [current + [[d,e,f]]]
                return []

            else:
                # internal arms, the last digit can be chosen from what remains
                fdigits = digits - set([e, d])
                for f in fdigits:
                    if not sum([d,e,f]) == sum(current[-1]):
                        # short circuit any combinations that don't sum to the 
                        # sum of the previous arm
                        continue
                    remaining = fdigits - set([f])
                    nxt = current + [[d, e, f]]
                    ss = find_solutions(arms, remaining, a+1, nxt)
                    solutions.extend(ss)
    return solutions


def soln_string(soln):
    return '; '.join([','.join(map(str, xs)) for xs in soln])


def unique_solutions(arms, max_digit):
    solns = find_solutions(arms, range(1, max_digit+1), 1, [])
    unique_solns = []
    for s in solns:
        min_external = sys.maxint
        min_arm = -1
        for arm in range(0, len(s)):
            if s[arm][0] < min_external:
                min_arm = arm
                min_external = s[arm][0]
        normalized_soln = s[min_arm:] + s[:min_arm]
        if normalized_soln not in unique_solns:
            unique_solns.append(normalized_soln)
    return unique_solns


def digit_string(soln):
    flat = list(chain(*soln))
    return int(str(''.join(map(str, flat))))

def max_digit_string(arms, max_digit, string_len):
    strings = [digit_string(s) for s in unique_solutions(arms, max_digit)]
    return max([s for s in strings if len(str(s)) == string_len])


# for s in unique_solutions(3, 6):
#     total = sum(s[0])
#     print '%d\t%s' % (total, soln_string(s))

print max_digit_string(3, 6, 9)
print max_digit_string(5, 10, 16)


