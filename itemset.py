# cette classe devra heriter de "set"
class Itemset:
    # Liste d'items
    def __init__(self,items):
        self.lst_item=items

    # Permet de determiner le support des Itemsets
    def supportItemset(self,data_set):
        pass

    # Cree des superset a partir de l'union 2 itemsets de meme taille n
    ## union est vire remplacé par unionvalide
    def unionItemset(self, monItemset):
        pass
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