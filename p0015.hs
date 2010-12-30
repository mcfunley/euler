{-
Starting in the top left corner of a 2×2 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20×20 grid?
-}
import Data.Int
import Data.HashTable
import EulerUtil

type Automata = (Int, Int)

-- initial values
initialA :: Automata
initialA = (0, 0)

-- directions
down = (0, 1)
right = (1, 0)

-- Moves a by the specified amount
move :: Automata -> (Int, Int) -> Automata
move (x, y) (x', y') = (x+x', y+y')

routesFrom' a | fst a == boardDim = 1 
              | snd a == boardDim = 1 
              | otherwise         = (routesFrom $ move a down) + (routesFrom $ move a right)

routesFrom = memoPos routesFrom'

answer = routesFrom (0, 0)
-- 137846528820
-- Size of the board. There are (boardDim+1)**2 positions.
boardDim :: Int
boardDim = 20

-- numbers the positions
ordinalOf :: (Int, Int) -> Int
ordinalOf (x, y) = y * (boardDim+1) + x 

-- hash function for a position
hashPos :: (Int, Int) -> Int32
hashPos = hashInt . ordinalOf

memoPos = hashMemo hashPos
