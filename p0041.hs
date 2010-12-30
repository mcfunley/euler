{-
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
-}
import EulerUtil
import Data.List
pans = filter (\xs -> length xs > 1) $ inits [1..9]
pandigitalPrimes = filter isPrime $ map digitsToNum $ concatMap permutations pans