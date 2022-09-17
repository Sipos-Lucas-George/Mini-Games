from board.board import Board
from board.ship import Ship


class Player:
    def __init__(self, board: Board, boardForPastCalls: Board, computerBoard: Board, computerShips):
        self.__board = board
        self.__boardCalls = boardForPastCalls
        self.__computerBoard = computerBoard
        self.__computerShips = computerShips
        self.__firstShip = None
        self.__secondShip = None

    def move(self, strike):
        if self.__computerBoard.verifyIfHit(strike) is True:
            self.__boardCalls.placeStrike(strike, "X")
            self.__computerBoard.placeStrike(strike, "X")
            self.checkWhichShip(strike)
        else:
            self.__boardCalls.placeStrike(strike, "0")
            self.__computerBoard.placeStrike(strike, "0")

    def checkWhichShip(self, strike):
        i = 0
        for ship in self.__computerShips:
            if ship.checkWhichBodyHit(strike) is True:
                self.__computerShips.pop(i)
            i += 1

    def setUpTheBoard(self, counter, place):
        alpha = "ABCDEF"
        num = "012345"
        place = f"{num[alpha.index(place[0])]}{place[1]}{num[alpha.index(place[2])]}{place[3]}{num[alpha.index(place[4])]}{place[5]}"
        if counter == 2:
            self.__firstShip = Ship(self.__board, place)
            self.__firstShip.placeShip(place)
        else:
            self.__secondShip = Ship(self.__board, place)
            self.__secondShip.placeShip(place)

    def verifyForDuplicateMove(self, strike):
        return self.__boardCalls.verifyStrike(strike)

    def setUpShipList(self, listOfShips):
        listOfShips.append(self.__firstShip)
        listOfShips.append(self.__secondShip)
