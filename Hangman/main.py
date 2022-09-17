from game.game import Game
from computer.computer import Computer
from repository.repository import Repository


computer = Computer()
repository = Repository(computer)
game = Game(computer, repository)
game.start()

