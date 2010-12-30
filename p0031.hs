{-
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
-}
import Control.Monad
import Data.List

coins = [200,100,50,20,10,5,2,1]

total counts = sum $ zipWith (*) counts coins

range counts = let c = coins !! (length counts)
                   left = 200 - total counts
               in [0..left `div` c]

ways = length [(a,b,c,d,e,f,g,h) | a <- range [], 
                            b <- range [a], 
                            c <- range [a,b], 
                            d <- range [a,b,c], 
                            e <- range [a,b,c,d], 
                            f <- range [a,b,c,d,e],
                            g <- range [a,b,c,d,e,f], 
                            h <- range [a,b,c,d,e,f,g],
                            total [a,b,c,d,e,f,g,h] == 200]





-- setsOfSize 2 []     -> []
-- setsOfSize 2 [1]    -> [[1, 1]]
-- setsOfSize 2 [2, 1] -> [[2, 2], [2, 1]] ++ setsOfSize 2 [1]

--setsMatching p (x : xs) = combinanations 

--make200 = filter ((==200) . sum) $ concatMap (\n -> replicateM n $ coins n) [1..200]
--answer = length . nub $ map sort make200
