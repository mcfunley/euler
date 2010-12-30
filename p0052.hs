{-
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
-}
import EulerUtil

isAnaInt x y = isAnagram (digits x) (digits y)
anaMultiples x = map (\m -> isAnaInt x $ m*x) [2..6]
answer = head $ filter (\x -> all id (anaMultiples x)) [1..]
