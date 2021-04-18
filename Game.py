import copy

class Game:
    def __init__(self, gameSize, visited):
        self.unvisited = self.getUnvisited(gameSize, visited)
        self.visited = visited
        self.isFirstMove = True if len(visited) == 0 else False
        self.lastToken = visited[-1] if len(visited) > 0 else None
        self.possibleMoves = self.getPossibleMoves(self.lastToken, self.unvisited, self.isFirstMove)
        self.children = self.getChildren(self.possibleMoves, self.visited, gameSize)
        self.isEnd = True if len(self.children) == 0 else False
        self.score = None  # IN MAX'S POINT OF VIEW
        self.isMaxTurn = self.whoseTurnIsIt(self.visited)

    def getUnvisited(self, gameSize, visitedPrime):
        visited = copy.deepcopy(visitedPrime)
        unvisited = []
        allTokens = range(1, gameSize + 1)
        for token in allTokens:
            if token not in visited:
                unvisited.append(token)

        return unvisited

    def getPossibleMoves(self, lastTokenPrime, unvisitedTokensPrime, isFirstMovePrime):
        possibleMoves = []
        lastToken = copy.deepcopy(lastTokenPrime)
        unvisitedTokens = copy.deepcopy(unvisitedTokensPrime)
        isFirstMove = copy.deepcopy(isFirstMovePrime)

        # we need to get all odd numbers lesser than n/2 for the first move
        if isFirstMove is True:
            limit = len(unvisitedTokens) / 2
            for token in unvisitedTokens:
                # assuming list is sorted asc
                if token >= limit:
                    break
                if token % 2 != 0:
                    possibleMoves.append(token)

        # anything other than first move, we get multiple or factor of the last move
        else:
            for token in unvisitedTokens:
                # get factors
                if lastToken % token == 0:
                    possibleMoves.append(token)
                # get multiples
                if token % lastToken == 0:
                    possibleMoves.append(token)

        return possibleMoves

    def getChildren(self, possibleMovesPrime, visitedPrime, gameSizePrime):
        possibleMoves = copy.deepcopy(possibleMovesPrime)
        visited = copy.deepcopy(visitedPrime)
        gameSize = copy.deepcopy(gameSizePrime)

        listOfGames = []
        for move in possibleMoves:
            oldVisited = copy.deepcopy(visited)
            oldVisited.append(move)
            newVisited = copy.deepcopy(oldVisited)
            aNewGame = Game(gameSize, newVisited)
            listOfGames.append(aNewGame)

        return listOfGames

    def setScore(self, aScore):
        self.score = aScore

    def whoseTurnIsIt(self, visited):
        numberOfVisited = len(visited)
        isMaxturn = False
        if numberOfVisited > 0:
            if numberOfVisited % 2 == 0:
                isMaxturn = True
        else:
            isMaxturn = True

        return isMaxturn

