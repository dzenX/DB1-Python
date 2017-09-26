class Competitions(object):

    def __init__(self):
        self.last_id = -1
        self.competitions = []

    def add(self, comp):
        if comp.cid != -1:
            i = 0
            while i < len(self.competitions):
                if self.competitions[i].type_of_competition == comp.type_of_competition:
                    if self.competitions[i].type_of_sport == comp.type_of_sport:
                        return i
                i += 1
            self.last_id += 1
            comp.cid = self.last_id
            self.competitions.append(comp)
            return self.last_id
        else:
            raise Exception("Invalid object")

    def print(self):
        for comp in self.competitions:
            comp.print()

    def delete(self, del_id):
        if del_id < 0:
            raise Exception("Invalid id")
        if del_id <= self.last_id:
            for comp in self.competitions:
                if comp.cid == del_id:
                    self.competitions.remove(comp)
                    break
        else:
            raise Exception("No such id")

    def printById(self, pid):
        if pid != -1:
            self.competitions[pid].print()
        else:
            print("Undefined\n")

    def reindex(self):
        i = 0
        result = []
        while i < len(self.competitions):
            if i == self.competitions[i].cid:
                i += 1
                continue
            else:
                result.append((self.competitions[i].cid, i))
                self.competitions[i].cid = i
                i += 1
        self.last_id = len(self.competitions) - 1
        return result
