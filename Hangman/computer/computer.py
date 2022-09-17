class Computer:
    def __init__(self):
        self.__hangman = ""
        self.__letters = ["n", "a", "m", "g", "n", "a", "h"]

    def add(self):
        self.__hangman += self.__letters.pop()

    @property
    def get(self):
        return self.__hangman

    def __str__(self):
        return self.__hangman
