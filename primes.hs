
primes = 2 : filter isP [3,5..] where
   f x p r = x < p*p || (not $ p `divides` x) && r
   isP x = foldr (f x) True primes

x `divides` y = y `mod` x == 0

