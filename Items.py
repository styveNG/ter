class Item:
    def __init__(self,nomItem,spetech=None):
        self.nomItem=nomItem
        self.spetech=spetech
    def __repr__(self):
        return "{}: {}".format(self.nomItem, self.spetech)


#####################
# PROGRAMME PRINCIPAL
#####################
pain = Item("pain")
lait = Item("lait", ["1L", "brique"])
couches = Item("couches", ["20couches"])
biere = Item("biere", ["50cL", "canette"])
oeufs = Item("oeufs", ["6", "barquette"])
coca = Item("coca", ["2L", "bouteille", "zero"])
cake = Item("cake")

#print(pain)
#print(lait)
# print(couches)
# print(biere)
# print(oeufs)
# print(coca)
