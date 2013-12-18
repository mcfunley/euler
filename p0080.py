#!/usr/bin/python
from decimal import *
getcontext().prec = 110

total = 0
for i in range(1, 101):
    d = Decimal(i).sqrt()
    if d == int(d):
        continue
    digits = str(d).replace('.', '')[:100]
    total += sum(map(int, digits))

print total

