{-
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
-}
import EulerUtil
import Control.Monad
d = hashMemoInt $ sum . properFactors
pairs = [(a, b) | a <- [1..9999], b <- [1..(a-1)]]
amicablePairs = filter (\(a, b) -> d a == b && d b == a) pairs
answer = foldl (\c (a, b) -> a + b + c) 0 amicablePairs

-- [(284,220),(1210,1184),(2924,2620),(5564,5020),(6368,6232)]