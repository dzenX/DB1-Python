class Olympic_Competition(object):

    def __init__(self):
        self.omap = []
        self.cmap = []
        self.omap_id = -1
        self.cmap_id = -1

    def add(self, oid, cid):
        if self.omap_id != self.cmap_id:
            raise Exception("Error")

        for ogame in self.omap:
            if ogame == oid:
                for comp in self.cmap:
                    if comp == cid:
                        raise Exception("Already exists")

        self.omap.append(oid)
        self.cmap.append(cid)
        self.omap_id += 1
        self.cmap_id += 1

    def delete(self, oid, cid):
        if cid > -1:
            i = 0
            while i < len(self.cmap):
                if cid == self.cmap[i]:
                    self.cmap.pop(i)
                    self.omap.pop(i)
                    self.cmap_id -= 1
                    self.omap_id -= 1
                i += 1
        elif oid > -1:
            i = 0
            while i < len(self.omap):
                if oid == self.omap[i]:
                    self.omap.pop(i)
                    self.cmap.pop(i)
                    self.cmap_id -= 1
                    self.omap_id -= 1
        else:
            raise Exception("What are you doing?")

    def getByID(self, idx):
        try:
            return self.omap[idx], self.cmap[idx]
        except Exception:
            raise Exception("Out of range")

    def getSize(self):
        return self.omap_id
