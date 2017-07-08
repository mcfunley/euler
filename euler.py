from math import sqrt

def digits(n):
    def d(n):
        while n:
            yield n % 10
            n //= 10
    return reversed(list(d(n)))


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

def positive_integral_quadratic_solution(a, b, c):
    x = b*b - 4*a*c
    if not is_perfect_square(x):
        return None

    den = 2*a
    num1 = (0-b) + sqrt(x)
    res1 = num1 / den
    if res1 > 0 and num1 % den == 0:
        return int(res1)

    num2 = (0-b) - sqrt(x)
    res2 = num2 / den
    if res2 > 0 and num2 % den == 0:
        return int(res2)

    return None
