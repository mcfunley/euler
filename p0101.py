#!/usr/bin/env python
from itertools import count
from io import StringIO
import numpy
from numpy import matmul


def f(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

def vandermode(xs, degree):
    return numpy.array([
        [x**i for i in range(degree+1)]
        for x in xs
    ])

correct_values = [f(n) for n in range(1, 100)]

def fit(values, degree):
    return numpy.polyfit(range(1, len(values)+1), values, degree)


def pprint_fit(fit):
    buf = StringIO()
    for i, coeff in enumerate(reversed(fit)):
        if i == 1:
            if coeff < 0:
                buf.write(' - %sn' % abs(coeff))
            else:
                buf.write(' + %sn' % coeff)
        elif i > 0:
            if coeff < 0:
                buf.write(' - %sn**%s' % (abs(coeff), i))
            else:
                buf.write(' + %sn**%s' % (coeff, i))
        else:
            buf.write(str(coeff))
    return buf.getvalue()

debug = lambda *xs: None
# debug = print

def op(k):
    return fit(correct_values[:k], k - 1)

# fuck float64 stuff just hardcode it out
def fitfunc(k):
    def f(coeffs):
        def p(n):
            return sum([a*(n**i) for i, a in enumerate(coeffs)])
        return p

    if k == 0:
        return f([1])
    elif k == 1:
        return f([-681, 682])
    elif k == 2:
        return f([42241, -63701, 21461])
    elif k == 3:
        return f([-665807, 1234387, -686587, 118008])
    elif k == 4:
        return f([4379761, -9277213, 6671533, -1984312, 210232])
    elif k == 5:
        return f([-14707439, 34305227, -29116967, 11535788, -2175668, 159060])
    elif k == 6:
        return f([27442801, -68962861, 65955241, -31492582, 8069182, -1070322, 58542])
    elif k == 7:
        return f([-28828799, 76941359, -80663539, 44083303, -13814218,
                  2524808, -254078, 11165])
    elif k == 8:
        return f([15966721, -44806465, 50572225, -30669221, 11126621,
                  -2514688, 352528, -28831, 1111])
    elif k == 9:
        return f([-3628799, 10628639, -12753575, 8409499, -3416929, 902054,
                  -157772, 18149, -1319, 54])

def first_incorrect(k):
    p = fitfunc(k)
    debug('k = %s' % k)

    for n, correct in enumerate(correct_values):
        v = p(n+1)
        debug('   %02d correct: %s, predicted: %s' % (n, correct, v))
        if v != correct:
            debug('      %s is wrong' % v)
            return v
    return None

print(sum(first_incorrect(k) for k in range(10)))
