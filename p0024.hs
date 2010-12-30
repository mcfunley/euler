{-
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
-}
import EulerUtil

shiftRightRot s i j = let (start, rest) = splitAt (i - 1) s
                          (region, end) = splitAt (j - i + 1) rest
                          l = last region
                          rs = take (length region - 1) region
                      in start ++ l : rs ++ end

pAcc' k n j f s = let j' = (k `div` f) `mod` (n + 1 - j)
                      s' = shiftRightRot s j (j+j')
                      f' = f `div` (n - j)
                  in pAcc k n (j+1) f' s'

pAcc k n j f s | j == n    = s
               | otherwise = pAcc' k n j f s

permutation s k = let n = length s 
                  in pAcc k n 1 (fac $ n - 1) s

stringPerm s k = concatMap show $ permutation s k

answer = stringPerm [0..9] 999999
