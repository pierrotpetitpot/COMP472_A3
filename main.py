from common import *
from Game import *
import math
import sys





# parsedArgs = getInputs(sys.argv)
# print(parsedArgs)

# aGame2 = createGame(parsedArgs)
# alphaBetaPrune(aGame2, 2, -math.inf, math.inf)

startObject = createGame([7, 1, 1, 2])
aGame2 = startObject["game"]
depth = startObject["depth"]
alphaBetaPrune(aGame2, depth, -math.inf, math.inf)
bestChild = getBestChild(aGame2)

# aGame3 = createGame([10, 3, 4, 2, 6, 4])
# alphaBetaPrune(aGame3, 4, -math.inf, math.inf)
test = 2
