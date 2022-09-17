from board.board import Board


class Ship:
    def __init__(self, board: Board, place):
        self.__board = board
        self.__firstBodyPart = "+"
        self.__secondBodyPart = "+"
        self.__thirdBodyPart = "+"
        self.__place = place

    def placeShip(self, place):
        self.__board.placeShip(place)

    def getPlace(self):
        return self.__place

    def checkPosition(self, place):
        if self.__place[:2] == place:
            self.__firstBodyPart = "X"
        elif self.__place[2:4] == place:
            self.__secondBodyPart = "X"
        elif self.__place[4:] == place:
            self.__thirdBodyPart = "X"
        else:
            return False
        return True

    def checkWhichBodyHit(self, place):
        if self.__place[:2] == place:
            self.__firstBodyPart = "X"
        elif self.__place[2:4] == place:
            self.__secondBodyPart = "X"
        elif self.__place[4:] == place:
            self.__thirdBodyPart = "X"
        else:
            return False
        if self.__firstBodyPart == self.__secondBodyPart == self.__thirdBodyPart == "X":
            return True
        return False
