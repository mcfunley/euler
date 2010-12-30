module EulerUtil (primes, factor
            ) where 

primes = 2 : filter isPrime [3,5..] where
   f x p r = x < p*p || mod x p /= 0 && r
   isPrime x = foldr (f x) True primes

factor x = factor' x primes []
    where factor' x (y : ys) fs | x == 1         = fs 
                                | x `mod` y == 0 = factor' (x `div` y) (y : ys) (y : fs)
                                | otherwise      = factor' x ys fs
