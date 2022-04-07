
class Player:

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def __repr__(self):
        return f" Player: {self.__name}, Score: {self.__score}"

    def __str__(self):
        return f" Player: {self.__name}, Score: {self.__score}"

    def get__name(self):
        return self.__name

    def __set__(self, name):
        self.__name = name

    def get__score(self):
        return self.__score

    def __set__score(self, score):
        self.__score = score
