from common import *
from Game import *
import math

# aGame1 = createGame([3, 0, 0])
# staticCounter.counter = 0
# alphaBetaPrune(aGame1, -math.inf, math.inf)
#
staticCounter.counter = 0
aGame2 = createGame([7, 1, 1, 2])
alphaBetaPrune(aGame2, 2, -math.inf, math.inf)
#
# staticCounter.counter = 0
# aGame3 = createGame([10, 3, 4, 2, 6, 4])
# alphaBetaPrune(aGame3, 4, -math.inf, math.inf)

