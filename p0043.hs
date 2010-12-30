{-
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    * d2d3d4=406 is divisible by 2
    * d3d4d5=063 is divisible by 3
    * d4d5d6=635 is divisible by 5
    * d5d6d7=357 is divisible by 7
    * d6d7d8=572 is divisible by 11
    * d7d8d9=728 is divisible by 13
    * d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
-}
import EulerUtil
divisors = [2,3,5,7,11,13,17]

secs x = map digitsToNum $ filter (\xs -> length xs > 2) $ map (\n -> take 3 $ drop n $ digits x) [1..7]

foo :: Integer -> Bool
foo x = all (==0) $ zipWith rem (secs x) divisors

startsWith n (x : xs) = x == n && xs == []

match :: [Int] -> Bool
match ls = (not $ startsWith 0 ls) && (foo $ digitsToNum ls)

pans :: [Integer]
pans = map (fromIntegral . digitsToNum) $ matchPermutations match [0..9]

answer = sum pans
