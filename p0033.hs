{-
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
-}
import Data.Ratio
import EulerUtil
import Data.List

fracs = [(x, y) | y <- [11..99], x <- [10..y-1]]

simplify (x, y) = (numerator f, denominator f)
    where f = x % y

shared (x, y) = intersect (digits x) (digits y)

dropShared fr@(x, y) = let sd = shared fr
                           f a = head $ filter (\d -> not $ elem d sd) $ digits a
                       in (f x, f y)

shareDigit fr@(x, y) = (length (shared fr) > 0) && (length (nub $ (digits x) ++ (digits y)) == 3)

isTrivial fr = elem 0 $ shared fr 

shareDigits = filter shareDigit fracs

valid fr = let ds@(_, y) = dropShared fr 
           in y /= 0 && (simplify fr == simplify ds)

nonTrivial = filter (not . isTrivial) shareDigits

fourFracs = filter valid nonTrivial

answer = product $ map (\(x, y) -> x%y) fourFracs