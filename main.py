from common import *
from Game import *
import math
import sys

if __name__ == '__main__':
    # Getting arguments
    arguments = sys.argv
    var = arguments.pop(0)

    parsedArgs = []

    for i in arguments:
        parsedArgs.append(int(i))

    # Building start object
    startObject = createGame(parsedArgs)
    # Running algorithms
    aGame2 = startObject["game"]
    depth = startObject["depth"]
    visitedCounter = 1
    alphaBetaPrune(aGame2, depth, -math.inf, math.inf)
    bestChild = getBestChild(aGame2)
    # Parsing Results for the analysis
    allChindren = aGame2.children
    tobeCounted = []
    for children in allChindren:
        tobeCounted.append(children)

    # Getting visited count
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

    # Getting the depth
    depthCounter = 1
    tempChildren = []
    flag = False
    while len(depthCounted) != 0:
        flag = False
        for children in depthCounted:
            childrenChild = children.children
            if len(childrenChild) != 0:
                flag = True
                for child in childrenChild:
                    tempChildren.append(child)
        if depthCounter >= depth:
            break
        if flag:
            depthCounter += 1
            depthCounted *= 0
            for values in tempChildren:
                depthCounted.append(values)
        else:
            depthCounted *= 0

    # Calculating the avg branching factor
    evaluatedCounter = aGame2.evaluatedNodes
    try:
        branchingFactor = (visitedCounter - 1) / (visitedCounter - evaluatedCounter)
    except:
        branchingFactor = -1

    print("Nodes visited: " + str(visitedCounter))
    print("Nodes evaluated: " + str(evaluatedCounter))
    print("Max depth: " + str(depthCounter))
    print("Average effective branching factor(if -1 there was a division by 0): " + str(branchingFactor))
