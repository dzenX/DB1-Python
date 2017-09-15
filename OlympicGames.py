class OlympicGames(object):

    def __init__(self):
        self.last_id = -1
        self.olympicGames = []

    def add(self, game):
        if game.oid != -1:
            self.last_id += 1
            game.oid = self.last_id
            self.olympicGames.append(game)
        else:
            raise Exception("Invalid object")

    def print(self):
        for game in self.olympicGames:
            game.print()

    def delete(self, del_id):
        if del_id < 0:
            raise Exception("Invalid id")
        if del_id <= self.last_id:
            for game in self.olympicGames:
                if game.oid == del_id:
                    self.olympicGames.remove(game)
                    break
            i = 0
            while i < len(self.olympicGames):
                self.olympicGames[i].oid = i
                i += 1
        else:
            raise Exception("No such id")
