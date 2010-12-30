{-
What is the first term in the Fibonacci sequence to contain 1000 digits?
-}
--import EulerUtil
len = 1000
answer = fst. head $ dropWhile ((<len) . length . show . snd) $ zipWith (,) [1..] fibs