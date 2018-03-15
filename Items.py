class Item:
    def __init__(self,nom,spe_tech="NULL"):
        self.nom=nom
        self.spe_tech=spe_tech

    def __repr__(self):
        return "{}: {}".format(self.nom, self.spe_tech)


#####################
# PROGRAMME PRINCIPAL
#####################
pain = Item("pain")
lait = Item("lait", ["1L", "brique"])
couches = Item("couches", ["20couches"])
biere = Item("biere", ["50cL", "canette"])
oeufs = Item("oeufs", ["6", "barquette"])
coca = Item("coca", ["2L", "bouteille", "zero"])

print(pain)
print(lait)
print(couches)
print(biere)
print(oeufs)
print(coca)