from items import Item
from transaction import Transaction
#from itemset import Itemset

class Itemset(set):
    def __init__(self, lst_item):
        super().__init__(lst_item)
        self.lst_item=lst_item

# Permet de creer le jeu de donnees TRANSACTIONS --> Items
class Dataset:
    def __init__(self):
        self.lst_transactions=[]

    def ajouterTransaction(self,maTransaction):
        self.lst_transactions.append(maTransaction)

    def __repr__(self):
        return "{}".format(self.lst_transactions)


    #parcourir toutes transactions et pour chaque transaction parcourrir tous les items de le transaction
    # en faire un itemset et verifier si on l'a deja dans le liste des singleton
    # Identifie les singletons presents dans les transactions
    # Renvoie une liste d'itemset de taille 1 non redondant
    def singleton(self):
        lst_singleton=[]
        for transac in self.lst_transactions:
            for item in transac.lst_item:
                item = Itemset([item])
                if item not in lst_singleton:
                    lst_singleton.append(item)
        return "Les singletons du dataset sont: \n {}".format(lst_singleton)

    # cree une liste d'itemset frequent a partir d'une liste d'itemset et d'un minSup
    # calcul le support et ceux qui verifie la condition sont rajoutés
    def itemsetFreq(self, lst_itemset, minsup =2):
        pass

    #combinaison de toutes les methodes precedentes
    def aPriori(self,minsup):
        pass


#####################
# PROGRAMME PRINCIPAL
#####################








# D1.itemsetFreq(lst_itemset,minsup)
# retourne une lst itemset frequent qui est sous ensemble de la liste d'itemset en parametre