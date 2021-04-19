import sympy
from Game import *
import math
from operator import attrgetter
import sys


# by default we assume that it's Max's turn. If it's Min's turn, we get the reverse
def getStaticEvaluation(aGamePrime, isMaxTurn):
    aGame = copy.deepcopy(aGamePrime)
    score = 0
    lastToken = aGame.lastToken
    unvisitedTokens = aGame.unvisited
    possibleMoves = aGame.possibleMoves

    if len(possibleMoves) == 0:
        score = -1
        if isMaxTurn is False:
            score = 1
        return score

    if lastToken is None:
        return None

    if 1 in unvisitedTokens:
        score = 0

    if lastToken == 1:
        if len(possibleMoves) % 2 == 0:
            score = -0.5
        else:
            score = 0.5

    if sympy.isprime(lastToken) is True:
        primeMultiples = []
        for child in possibleMoves:
            # finding all multiples of the prime number
            if child % lastToken == 0:
                primeMultiples.append(child)

        if len(primeMultiples) % 2 == 0:
            score = -0.7
        else:
            score = 0.7

    if sympy.isprime(lastToken) is False:
        # primefactors() returns prime factors of number in a list, and [-1] returns the last element of that list
        # which is usually the biggest prime from the list
        largestPrime = sympy.primefactors(lastToken)[-1]
        primeMultiples = []
        for child in possibleMoves:
            if child % largestPrime == 0:
                primeMultiples.append(child)

        if len(primeMultiples) % 2 == 0:
            score = -0.6
        else:
            score = 0.6

    if isMaxTurn is False:
        score = -score

    return score


def alphaBetaPrune(aGame, depth, alpha, beta):
    isMaxTurn = aGame.isMaxTurn

    if depth == 0 or len(aGame.children) == 0:
        score = getStaticEvaluation(aGame, isMaxTurn)
        aGame.setScore(score)
        return score

    if isMaxTurn is True:
        maxEval = -(math.inf)

        for child in aGame.children:
            eval = alphaBetaPrune(child, depth - 1, alpha, beta)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if maxEval == 1:
                break
            if beta <= alpha:
                break
            child.setScore(maxEval)
        return maxEval

    else:
        minEval = math.inf
        for child in aGame.children:
            eval = alphaBetaPrune(child, depth - 1, alpha, beta)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if minEval == -1:
                break
            if beta <= alpha:
                break
            child.setScore(minEval)
        return minEval


# creates a game and returns a dictionary composed of a game and a depth
def createGame(aList):
    gameSize = aList[0]
    depth = aList[-1]
    numberOfVisited = aList[1]
    visitedTokens = []
    if numberOfVisited > 0:
        visitedTokens = aList[2:-1]
    if depth == 0:
        depth = math.inf

    aNewGame = Game(gameSize, visitedTokens)

    dictionary = {
        "game": aNewGame,
        "depth": depth
    }
    return dictionary


def getBestChild(aGame):
    isMaxturn = aGame.isMaxTurn

    validChildren = []

    # null check, some children don't have a score
    for child in aGame.children:
        if child.score is not None:
            validChildren.append(child)

    if isMaxturn is True:
        bestChild = max(validChildren, key=attrgetter('score'))
    else:
        bestChild = min(validChildren, key=attrgetter('score'))

    return bestChild


def getInputs(inputs):
    arguments = inputs
    var = arguments.pop(0)
    parsedArgs = []
    for i in arguments:
        parsedArgs.append(int(i))

    return parsedArgs


def staticCounter():
    staticCounter.counter += 1
    print(staticCounter.counter)
