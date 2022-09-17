from game.game import Game
from board.board import Board
from strategy.strategy import Strategy
from player.player import Player
from player.computer import Computer


boardForPastCalls = Board()
playerBoard = Board()
computerBoard = Board()
playerShips = list()
computerShips = list()
strategy = Strategy(playerBoard, playerShips)
player = Player(playerBoard, boardForPastCalls, computerBoard, computerShips)
computer = Computer(computerBoard, strategy)
game = Game(player, computer, playerBoard, boardForPastCalls, computerBoard, playerShips, computerShips)
game.play()
