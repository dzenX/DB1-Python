# implementation of unary Olympic Game
class OlympicGame(object):

    # default constructor
    def __init__(self, year, city):
        self.oid = 0
        self.year = year
        self.city = city

    # method of showing info
    def print(self):
        print(self.oid, "\n")
        print(self.year, "\n")
        print(self.city, "\n")
        print("\n")

# EOI of Olympic Game
