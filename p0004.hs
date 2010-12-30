{-
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
o-}
import Control.Monad
p = maximum $ filter (\x -> (show x) == (reverse $ show x)) $ map product $ replicateM 2 [100..999]