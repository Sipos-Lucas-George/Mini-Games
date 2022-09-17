from computer.computer import Computer
from domain.sentence import Sentence
from random import randint


class Repository:
    def __init__(self, computer: Computer):
        self.__computer = computer
        self.__inputFile = "input.txt"
        self.__outputFile = "output.txt"
        self.__sentences = self.readFromFile()
        self.__sentence = None

    def checkGuess(self, guess):
        if guess in self.__sentence.getLetters():
            self.__sentence.popTheGuess(guess)
            self.saveToFile()
        else:
            self.__computer.add()
            self.saveToFile()

    def saveToFile(self):
        file = open("output.txt", "at")
        quote = '"'
        file.write(f"{self.__sentence} - {quote}{self.__computer}{quote}\n")
        file.close()

    def startGame(self):
        file = open("output.txt", "wt")
        quote = '""'
        file.write(f"{self.__sentence} - {quote}\n")
        file.close()

    def readFromFile(self):
        file = open(self.__inputFile, "rt")
        sentences = list()
        for line in file:
            sentences.append(line.strip())
        file.close()
        return sentences

    def takeASentence(self):
        self.__sentence = Sentence(self.__sentences[randint(0, len(self.__sentences) - 1)])
        return self.__sentence
