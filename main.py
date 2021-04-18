from common import *
import math



aGame = Game(7, [1])
alphaBetaPrune(True, aGame, 3, -(math.inf), math.inf)
print(aGame)
