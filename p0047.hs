{-
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?
-}
import EulerUtil
import Data.List
num = 4
df = nub . factor
ns n = map (+n) [0..num-1]
pfcount n = map (length . df) $ ns n
matches n = all (==num) $ pfcount n
answer = filter matches [1..]
