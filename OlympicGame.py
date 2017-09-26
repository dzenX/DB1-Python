# implementation of unary Olympic Game
class OlympicGame(object):

    # default constructor
    def __init__(self, year, city):
        self.oid = 0
        self.year = year
        self.city = city

    # method of showing info
    def print(self):
        print(str(self.oid) + ". ", end="")
        print(str(self.year) + " ", end="")
        print(self.city)

# EOI of Olympic Game
