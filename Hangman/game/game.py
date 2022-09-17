from domain.sentence import Sentence
from repository.repository import Repository


class Game:
    def __init__(self, computer, repository: Repository):
        self.__computer = computer
        self.__repository = repository
        self.__sentence = self.selectSentence()
        self.__guesses = list()

    def start(self):
        self.__repository.startGame()
        while True:
            self.move()
            if self.status() == 1:
                print("Player WON!!!")
                break
            elif self.status() == -1:
                print("Player LOST!!!")
                break

    def move(self):
        while True:
            guess = input("Please guess: ")
            if len(guess) != 1 or guess.isalpha() is False:
                print("WRONG VALUE!!!")
                pass
            elif guess not in self.__guesses:
                self.__guesses.append(guess)
                break
            else:
                print("Already made that guess!!!")
        self.__repository.checkGuess(guess)

    def status(self):
        if self.__sentence.done() is True:
            return 1
        if self.__computer.get == "hangman":
            return -1
        return 0

    def selectSentence(self):
        return self.__repository.takeASentence()
