class Item:
    def __init__(self,nom_item,spe_tech=None):
        self.nom_item=nom_item
        self.spe_tech=spe_tech
    def __repr__(self):
        return "{} ({})".format(self.nom_item, self.spe_tech)


# Permet de creer les transactions
class Transaction:
    def __init__(self,nom_transac,lst_item):
        self.nom_transac=nom_transac
        self.lst_item=lst_item
        maListe=[]
        for item in lst_item:
            maListe.append(Item(item))
    def __repr__(self):
        return "{} : {}".format(self.nom_transac,self.lst_item)


# Permet de creer le jeu de donnees TRANSACTION --> Items
class Dataset:
    def __init__(self,lst_transactions):
        self.lst_transactions=lst_transactions
        mondata=[]
        for mestransac in lst_transactions:
            mondata.append(mestransac)
            print (mondata)

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

monCaddie1= Transaction("T1",["Pain"])
monCaddie2 = Transaction("T2",["pain", "couches", "biere", "œufs"])

monData=Dataset([monCaddie1,monCaddie2])







# D1.itemsetFreq(lst_itemset,minsup)
# retourne une lst itemset frequent qui est sous ensemble de la liste d'itemset en parametre