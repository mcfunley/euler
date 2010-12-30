module EulerUtil (primes, factor, divides, factors, hashMemo, hashMemoInt,
                  unroll, maxM, sumDigits, fac, properFactors,
                  lookupWithDefault, nPr, fibs, maximumByKey, digits, bigPower,
                  swap, permutations, digitsToNum, isPrime, isPrimeLookup,
                  showBinary, isPandigital, readCsvQuoted, isPandigital9,
                  isPandigital0, matchPermutations, unsafePrint,
                  intMembershipLookup, quadratic, isInt, digitCount,
                  combinations, isAnagram, nCr, replace, isPalindrome,
                  numIsPalindrome, reverseNum, concatNums, concatInts, disjoint, 
                  isPrimeMemo, nub') where

import Data.HashTable
import Data.Int
import System.IO.Unsafe
import Data.IORef
import Control.Monad
import Data.List
import Data.Char
import Data.Bits
import Control.Exception
import qualified Data.Set as S

-- faster nub for Ord.
nub' :: (Ord a) => [a] -> [a]
nub' = go S.empty
  where go _ [] = []
        go s (x:xs) | S.member x s = go s xs
                    | otherwise    = x : go (S.insert x s) xs

isInt n = let (_, f) = properFraction n in f == 0

type Prime = Int64

-- List of all of the primes.
primes :: [Prime]
primes = 2 : filter isP [3,5..] where
   f x p r = x < p*p || mod x p /= 0 && r
   isP x = foldr (f x) True primes

isPrime n | n == 2 = True
          | otherwise = isP primes where
          isP (p : ps) = let (d, m) = n `divMod` p
                         in if m == 0 then False 
                            else if d < p then True
                                 else isP ps

primesToRoot n = takeWhile (<=lim) primes
    where lim :: Prime
          lim = ceiling $ sqrt (fromIntegral n)

-- test for primes using a hash table for memoization.
isPrimeMemo n | n == 2    = True
              | even n    = False
              | otherwise = isPrimeMemo' n
    where isPrimeMemo' = hashMemoInt $ isPrime

primesBelow n = takeWhile (<n) primes

primesLookupBelow n = intMembershipLookup $ primesBelow n

isPrimeLookup max = lookupWithDefault (primesLookupBelow (max+1)) False 

-- Reduces x to its prime factors.
factor x = factor' x primes []
    where factor' x (y : ys) fs | x == 1         = fs 
                                | x `mod` y == 0 = factor' (x `div` y) (y : ys) (y : fs)
                                | otherwise      = factor' x ys fs

-- True if x evenly divides y
x `divides` y = y `rem` x == 0

unroll [] = []
unroll ((x, y) : zs) = x : y : unroll zs

-- Returns all of the numbers that evenly divide x, including 1 and itself.
factors x = nub $ unroll pairs
    where pairs = [(y, x `div` y) | y <- [1..(ceiling . sqrt $ fromIntegral x)], y `divides` x]

properFactors x = filter (/=x) $ factors x

-- Memoizes a function f :: Eq a => a -> b using a hash table to remember
-- values. Uses the hash function hash
hashMemo :: Eq a => (a -> Int32) -> (a -> b) -> (a -> b)
hashMemo hash f = unsafePerformIO $ do
   cache <- Data.HashTable.new (==) hash
   return $ \x -> unsafePerformIO $ do 
                    val <- Data.HashTable.lookup cache x
                    case val of
                      Nothing -> do let y = f x
                                    Data.HashTable.insert cache x y
                                    return y
                      Just y -> do return y

lookupWithDefault :: (IO (HashTable key val)) -> val -> (key -> val) 
lookupWithDefault table def = unsafePerformIO $ do
  t <- table
  return $ \x -> unsafePerformIO $ do
                   val <- Data.HashTable.lookup t x
                   case val of
                     Nothing -> do return def
                     Just y -> do return y

intMembershipLookup :: [Int64] -> (IO (HashTable Int Bool))
intMembershipLookup xs = do
  t <- Data.HashTable.new (==) hashInt
  mapM_ (\x -> Data.HashTable.insert t x True) xs
  return $ t


-- Memoizes a function that takes an Int
hashMemoInt = hashMemo hashInt

-- A version of maximum that uses IORefs to avoid stack overflow
-- for long/infinite lists.
less r x = x > (unsafePerformIO $ readIORef r)
useMax r x = when (less r x) $ writeIORef r x
maxM xs = do 
  m <- newIORef $ head xs
  mapM_ (useMax m) xs
  readIORef m

-- Sums the digits of n in base 10
sumDigits = sum . digits

-- digits in base 10 of the number
digits :: Integral a => a -> [Int]
digits = (map digitToInt) . show 

digitCount = length . digits

digitsToNum :: [Int] -> Integer
digitsToNum = read . (concatMap show)

-- n!
fac n = if n > 0 then n * fac (n - 1) else 1

isPandigital9 = isPandigital [1..9]
isPandigital0 = isPandigital [0..9]
isPandigital ns = digitsPan . digits where
    digitsPan ds = sort ds == ns

-- The Fibonacci sequence
fibs = 1 : 1 : zipWith (+) fibs (tail fibs)

maximumByKey key = maximumBy (\a b -> compare (key a) (key b))

bigPower :: Int -> Int -> Integer
bigPower a b = product $ map fromIntegral (replicate b a)

removing others = filter (\d -> not $ elem d others) 

perms p start [] = [[]]
perms p start xs = concatMap (\x -> 
                              let start' = start ++ [x]
                              in if p start' then map (x:) $ perms p start' $ filter (/=x) xs
                                 else []) xs

-- Short-circuiting generation of permutations, all matching p.
matchPermutations p xs = perms p [] xs 

permutations :: Eq a => [a] -> [[a]]
permutations = matchPermutations (\_ -> True) 

showBinary' :: Bits a => a -> String
showBinary' n = let next = sb $ shiftR n 1
               in case testBit n 0 of
                    True -> '1' : next
                    _    -> '0' : next
    where sb n' | n' == 0   = ""
                | otherwise = showBinary' n'

showBinary :: Bits a => a -> String
showBinary = reverse . showBinary'

readCsvQuoted' s = case dropWhile isPunctuation s of
                     "" -> []
                     s' -> n : readCsvQuoted' s''
                         where (n, s'') = break isPunctuation s'

readCsvQuoted file = do readFile file >>= return . sort . readCsvQuoted'

unsafePrint r x = unsafePerformIO $ do print x ; return r


-- solves a quadratic equation
quadratic a b c = let s = sqrt(b^2 - 4*a*c)
                      aa = 2*a
                  in ((-b + s) / aa, (-b - s) / aa)


-- Generates unique combinations. 
-- (length $ combinations r xs) == (length xs) `nCr` r
combinations :: Int -> [a] -> [[a]]
combinations n xs@(x : xs') | length xs < n  = throw $ AssertionFailed "Can't choose more elements than I have."
                            | n == 0         = [[]]
                            | length xs == n = [xs] 
                            | otherwise      = (map (x:) $ combinations (n-1) xs') ++ (combinations n xs')

isAnagram xs ys = (sort xs) == (sort ys)

n `nCr` r = (fac n) `div` ((fac r) * (fac $ n - r))
n `nPr` r = (fac n) `div` (fac $ n - r)

replace x y xs = map (\x' -> if x' == x then y else x') xs

isPalindrome xs = xs == (reverse xs)

numIsPalindrome num = isPalindrome $ digits num

reverseNum n = digitsToNum $ reverse $ digits n

concatNums x y = read $ show x ++ show y
concatInts x y = x*(mag 1) + y where
    mag n = if n > y then n else mag (10*n)

disjoint a b = S.intersection (S.fromList a) (S.fromList b) == S.empty

-- Stuff below here I wrote, thinking I needed it, but never actually used
-- it in a finished solution.

swap xs i j | i == j    = xs 
            | otherwise = let i' = minimum [i, j]
                              j' = maximum [i, j] - i' - 1
                              (start, xi : rest) = splitAt i' xs
                              (mid, xj : end) = splitAt j' rest
                          in foldl1 (++) [start, xj : mid, xi : end]

