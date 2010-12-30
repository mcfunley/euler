{-
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5 nCr 3 = 10.

In general,
nCr = (n!) / (r!(n−r)!)

where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23 nCr 10 = 1144066.

How many values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
-}
import EulerUtil

matching = [(n, r) | n <- [1..100], r <- [1..n], n `nCr` r > 1000000]
answer = length matching