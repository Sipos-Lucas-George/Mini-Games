from board.board import Board
from player.player import Player
from player.computer import Computer


class Game:
    def __init__(self, player: Player, computer: Computer, playerBoard: Board, boardForPastCalls, computerBoard, playerShips, computerShips):
        self.__player = player
        self.__computer = computer
        self.__playerBoard = playerBoard
        self.__boardForPastCalls = boardForPastCalls
        self.__computerBoard = computerBoard
        self.__playerShips = playerShips
        self.__computerShips = computerShips
        self.__turn = True

    def play(self):
        self.playerPlaceShips()
        self.__computer.placeShips(self.__computerShips)
        print(self.__playerBoard)
        print(self.__computerBoard)
        while True:
            if self.__turn is True:
                print(self.__computerBoard)
                print(self.__playerBoard)
                print(self.__boardForPastCalls)
                self.move()
                self.__turn = False
            else:
                self.__computer.move()
                self.__turn = True
            if self.winnerStatus() is True:
                return

    def move(self):
        alpha = "ABCDEF"
        num = "012345"
        while True:
            strike = input("Choose where to attack: ")
            if len(strike) != 2 or alpha.count(alpha[0]) == 0 or num.count(strike[1]) == 0:
                pass
            else:
                strike = num[alpha.index(strike[0])] + strike[1]
                if self.__player.verifyForDuplicateMove(strike) is False:
                    self.__player.move(strike)
                    break

    def winnerStatus(self):
        if len(self.__computerShips) == 0:
            print("Computer board:")
            print(self.__computerBoard)
            print("Your boards:")
            print(self.__boardForPastCalls)
            print(self.__playerBoard)
            print("!!!---YOU WON---!!!")
            return True
        elif len(self.__playerShips) == 0:
            print("Computer board:")
            print(self.__computerBoard)
            print("Your boards:")
            print(self.__boardForPastCalls)
            print(self.__playerBoard)
            print("!!!---COMPUTER WON---!!!")
            return True
        return False

    def playerPlaceShips(self):
        donePlacing = 2
        while donePlacing != 0:
            print(self.__playerBoard)
            playerInput = input("Place your ship: ").strip()
            if self.verifyInput(playerInput) is True:
                if donePlacing == 2:
                    self.__player.setUpTheBoard(donePlacing, playerInput[-6:])
                    donePlacing -= 1
                else:
                    if self.__playerBoard.verifyAreaForShip(playerInput[-6:]) is True:
                        self.__player.setUpTheBoard(donePlacing, playerInput[-6:])
                        donePlacing -= 1
            else:
                print("WRONG INPUT!")
        self.__player.setUpShipList(self.__playerShips)

    @staticmethod
    def verifyInput(playerInput):
        alpha = "ABCDEF"
        num = "012345"
        playerInput = playerInput.split(" ")
        for i in range(len(playerInput)):
            playerInput[i] = playerInput[i].strip()
            if playerInput == "":
                pass
            elif i == 0 and playerInput[i] != "ship":
                return False
            if i != 0:
                for j in range(len(playerInput[i])):
                    if j % 2 == 0 and alpha.count(playerInput[i][j]) == 0:
                        return False
                    elif j % 2 != 0 and num.count(playerInput[i][j]) == 0:
                        return False
        return True
