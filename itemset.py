from item import Item
from dataset import Dataset
from transaction import Transaction

# la classe Itemset herite de la class set
class Itemset(set):
    def __init__(self, lst_item):
        super().__init__(lst_item)
        self.lst_item=lst_item

    # # => comment faire pour accéder à un élément d'un itemset??

    # Doit afficher uniquement une liste d'item avec leur nom sans les spetech
    # --- PB n'affiche pas la liste generee grace au set
    # def __repr__(self):
    #     lst_nomItem=[]
    #     for num_item in range(0,len(self.lst_item)):
    #         lst_nomItem.append(self.lst_item[num_item].nomItem)
    #     return "Itemset: {}".format(lst_nomItem)

    # Permet de determiner le support des Itemsets en fonction d'un dataset
    def supportItemset(self,dataset):
        # mettre un compeur initialisé à 0
        # boucle sur les transactions de dataset
                # recuperer la liste des items de la transaction
                # en faire un itemset ( )
                # utiliser .issubset => si vaut TRUE, rajouter 1 au compteur
        support = 0
        for transaction in dataset.lst_transactions:
            lst_item = transaction.lst_item
            itemset = Itemset(lst_item)
            if self.issubset(itemset):
                support += 1
        return "Le support de l'{} est {}.".format(self,support)
    # Cree des superset a partir de l'union de 2 itemsets de meme taille n
    ## union est vire remplacé par unionvalide
    def unionItemset(self, monItemset):
        set_result = super().union(monItemset)
        return Itemset(set_result)
    # Affiche le superSet cree a partir de l'union; il doit etre de taille n+1
    #verifie que la l'union de deux itemsets de taille n retourne un itemset de taille n+1
    #si c'est de taille n+1, alors retourne l'union
    #sinon retourne None
    def unionValide(self, monItemset):
        if len(self) != len(monItemset):
            print("Les itemsets ne sont pas de la meme taille.")
            return None
        elif len(self.unionItemset(monItemset)) != len(self) +1:
            print("L'union de ces deux itemsets n'est pas valide.")
            return None
        else: #cas ou les itemset sont de meme taille n et leur union est de taille n+1
            return self.unionItemset(monItemset)
    # Permet de verifier que tous les subset de taille n-1 qui composent un itemset
    # de taille n sont frequents
    #les elts de lst_frq doivent etre de taille n-1
    # retourne un booleen
    def verifSubSet(self,lst_frq):
        for item in self:
            subset = Itemset(self.remove(Itemset(item)))
            if subset.isnotsubset(lst_frq):
                return "Les subsets de {} ne sont pas tous fréquents. Par conséquent, {} ne peut être fréquent".format(self, self)

    @classmethod
    #liste vide d'itemset cand initialisée
    #liste d'itemset freq de meme taille
    # prendre des paires d'union valide qui doivent etre de taille n+1
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




# #test de verifSubset
# #monItemset.verifSubSet([pain, lait, biere])
