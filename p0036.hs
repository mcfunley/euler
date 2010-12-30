{-
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
-}
import EulerUtil

nums :: [Int]
nums = takeWhile (<1000000) [1..]

isPalindrome xs = xs == xs' where
    xs' = reverse xs

isTwoBasePal n = all isPalindrome [show n, showBinary n]

twoBasePals = filter isTwoBasePal nums

answer = sum twoBasePals