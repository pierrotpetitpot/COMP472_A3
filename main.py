from common import *
from Game import *
import math
import sys





# parsedArgs = getInputs(sys.argv)
# print(parsedArgs)

# staticCounter.counter = 0
# aGame2 = createGame(parsedArgs)
# alphaBetaPrune(aGame2, 2, -math.inf, math.inf)

staticCounter.counter = 0
aGame2 = createGame([7, 1, 1, 2])
alphaBetaPrune(aGame2, 2, -math.inf, math.inf)
bestChild = getBestChild(aGame2)

# staticCounter.counter = 0
# aGame3 = createGame([10, 3, 4, 2, 6, 4])
# alphaBetaPrune(aGame3, 4, -math.inf, math.inf)

test = 'ca'
