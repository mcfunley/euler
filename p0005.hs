{-
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
-}
import EulerUtil
a = head $ filter (\x -> foldl1 (&&) $ map (divides x) [2..20]) [2520,2540..]