class Board:
    def __init__(self):
        self.__dimension = 6
        self.__emptySpace = "."
        self.__board = self.createBoard()
        self.__letterDictionary = {
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
            "E": 4,
            "F": 5
        }

    def createBoard(self):
        return[[self.__emptySpace for _ in range(self.__dimension)]for _ in range(self.__dimension)]

    def verifyStrike(self, place):
        if self.__board[int(place[1])][int(place[0])] == self.__emptySpace:
            return False
        return True

    def verifyIfHit(self, place):
        if self.__board[int(place[1])][int(place[0])] != self.__emptySpace:
            return True
        return False

    def placeStrike(self, place, symbol):
        self.__board[int(place[1])][int(place[0])] = symbol

    def placeShip(self, place):
        self.__board[int(place[1])][int(place[0])] = "+"
        self.__board[int(place[3])][int(place[2])] = "+"
        self.__board[int(place[5])][int(place[4])] = "+"

    def verifyAreaForShip(self, place):
        if self.__board[int(place[1])][self.__letterDictionary[place[0]]] == "+":
            return False
        if self.__board[int(place[3])][self.__letterDictionary[place[2]]] == "+":
            return False
        if self.__board[int(place[5])][self.__letterDictionary[place[4]]] == "+":
            return False
        return True

    def verifyComputerAreaForShip(self, place):
        if self.__board[int(place[0])][int(place[1])] == "+":
            return False
        if self.__board[int(place[2])][int(place[3])] == "+":
            return False
        if self.__board[int(place[4])][int(place[5])] == "+":
            return False
        return True

    def __str__(self):
        boardString = "  A B C D E F\n"
        for i in range(self.__dimension):
            addToBoard = " ".join(self.__board[i][j] for j in range(self.__dimension))
            boardString += f"{i} " + addToBoard + "\n"
        return boardString
