class Competitions(object):

    def __init__(self):
        self.last_id = -1
        self.competitions = []

    def add(self, comp):
        if comp.cid != -1:
            self.last_id += 1
            comp.cid = self.last_id
            self.competitions.append(comp)
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
            i = 0
            while i < len(self.competitions):
                self.competitions[i].cid = i
                i += 1
        else:
            raise Exception("No such id")