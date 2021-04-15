import sympy
from Game import *


# by default we assume that it's Max's turn
def getStaticEvaluation(aGame, isMaxTurn):

    score = 0
    lastToken = aGame.lastToken
    unvisitedTokens = aGame.unvisited
    children = aGame.possibleMoves

    if 1 in unvisitedTokens:
        score = 0

    if lastToken == 1:
        if len(children) % 2 == 0:
            score = -0.5
        else:
            score = 0.5

    if sympy.isprime(lastToken) is True:
        primeMultiples = []
        for child in children:
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
        for child in children:
            if child % largestPrime == 0:
                primeMultiples.append(child)

        if len(primeMultiples) % 2 == 0:
            score = -0.6
        else:
            score = 0.6

    if len(children) == 0:
        score = -1

    if isMaxTurn is False:
        score = -score

    return score


def alphaBetaPrune(isMaxTurn, aGame, depth):

    if depth == 0 or len(aGame.children) == 0:
        return getStaticEvaluation(aGame.lastToken, aGame.unvisited, aGame.children)


aGame = Game(7, [1, 2, 3], 5)
