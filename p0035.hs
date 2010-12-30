{-
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
-}
import EulerUtil
limit = 1000000

rotations n = let n' = show n
                  l = length n'
                  cs = map (\x -> drop x $ take (l+x) $ cycle n') [0..l-1]
              in map read cs :: [Int]

isPrime' = isPrimeLookup limit

circularPrimes = filter (\n -> all isPrime' $ rotations n) $ takeWhile (<limit) primes

answer = length circularPrimes
