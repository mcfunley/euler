{-
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

    * High Card: Highest value card.
    * One Pair: Two cards of the same value.
    * Two Pairs: Two different pairs.
    * Three of a Kind: Three cards of the same value.
    * Straight: All cards are consecutive values.
    * Flush: All cards of the same suit.
    * Full House: Three of a kind and a pair.
    * Four of a Kind: Four cards of the same value.
    * Straight Flush: All cards are consecutive values of same suit.
    * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following four hands dealt to two players:
Hand                 Player 1	 	Player 2	 	Winner
1                    5H 5C 6S 7S KD     2C 3S 8S 8D TD          Player 2
2                    5D 8C 9S JS AC     2C 5C 7D 8S QH          Player 1
3                    2D 9C AS AH AC     3D 6D 7D TD QD          Player 2
4                    4D 6S 9H QH QC     3D 6D 7H QD QS          Player 1
5                    2H 2D 4C 4D 4S     3C 3D 3S 9S 9D          Player 1

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are player one's cards and the last five are player two's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does player one win?
-}
import EulerUtil
import Data.List
import Data.Maybe

data Rank = HighCard | Pair | TwoPair | ThreeOfAKind | 
            Straight | Flush | FullHouse | FourOfAKind | 
            StraightFlush | RoyalFlush
            deriving (Show, Eq, Ord, Enum)

ranks = enumFromTo HighCard RoyalFlush

data Suit = Spades | Clubs | Hearts | Diamonds
            deriving (Eq, Show, Enum)

data CardValue = Two | Three | Four | Five | Six | Seven | Eight | 
                 Nine | Ten | Jack | Queen | King | Ace
                 deriving (Show, Enum, Eq, Ord)

data Card = Card {value :: CardValue,
                  suit :: Suit}
            deriving (Show, Eq)

type SortedCards = [Card]
sortedCards cs = reverse $ sort cs

instance Ord Card where
    compare c1 c2 = compare (value c1) (value c2)

-- For overriding default Eq behavior on Card
eqIgnoreSuit :: Card -> Card -> Bool
eqIgnoreSuit c1 c2 = (value c1) == (value c2)

data Hand = Hand {cards :: SortedCards}
            deriving (Show, Eq)

hand :: [Card] -> Hand
hand cs | length cs == 5 = Hand $ sortedCards cs
        | otherwise      = error "Wrong number of cards."

data RankInst = RankInst { rank :: Rank, constituents :: [Card] }
                deriving (Show, Eq)
rankInst r cs = RankInst r $ reverse $ sort cs

instance Ord RankInst where 
    compare x y | (rank x == rank y) = orderWithinRank (rank x) (constituents x) (constituents y)
                | otherwise          = compare (rank x) (rank y)

-- All that consist of just one card, or that only depend on the high card 
-- can be compared easily; full house and two pair require special treatment.
orderWithinRank r xs ys | elem r [HighCard, Flush, Pair, 
                                  TwoPair, ThreeOfAKind,
                                  FourOfAKind, RoyalFlush] = compare (head xs) (head ys)
                        -- compare second element for the case of a wheel straight 
                        -- (Ace would be first, should be last)
                        | elem r [Straight, StraightFlush] = compare (xs !! 1) (ys !! 1)
                        | otherwise = orderWithinRank' r (map value xs) (map value ys)

orderWithinRank' r xs ys =
    case r of
      FullHouse -> let split cs = (head $ firstSetOfLength 3 cs, head $ firstSetOfLength 2 cs)
                   in rankCompare (split xs) (split ys)                      
      TwoPair -> rankCompare (head xs, xs !! 2) (head ys, ys !! 2)

rankCompare (xh, xl) (yh, yl) = if xh == yh then compare xl yl
                                else compare xh yh

firstSetOfLength n xs = head $ filter (\xs' -> length xs' == n) $ group xs

maybeSetOfLength :: Int -> [Card] -> Maybe [Card]
maybeSetOfLength n xs = let gs = filter (\xs' -> length xs' == n) $ groupBy eqIgnoreSuit (sort xs)
                        in if gs == [] then Nothing
                           else Just $ head gs

removeCards cs from = filter (\c -> not $ elem c cs) from 

matchSet t n cs = maybeSetOfLength n cs >>= \cs' -> return $ rankInst t cs'

fullHandOnly f = \cs -> if length cs < 5 then Nothing
                        else f cs

consecutive nums = let nums' = sort nums
                       (from, to) = (head nums', last nums')
                   in [from..to] == nums'

cardNums = map (fromEnum . value)

matchStraight = fullHandOnly matchStraight'
matchStraight' :: [Card] -> Maybe RankInst
matchStraight' cs = let nums = cardNums cs
                    in if consecutive nums then Just $ rankInst Straight cs
                       else matchWheel cs

-- Detect a wheel straight. 
matchWheel :: [Card] -> Maybe RankInst
matchWheel cs = let ace = fromEnum Ace
                    nums = cardNums cs
                    nums' = replace ace ((fromEnum Two) - 1) nums
                in if consecutive nums' then Just $ rankInst Straight cs
                   else Nothing

matchFlush = fullHandOnly matchFlush'
matchFlush' :: [Card] -> Maybe RankInst
matchFlush' cs@(c : _) = if all (\c' -> suit c == suit c') cs then Just $ rankInst Flush cs
                        else Nothing

-- matchFlush [Card Ace Spades, Card Jack Spades, Card Three Spades, Card Two Spades, Card Six Spades]

matchRank :: Rank -> [Card] -> Maybe RankInst
matchRank _ [] = Nothing
matchRank r cs =
    case r of 
      HighCard -> Just $ rankInst HighCard [maximum cs]
      Pair -> matchSet Pair 2 cs
      TwoPair -> maybeSetOfLength 2 cs >>= \pair1 -> 
                 maybeSetOfLength 2 (removeCards pair1 cs) >>= \pair2 -> 
                 return $ rankInst TwoPair (pair1++pair2)
      ThreeOfAKind -> matchSet ThreeOfAKind 3 cs
      Straight -> matchStraight cs
      Flush -> matchFlush cs
      FullHouse -> maybeSetOfLength 3 cs >>= \trips -> 
                   maybeSetOfLength 2 (removeCards trips cs) >>= \pair ->
                   return $ rankInst FullHouse (trips++pair)
      FourOfAKind -> matchSet FourOfAKind 4 cs
      StraightFlush -> matchFlush cs >>= \_ -> 
                       matchStraight cs >>= \ri -> return $ rankInst StraightFlush (constituents ri)
      RoyalFlush -> matchRank StraightFlush cs >>= \ri@(RankInst { rank = _, constituents = cs' }) ->
                    if (value (cs' !! 1) == King) then Just $ rankInst RoyalFlush cs'
                    else Nothing


handRanks :: Hand -> [RankInst]
handRanks h = handRanks' (cards h) []

handRanks' :: [Card] -> [RankInst] -> [RankInst]
handRanks' [] rs = rs
handRanks' cs rs = let ri = head $ catMaybes $ map (\r -> matchRank r cs) (reverse ranks)
                   in handRanks' (removeCards (constituents ri) cs) $ rs ++ [ri]

compareLists xs ys = let cs = filter (/=EQ) $ zipWith compare xs ys
                     in if cs == [] then EQ
                        else head cs

instance Ord Hand where
    compare h1 h2 = compareLists (handRanks h1) (handRanks h2)

parseCard :: String -> Card
parseCard (v : s : []) = Card (parseValue v) (parseSuit s)

parseValue :: Char -> CardValue
parseValue v = toEnum $ fromJust $ elemIndex v "23456789TJQKA"
                 
parseSuit :: Char -> Suit
parseSuit s = case s of
                'C' -> Clubs
                'S' -> Spades
                'H' -> Hearts
                'D' -> Diamonds

parseGame :: String -> (Hand, Hand)
parseGame s = let cards = map parseCard $ words s
                  (h1, h2) = splitAt 5 cards
              in (hand h1, hand h2)

games :: IO [(Hand, Hand)]
games = readFile "poker.txt" >>= \s -> return $ map parseGame $ lines s

p1wins = games >>= return . filter (\(h1, h2) -> h1 > h2)

answer = p1wins >>= return . length