-- Find the sum of all the multiples of 3 or 5 below 1000.
isMultiple x y = rem x y == 0
answer = sum $ filter (\x -> isMultiple x 5 || isMultiple x 3) [1..999]