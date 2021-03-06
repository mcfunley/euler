{-
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference is pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
-}
import Control.Monad
import Data.List
import EulerUtil
p n = n * (3 * n - 1) `div` 2
p' n = 3 * n - 0.5 
d k j = abs $ (p k) - (p j)
d' k j = 6*k - 6*j - 2
pens = map p [1..]
--isPen = hashMemoInt $ \n -> (head $ dropWhile (<n) pens) == n

pens' = intMembershipLookup $ take 100000 pens
isPen = lookupWithDefault pens' False 

match a b = isPen (pa + pb) && isPen (abs $ pa - pb) where
    pa = p a
    pb = p b

range = 10000

{-
So for any constant difference that is a pentagonal,

Pn = [ k(3k - 1) - j(3j - 1) ] / 2
2*Pn = 3k^2 - k - 3j^2 + j

And there is a corresponding sum that is a pentagonal

Pn' = [ k(3k - 1) + j(3j - 1) ] / 2
2*Pn' = 3k^2 - k + 3j^2 - j

2*Pn' = 2*Pn + 6j^2 - 2j
Pn' = Pn + 3j^2 - j
Pn = Pn' - 3j^2 + j

Given two numbers k, j | k > j whose sum is a pentagonal Pn', Pn' - 3j^2 + j should 
also be pentagonal.

And,
Pn > 0
[ k(3k - 1) - j(3j - 1) ] / 2 > 0
k(3k - 1) - j(3j - 1) > 0

(that was fairly useless, brute forcing did it)

-}

pairs = [(j, k) | k <- [1..], j <- [1..k], isPen (p k + p j)]
diffs = filter (\(j, k) -> isPen (p k - p j)) pairs

-- j = 1020, k = 2167

--pairs = filter (\[a : b : _] -> isPen (a+b) && isPen (b-a)) $ replicateM 2 pens
