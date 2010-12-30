{-
The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

-}
import EulerUtil
import Data.List
nums = [1..9]

splitEvery list minLeft minRight = map ((flip splitAt) list) [minLeft..length list - minRight]

equations' perm = let firsts = splitEvery perm 1 2
                      eqs (first, rest) = map (\(r, e) -> (first, r, e)) $ splitEvery rest 1 1
                  in concatMap eqs firsts

equations perm = map (\(x,y,z) -> (digitsToNum x, digitsToNum y, digitsToNum z)) $ equations' perm

trueEquations perm = filter (\(x,y,z) -> x*y==z) $ equations perm

answers = concatMap trueEquations $ permutations nums

answers' = [(12,483,5796),(138,42,5796),(157,28,4396),(159,48,7632),(1738,4,6952),(18,297,5346),(186,39,7254),(1963,4,7852),(198,27,5346),(27,198,5346),(28,157,4396),(297,18,5346),(39,186,7254),(4,1738,6952),(4,1963,7852),(42,138,5796),(48,159,7632),(483,12,5796)]

products = nub $ map (\(_,_,x) -> x) answers'