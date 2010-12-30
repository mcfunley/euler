import EulerUtil
import Data.List

isSatanic n = isInfixOf "666" (show n)

answer = sum $ take 666 $ filter isSatanic primes

-- 1112840592
