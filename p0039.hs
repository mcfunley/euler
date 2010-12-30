{-

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?
-}
{-
a^2 + b^2 = c^2
a+b+c = perim
-}
import EulerUtil
import Data.List
same (a,b,_) (a',b',_) = (a,b) == (b',a')
solutions p = nubBy same [(a,b,c) | a <- [1..p-2], 
                                    b <- [a..p-a-1], 
                                    c <- [sqrt $ a*a+b*b],
                                    a+b+c==p]
nsol = length . solutions
answer = maximumByKey snd $ map (\n -> (n, nsol n)) [3..999]