{- 
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this
property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime. 
-}
import Control.Monad
import Utils
import Data.BloomFilter
import qualified Data.HashTable as H
import qualified Data.Set as S
import System.IO.Unsafe
import Data.List (sortBy)

groupLen = 5


main = do 
  ps <- primes
  filt <- primeFilter' ps

  let checkPair a b = ((concatInts a b) `elemB` filt) &&
                      ((concatInts b a) `elemB` filt)
      groups = [(sum g, g) | g <- findGroups checkPair $ drop 1 ps]

  mapM_ (putStrLn . show) $ take 5 groups


printLasts [] = []
printLasts xs@(x : _) = unsafePerformIO $ do putStrLn . show . last $ x
                                             return xs


-- find all elements of ps that match with p as well as with each other
findGroups :: (Num a, Ord a) => (a -> a -> Bool) -> [a] -> [[a]]
findGroups checkPair ps = filter (\x -> length x == groupLen) groups where 
    groups = printLasts $ findGroups' checkPair [] ps


findGroups' :: (Num a, Ord a) => (a -> a -> Bool) -> [a] -> [a] -> [[a]]
findGroups' _ ms [] = [ms]
findGroups' checkPair ms (p : ps) 
    | length ms == groupLen = [ms]
    | p > 10000 = [ms]
    | otherwise = 
        let discarded = findGroups' checkPair ms ps
        in if all (checkPair p) ms 
           then (findGroups' checkPair (p : ms) ps) ++ discarded
           else discarded

