{-
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
-}
import EulerUtil
import Data.List

digitsPan ds = sort ds == [1..9]
isPan = digitsPan . digits 

natProducts n = map (*n) [1..]
prod2dig = concatMap digits
productsPan ps = digitsPan $ prod2dig ps

pandigitalProducts n = prod2num' $ filter productsPan $ drop 2 $ inits $ take 9 $ natProducts n where
    prod2num' [] = 0
    prod2num' (x : _) = digitsToNum $ prod2dig x

answer = filter (/=0) $ map pandigitalProducts [1..]

answer' = maximum [123456789,918273645,192384576,219438657,273546819,327654981,672913458,679213584,692713854,726914538,729314586,732914658,769215384,792315846,793215864,926718534,927318546,932718654]