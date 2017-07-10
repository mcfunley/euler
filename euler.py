from math import sqrt

def digits(n):
    result = []
    while n:
        result.append(n % 10)
        n //= 10
    return list(reversed(result))


def from_digits(ds):
    return sum(n*10**i for i, n in enumerate(reversed(ds)))


def partitions(xs):
    "Generates all in-order partitions of a list xs"
    yield [xs]

    if len(xs) == 1:
        return

    for i in range(1, len(xs)):
        yield [xs[:i], xs[i:]]

        first = True
        for p in partitions(xs[i:]):
            if first:
                first = False
                continue
            yield [xs[:i]] + p


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
