{-
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
-}
import EulerUtil

target = 3.0 / 5.0

-- see problem 28
steps = concatMap (replicate 4) [2,4..]
diags = 1 : zipWith (+) diags steps
widths = map (\x -> x + 1) (0 : steps)

iter width ws ds prime total 
    | total > 1 && ratio <= 0.1 = width
    | otherwise                        = 
        let (ds', ds'') = splitAt 4 ds
            width'      = head ws
            ws'         = drop 4 ws
            pc          = length $ filter isPrime ds'
        in iter width' ws' ds'' (prime+pc) (total+4)
    where ratio = (fromIntegral prime) / (fromIntegral total)

answer = iter 1 (drop 1 widths) (drop 1 diags) 0 1

{-iter n t last ((d, s) : ds) 
    | t > 0 && n / t <= target = last
    | otherwise                = iter (if isPrime d then (1+n) else n) (1+t) s ds

answer = iter 0.0 0.0 0 diags
-}