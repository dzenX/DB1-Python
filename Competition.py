# implementation of unary competition
class Competition(object):

    # default constructor
    def __init__(self, type_of_competition, type_of_sport):
        self.cid = 0
        self.type_of_competition = type_of_competition
        self.type_of_sport = type_of_sport

    # method of showing info
    def print(self):
        print(str(self.cid) + ". " + self.type_of_competition + ", " + self.type_of_sport)

# EOI of Competition
