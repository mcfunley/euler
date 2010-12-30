{-
A Pythagorean triplet is a set of three natural numbers, a<b<c, for which,
a� + b� = c�

For example, 3� + 4� = 9 + 16 = 25 = 5�.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
-}

triplet = head [[a, b, c] | c <- [334..998], 
                            b <- [1..c],
                            a <- [1..b],
                            a**2 + b**2 == c**2,
                            a + b + c == 1000]
answer = product triplet
