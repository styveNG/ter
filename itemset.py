from Items import Item

# cette classe devra heriter de "set"
class Itemset(set):
    # Liste d'items
    def __init__(self, lst_item):
        super().__init__(lst_item)

    # def __repr__(self):
    #     return "{}".format(self)

    # Permet de determiner le support des Itemsets
    def supportItemset(self,data_set):
        pass

    # Cree des superset a partir de l'union de 2 itemsets de meme taille n
    ## union est vire remplacé par unionvalide
    def unionItemset(self, monItemset):
        set_result = super().union(monItemset)
        return Itemset(set_result)
    # Affiche le superSet cree a partir de l'union; il doit etre de taille n+1

    def tailleItemset(self,monItemset):
        pass
    # Permet de verifier que tous les subset de taille n-1 qui composent un itemset
    # de taille n sont frequents
    #les elts de lst_frq doivent etre de taille n-1
    # retourne un booleen

    def verifSubSet(self,lst_frq):
        pass

    @classmethod
    def superSetcand(cls,lst_itemset_freq):
        pass


#####################
# PROGRAMME PRINCIPAL
#####################
# * IS: itemset quelconque
# D1: dataset
#IS.supportItemset(D1)
# Itemset.superSetcand(lst_itemset_freq) ; lst_itemset_freq: composée d'elt de taille n
# retourne une liste d'itemset

pain = Item("pain")
lait = Item("lait", ["1L", "brique"])
couches = Item("couches", ["20couches"])
cake = Item("cake")

monItemset = Itemset([pain, lait, couches])
print(monItemset)
monItemset2 = Itemset([pain, pain, couches, cake])
print(monItemset2)
print(monItemset.unionItemset(monItemset2))
