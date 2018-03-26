from Items import Item
from transaction import Transaction

# Permet de creer le jeu de donnees TRANSACTION --> Items
class Dataset:
    def __init__(self,lst_transactions):
        self.lst_transactions=lst_transactions


    # Identifie les singletons presents dans les transactions
    # Renvoie une liste d'itemset de taille 1 non redondant
    def singleton(self):
        pass

    # cree une liste d'itemset frequent a partir d'une liste d'itemset et d'un minSup
    def itemsetFreq(self, lst_itemset, minsup=2):
        pass

    #combinaison de toutes les methodes precedentes
    def aPriori(self,minsup):
        pass


#####################
# PROGRAMME PRINCIPAL
#####################

monCaddie1= Transaction("T1")
monCaddie2 = Transaction("T2")







# D1.itemsetFreq(lst_itemset,minsup)
# retourne une lst itemset frequent qui est sous ensemble de la liste d'itemset en parametre