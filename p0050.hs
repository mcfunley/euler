{-
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
-}
import EulerUtil
import Data.List

data Sum = S { theSum :: Int, nums :: [Int] } deriving Show
mksum :: [Int] -> Sum
mksum xs = S { theSum = sum xs, nums = xs }

emptySum = mksum []

getSum :: Sum -> Int
getSum (S { theSum = s, nums = _ }) = s

getNums :: Sum -> [Int]
getNums (S { theSum = _, nums = ns }) = ns

instance Ord Sum where
    s1 <= s2 = (getSum s1) <= (getSum s2)

instance Eq Sum where
    s == s'        = (getSum s) == (getSum s')

instance Num Sum where
    s1 + s2        = mksum $ (getNums s1) ++ (getNums s2)
    s1 - s2        = mksum $ (getNums s1) ++ (map negate $ getNums s2)
    s1 * s2        = mksum [(getSum s1) * (getSum s2)]
    abs s          = abs $ mksum [abs $ getSum s]
    signum s       = signum $ mksum [-1]
    fromInteger i  = mksum [fromIntegral i]
    
primeSum = isPrime . getSum

cprimes n = map (\n' -> take n $ drop n' primes) [0..]

sumsBelow :: Int -> Int -> [Sum]
sumsBelow n max = takeWhile (< (mksum [max])) $ map mksum $ cprimes n

primeSumsBelow n max = filter primeSum $ sumsBelow n max

biggestPrimeSum n max = longestRun $ emptySum : primeSumsBelow n max

maxRun max = takeToSum 0 0 primes where
    takeToSum n acc (p : ps) | acc < max = takeToSum (n+1) (acc+p) ps
                             | otherwise = (n-1)

longestRun :: [Sum] -> Sum
longestRun = maximumByKey (length . getNums) 

longestPrimeRun max = head $ filter (/=emptySum) $ map (\n -> biggestPrimeSum n max) [n, n-1..1] where n = maxRun max

