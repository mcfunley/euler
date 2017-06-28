#!/usr/bin/env python

# t = r + b > 1e12
# b / t * (b - 1) / (t - 1) = 1/2
# (b * (b - 1)) / (t * (t - 1)) = 1/2
# 2b^2 - 2b - t^2 + t = 0

b = 15
t = 21
target = 1e12

while t < target:
    b2 = 3*b + 2*t - 2
    t2 = 4*b + 3*t - 3
    b = b2
    t = t2

print(b, t)
print((b / t) * ((b - 1) / (t - 1)))
