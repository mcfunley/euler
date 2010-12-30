{-
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
-}
import EulerUtil
import Data.List

rec' n rdigits next rems = 
    let (d, r) = next `divMod` n
        rdigits' = d : rdigits
        next' = r * 10
        rems' = r : rems
        repeats = elem r rems
    in case r of 
         0 -> zipWith (,) rdigits' rems'
         _ -> if repeats then zipWith (,) rdigits' rems'
              else rec' n rdigits' next' rems'

rec n = rec' n [] 10 []

cycleLength n = cycleLength' $ rec n

cycleLength' rs@((_, r) : _) = case findIndex (\(_, r') -> r' == r) (tail rs) of
                                 Nothing -> 0
                                 Just n -> n + 1

cycleLengths = [(n, cycleLength n) | n <- [1..1000]]

answer = maximumByKey snd cycleLengths

--
repeats ((_, r) : _) = (r > 0)

showRecip n = showRecip' $ rec n
              
showRecip' rs | repeats rs = ""
              | otherwise  = "0." ++ concatMap (show . fst) (reverse rs)
