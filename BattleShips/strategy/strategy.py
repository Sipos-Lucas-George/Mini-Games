from board.board import Board
from random import shuffle


class Strategy:
    def __init__(self, playerBoard: Board, playerShips):
        self.__playerBoard = playerBoard
        self.__playerShips = playerShips
        self.__movesThatHit = list()
        self.__movePositions = ['00', '01', '02', '03', '04', '05', '10', '11', '12', '13', '14', '15', '20', '21', '22', '23', '24', '25', '30', '31', '32', '33', '34', '35', '40', '41', '42', '43', '44', '45', '50', '51', '52', '53', '54', '55']

    def move(self):
        if len(self.__movesThatHit) == 0:
            self.randomDecision()
        else:
            self.makeDecision()

    def makeDecision(self):
        i = -1
        for ship in self.__playerShips:
            i += 1
            if ship.checkPosition(self.__movesThatHit[0]) is True:
                break
        location1, location2, location3 = self.parseLocation(i)
        theChosenOne = self.whichToChoose(location1, location2, location3)
        self.__playerBoard.placeStrike(theChosenOne, "X")
        self.__movesThatHit.append(theChosenOne)
        self.checkWhichShip(theChosenOne)
        if len(self.__movesThatHit) == 3:
            self.__movesThatHit.clear()

    def whichToChoose(self, first, second, third):
        if first not in self.__movesThatHit:
            return first
        elif second not in self.__movesThatHit:
            return second
        return third

    def parseLocation(self, index):
        location = self.__playerShips[index].getPlace()
        first = location[:2]
        second = location[2:4]
        third = location[4:]
        return first, second, third

    def randomDecision(self):
        shuffle(self.__movePositions)
        strike = self.__movePositions.pop(0)
        if self.__playerBoard.verifyIfHit(strike) is True:
            self.__playerBoard.placeStrike(strike, "X")
            self.__movesThatHit.append(strike)
            self.checkWhichShip(strike)
        else:
            self.__playerBoard.placeStrike(strike, "0")

    def checkWhichShip(self, strike):
        i = 0
        for ship in self.__playerShips:
            if ship.checkWhichBodyHit(strike) is True:
                self.__playerShips.pop(i)
            i += 1
