class OlympicGames(object):

    def __init__(self):
        self.last_id = -1
        self.olympicGames = []

    def add(self, game):
        if game.oid != -1:
            i = 0
            while i < len(self.olympicGames):
                if (self.olympicGames[i].city == game.city) and (self.olympicGames[i].year == game.year):
                    return i
                i += 1
            self.last_id += 1
            game.oid = self.last_id
            self.olympicGames.append(game)
            return self.last_id
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
        else:
            raise Exception("No such id")

    def printById(self, pid):
        if pid < len(self.olympicGames):
            self.olympicGames[pid].print()

    def reindex(self):
        i = 0
        result = []
        while i < len(self.olympicGames):
            if i == self.olympicGames[i].oid:
                i += 1
                continue
            else:
                result.append((self.olympicGames[i].oid, i))
                self.olympicGames[i].oid = i
                i += 1
        self.last_id = len(self.olympicGames) - 1
        return result

