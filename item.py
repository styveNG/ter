class Item:
    def __init__(self,nomItem,spetech=None):
        self.nomItem=nomItem
        self.spetech=spetech
    def __repr__(self):
        return "{}: {}".format(self.nomItem, self.spetech)

    #test d'equalite
    #other=item2
    def __eq__(self,other):
        if self.nomItem==other.nomItem and self.spetech==other.spetech:
            return True
        else:
            return False

    # utilisation de la mthode __hash__
    # calcul de la signature

    def __hash__(self):
        return self.nomItem.__hash__()