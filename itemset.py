class Itemset:
    # Liste d'items
    def __init__(self,items):
        self.lst_item=items

    # Permet de determiner le support des Item et Itemset
    def supItem(self,data_set):
        pass

    # Cree des superset a partir de l'union 2 itemsets de meme taille n
    def unionItemset(self, itemset1, itemset2):
        pass

    # Affiche le superSet cree a partir de l'union; il doit etre de taille n+1
    def tailleItemset(self):
        pass

    # Permet de verifier que tous les subset de taille n-1 qui composent un itemset
    # de taille n sont frequents
    def subSet(self):
        pass

    @classmethod
    def superSetcand(cls):
        pass
