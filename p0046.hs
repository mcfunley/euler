{-
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
-}
import EulerUtil
import Data.Maybe

findSquare num prime = 
    let x = sqrt $ fromIntegral $ (num - prime) `div` 2
    in case isInt x of
         True -> Just (floor x)
         _ -> Nothing

g n = catMaybes $ map (findSquare n) $ takeWhile (<=n) primes

answer = head $ dropWhile (not . null . g) $ [33,35..]