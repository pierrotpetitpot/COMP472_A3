from common import *
from Game import *
import math
import sys

# if __name__ == '__main__':
#
#     arguments = sys.argv
#     var = arguments.pop(0)
#
#     parsedArgs = []
#
#     for i in arguments:
#         parsedArgs.append(int(i))


# # parsedArgs = getInputs(sys.argv)
# # print(parsedArgs)
# #
# # aGame2 = createGame(parsedArgs)
# # alphaBetaPrune(aGame2, 2, -math.inf, math.inf)
#
    #startObject = createGame(parsedArgs)
startObject = createGame([7, 3, 1, 4, 2, 3])
aGame2 = startObject["game"]
depth = startObject["depth"]
visitedCounter = 1
alphaBetaPrune(aGame2, depth, -math.inf, math.inf)
bestChild = getBestChild(aGame2)
allChindren = aGame2.children
tobeCounted = []
for children in allChindren:
    tobeCounted.append(children)

depthCounted = []
depthCounted = tobeCounted
while len(tobeCounted) != 0:
    currentChild = tobeCounted.pop(0)
    visitedCounter += 1
    if len(currentChild.children) != 0:
        currentChildChildren = currentChild.children
        for children in currentChildChildren:
            tobeCounted.append(children)

depthCounter = 1
tempChildren = []
while len(depthCounted) != 0:
    flag = False
    for children in depthCounted:
        if len(children.children) != 0:
            flag = True
            childrenChild = children.children
            for boys in childrenChild:
                tempChildren.append(boys)
    if flag:
        depthCounter += 1
        depthCounted.clear()
        for values in tempChildren:
            depthCounted.append(values)



print("Nodes evaluated: "+str(aGame2.evaluatedNodes))
print("Nodes visited: "+str(visitedCounter))
# # aGame3 = createGame([10, 3, 4, 2, 6, 4])
# # alphaBetaPrune(aGame3, 4, -math.inf, math.inf)
# test = 2
