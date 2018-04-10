# from item import Item
# from transaction import Transaction
from itemset import Itemset


# Permet de creer le jeu de donnees TRANSACTIONS --> Items
class Dataset:
    def __init__(self):
        self.lst_transactions=[]

    # Ajoute des transactions dans le data
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
                    # retpourne une liste
        return lst_singleton

    # cree une liste d'itemset frequent a partir d'une liste d'itemset et d'un minSup
    # calcul le support et ceux qui verifie la condition sont rajoutés
    def itemsetFreq(self, lst_itemset, minsup=2):
        lst_itemsetfreq=[]
        for monItemset in lst_itemset:
            #print(monItemset)
            supportItemset=monItemset.supportItemset(self)
            #print(supportItemset)
            if (supportItemset) >= minsup:
                lst_itemsetfreq.append(monItemset)
        return " Les itemsets frequents dans ce Data sont : \n {}".format(lst_itemsetfreq)


    #combinaison de toutes les methodes precedentes
    # retourne une liste d'itemsets frequents
    def aPriori(self,minsup):

        # Recuperation les singletons du dataset
        liste_singleton=Dataset.singleton(self)

        # On cree une liste vide d'itemset qui nous permettra de recuperer la liste des singletons frequents
        mesItemsetFrq=[]

        # Permet de recuperer la liste des Itemsets( de taille n+1)
        mescandidats=[]

        # Pour chaque singleton (qui sont des itemsets de taille 1) dans la liste des singletons Calculer le support
        for monSingleton in liste_singleton:
            mesSupports=monSingleton.supportItemset(self)

            # Pour chaque support(des singletons) >= au minSup, on rajoute le singleton dans mesItemsetFreq
            for unSupport in [mesSupports]:
                if unSupport >= minsup:
                    mesItemsetFrq.append(monSingleton)

                    # On genere des itemsets de taille n+1 frequent que l'on stockent dans une liste d'itemset candidate
                    monCandidat=Itemset.supersetCand(mesItemsetFrq)
                    mescandidats.append(monCandidat)

                    # Pour un candidat dans la liste d'itemset (de taille n+1) frequent, calculer le support
                    # si le support d'un candidat est superieur ou egal au minsup
                    # on le rajoute dans la liste de candidat
                    for moncandidat in mescandidats:
                        supportCand=moncandidat.supportItemset(self)
                        if supportCand >= minsup:
                            mescandidats.append(moncandidat)

        # On retourne une liste d'itemset de taille n+1 candidate pour une regle d'association
        return "Liste d'itemset (de taille n+1) frequent dans le data : \n {} ".format(mescandidats)