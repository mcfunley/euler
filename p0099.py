#!/usr/bin/env python

def _numbers():
    for i, l in enumerate(open('p099_base_exp.txt', 'r').readlines()):
        base, exponent = [int(x) for x in l.split(',')]
        yield i+1, base, exponent

numbers = { line: (base, exponent) for line, base, exponent in _numbers() }

while len(numbers) > 1:
    # for every b**e and b**e2, raise both sides to 1/(e*e2) which retains
    # the direction of the inequality and compare. Drop from the dict until
    # only one is left.

    it = iter(list(numbers.items()))
    line, (b, e) = next(it)

    for line2, (b2, e2) in it:
        cb = b ** (1 / e2)
        cb2 = b2 ** (1 / e)
        if cb < cb2:
            print('%s**%s < %s**%s' % (b, e, b2, e2))
            del numbers[line]
            break
        else:
            print('%s**%s > %s**%s' % (b, e, b2, e2))
            del numbers[line2]

print(numbers)
