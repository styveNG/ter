class Item:
    def __init__(self,nomItem,spetech=None):
        self.nomItem=nomItem
        self.spetech=spetech
    def __repr__(self):
        return "{}: {}".format(self.nomItem, self.spetech)

    # creation de la methode d'equalite afin de comparer 2produits de meme nom
    # et de meme spetech

    # other: correspond a un second item

    def __eq__(self, autreitem):
        if self.nomItem==autreitem.nomItem and self.spetech==autreitem.spetech:
            return True
        else:
            return False

    # permet de calculer la signature d'un objet

    def __hash__(self):
        return self.nomItem.__hash__()