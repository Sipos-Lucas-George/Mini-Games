from strategy.strategy import Strategy
from board.board import Board
from board.ship import Ship
from random import shuffle


class Computer:
    def __init__(self, board: Board, strategy: Strategy):
        self.__board = board
        self.__strategy = strategy
        self.__firstShip = None
        self.__secondShip = None

    def move(self):
        self.__strategy.move()

    def placeShips(self, listOfShips):
        alpha = ["0", "1", "2", "3", "4", "5"]
        num = ["0", "1", "2", "3", "4", "5"]
        lr = [-1, 1]
        ud = ["row", "coll"]
        while True:
            shuffle(alpha)
            shuffle(num)
            shuffle(lr)
            shuffle(ud)
            place = alpha[0] + num[0]
            place = self.buildShip(place, lr[0], ud[0])
            if place != -1:
                self.__firstShip = Ship(self.__board, place)
                self.__firstShip.placeShip(place)
                break
        while True:
            shuffle(alpha)
            shuffle(num)
            shuffle(lr)
            shuffle(ud)
            place = alpha[0] + num[0]
            place = self.buildShip(place, lr[0], ud[0])
            if place != -1 and self.__board.verifyComputerAreaForShip(place) is True:
                self.__secondShip = Ship(self.__board, place)
                self.__secondShip.placeShip(place)
                break
        self.setUpShipList(listOfShips)

    @staticmethod
    def buildShip(place, sign, way):
        if way == "row":
            if sign == -1 and int(place[0]) < 2:
                return -1
            elif sign == 1 and int(place[0]) > 3:
                return -1
            place += f"{int(place[0])+sign}{place[1]}{int(place[0])+sign*2}{place[1]}"
        else:
            if sign == -1 and int(place[1]) < 2:
                return -1
            elif sign == 1 and int(place[1]) > 3:
                return -1
            place += f"{place[0]}{int(place[1])+sign}{place[0]}{int(place[1])+sign*2}"
        return place

    def setUpShipList(self, listOfShips):
        listOfShips.append(self.__firstShip)
        listOfShips.append(self.__secondShip)
