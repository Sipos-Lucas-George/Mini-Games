class Sentence:
    def __init__(self, sentence):
        self.__sentence = sentence
        self.__letters = self.setLetters()
        self.__givenLetters = [sentence[0], sentence[len(sentence) - 1]]
        self.__letters.remove(sentence[0])
        self.__letters.remove(sentence[len(sentence) - 1])

    def getLetters(self):
        return self.__letters

    def popTheGuess(self, guess):
        self.__letters.remove(guess)
        self.__givenLetters.append(guess)

    def setLetters(self):
        listOfLetters = list()
        for i in range(len(self.__sentence)):
            if self.__sentence[i] not in listOfLetters and self.__sentence[i].isalpha():
                listOfLetters.append(self.__sentence[i])
        return listOfLetters

    def done(self):
        if len(self.__letters) == 0:
            return True
        return False

    def __str__(self):
        listToReturn = ""
        for i in range(len(self.__sentence)):
            if self.__sentence[i] in self.__givenLetters:
                listToReturn += self.__sentence[i]
            elif self.__sentence[i] == " ":
                listToReturn += self.__sentence[i]
            else:
                listToReturn += "_"
        return listToReturn
