{-
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
-}
import Data.Char
import EulerUtil
wordValue w = sum $ map (\c -> (ord $ toLower c) - (ord 'a') + 1) w
t n = n * (n+1) `div` 2
triangles = map t [1..]
isTriangle n = (head $ dropWhile (<n) triangles) == n
engWords = readCsvQuoted "words.txt"
wordVals = engWords >>= return . map wordValue 
triWords = wordVals >>= return . filter isTriangle
answer = triWords >>= return . length
