import sympy


def getChildren(lastToken, unvisitedTokens, isFirstMove):
    children = []

    # we need to get all odd numbers lesser than n/2 for the first move
    if isFirstMove is True:
        limit = len(unvisitedTokens) / 2
        for token in unvisitedTokens:
            # assuming list is sorted asc
            if token > limit:
                break
            if token % 2 != 0:
                children.append(token)

    # anything other than first move, we get multiple or factor of the last move
    else:
        for token in unvisitedTokens:
            # get factors
            if lastToken % token == 0:
                children.append(token)
            # get multiples
            if token % lastToken == 0:
                children.append(token)

    return children


def getScoreHelper(lastToken, unvisitedTokens, children, isMax):
    score = 0
    if 1 not in unvisitedTokens:
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

    if isMax is False:
        score = -score

    return score


def staticEvaluation(isMaxTurn, visitedTokens, unvisitedTokens, isFirstMove):
    score = 0
    lastToken = visitedTokens[-1]
    children = getChildren(lastToken, unvisitedTokens, isFirstMove)

    if isMaxTurn is True:
        # if it's Max's turn and he can't choose any token, Min wins
        if not len(children) > 0:
            score = -1
        else:
            score = getScoreHelper(lastToken, unvisitedTokens, children, isMaxTurn)


    else:
        # if it's Min's turn and he can't choose any token, Max wins
        if not len(children) > 0:
            score = 1
        else:
            score = getScoreHelper(lastToken, unvisitedTokens, children, isMaxTurn)

    return score
