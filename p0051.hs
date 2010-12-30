{-
By replacing the 1st digit of *57, it turns out that six of the possible values: 157, 257, 457, 557, 757, and 857, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
-}
import EulerUtil
import Control.Exception

changeNth n xs x | length xs < n = throw $ AssertionFailed "Bad index."
                 | otherwise     = let (start, end) = splitAt (n-1) xs
                                       e = if end == [] then [] else tail end
                                   in start ++ (x : e)

-- Change digits in the list ds in the list of digits xs to x.
changeDigits ds xs x = foldl (\xs' d -> changeNth d xs' x) xs ds

-- Change digits ds in the number n to x.
replaceDigits ds n x = digitsToNum $ changeDigits ds (digits n) x

-- Get all numbers that can be derived by replacing digits ds in num with the same digit.
replaceN num ds = map (replaceDigits ds num) [0..9]

-- Get a list of lists of replacement families, up to replacing all but one digit 
-- of the number.
replacementFamilies n = concatMap (replacementFamiliesOfLength n) [1..digitCount n - 1]

replacementFamiliesOfLength n d = 
    let cn = digitCount n
        digitSets = combinations d $ [1..cn]
        families = map (replaceN n) digitSets
    in map (uniformDigits cn) families

-- filters any numbers in xs that do not have exactly n digits.
uniformDigits n = filter (\x -> digitCount x == n) 

primeReplacementFamilies n = filter (/=[]) $ map (filter (isPrime . fromIntegral)) $ replacementFamilies n

prfsContainingSelf n = filter (elem n) $ primeReplacementFamilies n

hasNPrimeFamily n num = length (take 1 $ filter (\xs -> length xs == n) $ prfsContainingSelf num) > 0

answer = head $ filter (hasNPrimeFamily 8) $ map fromIntegral primes

-- 121313

-- 120383
-- 120383
-- 100109