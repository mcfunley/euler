from math import sqrt

def gcd(a, b):
    while b != a:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


_bad_h = { 2, 3, 5, 6, 7, 8 }

# make sure n is an integer
def is_perfect_square(n):
    if n == 0:
        return False

    h = n & 0xf
    if h > 9:
        return False

    if h not in _bad_h:
        t = int(sqrt(n))
        return t*t == n

    return False
