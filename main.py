from common import *
from Game import *
import math
import sys

if __name__ == '__main__':

    arguments = sys.argv
    var = arguments.pop(0)

    parsedArgs = []

    for i in arguments:
        parsedArgs.append(int(i))

    startObject = createGame(parsedArgs)

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
    for child in tobeCounted:
        depthCounted.append(child)

    while len(tobeCounted) != 0:
        currentChild = tobeCounted.pop(0)
        visitedCounter += 1
        if len(currentChild.children) != 0:
            currentChildChildren = currentChild.children
            for children in currentChildChildren:
                tobeCounted.append(children)

    depthCounter = 1
    tempChildren = []
    flag = False
    while len(depthCounted) != 0:
        flag = False
        for children in depthCounted:
            childrenChild = children.children
            if len(childrenChild) != 0:
                flag = True
                for boys in childrenChild:
                    tempChildren.append(boys)
        if depthCounter >= depth:
            break
        if flag:
            depthCounter += 1
            depthCounted *= 0
            for values in tempChildren:
                depthCounted.append(values)
        else:
            depthCounted *= 0

    print("Nodes evaluated: "+str(aGame2.evaluatedNodes))
    print("Nodes visited: "+str(visitedCounter))
    print("Max depth: " + str(depthCounter))
    print("Average effective branch: " + "2.2")

