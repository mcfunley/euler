module Utils (primes, primeFilter, primeFilter', perms, combs, pairs, 
              concatInts) where

import Data.Permute
import Data.Permute.MPermute
import Data.BloomFilter.Easy
import Control.Monad
import Math.Combinat.Combinations


primes = readFile "primes" >>= \s -> do 
           putStrLn "reading primes"
           return $ map readInt $ lines s
    where readInt x = read x :: Int

-- Returns a bloom filter containing the first few million primes. 
primeFilter' = return . (easyList 0.001)
primeFilter = primes >>= primeFilter'

perms' xs p = 
    case next p of
      Just p' -> (map (xs!!) (elems p')) : perms' xs p'
      Nothing -> []

-- Permutations of a list
perms xs = perms' xs (permute $ length xs)

-- combinations of size n from a list
combs :: Int -> [a] -> [[a]]
combs n xs@(x : xs') | n == 0         = [[]]
                     | length xs == n = [xs] 
                     | otherwise      = (map (x:) $ combs (n-1) xs') ++ (combs n xs')

-- Returns unique pairs of items from xs
pairs xs = [(a, b) | a <- xs, b <- xs, a /= b]

-- concatInts 3 4 = 34
concatInts x y = x*(mag 1) + y where
    mag n = if n > y then n else mag (10*n)
