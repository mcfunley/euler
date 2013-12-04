def gcd(a, b):
    while b != a:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
