from Items import Item
from dataset import Dataset
from transaction import Transaction
# cette classe devra heriter de "set"
class Itemset(set):
    # Liste d'items
    def __init__(self, lst_item):
        super().__init__(lst_item)
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
        return "Le support de {} est {}.".format(self,support)
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
pain = Item("pain")
lait = Item("lait", ["1L", "brique"])
couches = Item("couches", ["20couches"])
biere = Item("biere", ["50cL", "canette"])
oeufs = Item("oeufs", ["6", "barquette"])
coca = Item("coca", ["2L", "bouteille", "zero"])
cake = Item("cake")
monItemset = Itemset([pain, lait, couches])
# print(monItemset)
monItemset2 = Itemset([pain, pain, couches, cake])
# print(monItemset2)
# print(monItemset.unionItemset(monItemset2))
#######################################
monCaddie1= Transaction("T1")
monCaddie1.ajouterItem(pain)
monCaddie1.ajouterItem(couches)
monCaddie1.ajouterItem(biere)
monCaddie2 = Transaction("T2")
monCaddie2.ajouterItem(couches)
monCaddie2.ajouterItem(cake)
monCaddie2.ajouterItem(coca)
monCaddie2.ajouterItem(oeufs)
monCaddie3 = Transaction("T3")
monCaddie3.ajouterItem(lait)
monCaddie3.ajouterItem(pain)
monCaddie3.ajouterItem(oeufs)
monData=Dataset()
monData.ajouterTransaction(monCaddie1)
monData.ajouterTransaction(monCaddie2)
monData.ajouterTransaction(monCaddie3)
#######################################
monItemsetTest = Itemset([cake])
# print(monData)
# print(monItemsetTest.supportItemset(monData))
#test de unionItemset => les deux itemsets ne sont pas forcément de meme taille (?)
#print(monItemset.unionItemset(monItemset2))
#test de union valide : les deux itemsets doivent etre de meme taille n et leur union doit etre de taille n+1
    #cas ou les deux itemsets sont de meme taille
#print(monItemset.unionValide(monItemset2))
    #cas ou l'union des deux itemsets n'est pas de taille n+1
monItemset3 = Itemset([pain,lait])
monItemset4 = Itemset([couches, biere])
#print(monItemset3.unionValide(monItemset4))
    #cas ou les deux itemsets ne sont pas de meme taille
#print(monItemset.unionValide(monItemsetTest))
#print(monItemset)
# => comment faire pour accéder à un élément d'un itemset
# pour conserver les items qui sont soit dans monItemset, soit dans monItemset2 = retirer les items qui sont dans les 2
#print(monItemset ^ monItemset2)
#test de verifSubset
monItemset.verifSubSet([pain, lait, biere])
