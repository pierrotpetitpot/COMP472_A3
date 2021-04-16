import sympy
from Game import *
import math


# by default we assume that it's Max's turn
def getStaticEvaluation(aGame, isMaxTurn):

    score = 0
    lastToken = aGame.lastToken
    unvisitedTokens = aGame.unvisited
    possibleMoves = aGame.possibleMoves

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

    if len(possibleMoves) == 0:
        score = -1

    if isMaxTurn is False:
        score = -score

    return score


def alphaBetaPrune(isMaxTurn, aGame, depth):

    if depth == 0 or len(aGame.children) == 0:
        score = getStaticEvaluation(aGame, isMaxTurn)
        aGame.setScore(score)

    if isMaxTurn is True:
        maxEval = -(math.inf)

        for child in aGame.children:
            eval = alphaBetaPrune(False, child, depth - 1)
            maxEval = max(maxEval, eval)
        return maxEval

    else:
        minEval = math.inf
        for child in aGame.children:
            eval = alphaBetaPrune(True, child,  depth - 1)
            minEval = min(minEval, eval)
        return minEval


aGame = Game(7, [1])
alphaBetaPrune(True, aGame, 3)
print(aGame)
