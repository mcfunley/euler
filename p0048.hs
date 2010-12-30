{-
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
-}
num :: Integer
num = sum $ map (\n -> n^n) [1..1000]
snum = show num
answer = reverse $ take 10 $ reverse snum