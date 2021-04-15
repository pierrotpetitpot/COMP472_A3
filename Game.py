class Game:
    def __init__(self, gameSize, visited):
        self.unvisited = self.getUnvisited(gameSize, visited)
        self.visited = visited
        self.isEnd = True if len(visited) == gameSize else False
        self.isFirstMove = True if len(visited) == 0 else False
        self.lastToken = visited[-1]

        def getUnvisited(gameSize, visited):
            unvisited = []
            allTokens = range(1, gameSize)
            for token in allTokens:
                if token not in visited:
                    unvisited.append(token)

            return unvisited
