# from item import Item
# from transaction import Transaction
from itemset import Itemset


# Permet de creer le jeu de donnees TRANSACTIONS --> Items
class Dataset:
    def __init__(self):
        self.lst_transactions=[]

    # méthode pour ajouter des transactions dans le data
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
    # retourne une liste d'itemsets fréquents
    def itemsetFreq(self, lst_itemset, minsup=2):
        lst_itemsetfreq=[]
        for monItemset in lst_itemset:
            #print(monItemset)
            supportItemset=monItemset.supportItemset(self)
            #print(supportItemset)
            if (supportItemset) >= minsup:
                lst_itemsetfreq.append(monItemset)
        return lst_itemsetfreq

    #méthode qui returne le nombre de transactions dasn un dataset
    def nbTransactions(self):
        nbTransa = 0
        for transaction in self.lst_transactions:
            nbTransa += 1
        return nbTransa


    #combinaison de toutes les methodes precedentes
    # retourne une liste d'itemsets frequents
    # il faut faire une boucle
    def aPriori(self,minsup):

        # Recuperation des singletons du dataset
        liste_singleton=self.singleton()

        # Récupération des singletons frequents
        liste_frq = self.itemsetFreq(liste_singleton)

        while len(liste_frq) >= 2:
            #Génération de tous les supersets
            liste_superset = Itemset.supersetCand(liste_frq)
            #print(liste_superset)

            #Génération des supersets fréquents
            liste_frq = self.itemsetFreq(liste_superset)
            #print(liste_frq)
            #memoriser dans une autre liste ce qu'on obtient dans itemsetfrq: itemset avec des tailles differentes
            #tous les mettre dans une meme grande liste, et cest cette derniere liste qu'on retourne

            #vide = []
            if liste_frq != []:
                liste_itemset = liste_frq

        return liste_itemset

    #méthode qui retourne la liste des règles d'association qui vérifient le minsup et le minconf
    #est-ce que les règles d'association qui découlent des itemset issus de apriori vérifient forcément minsup et minconf?
    def associations_valides(self, minsup, minconf):
        liste_asso = []
        for itemset in self.aPriori(minsup):
            for regle in itemset.regles_asso():
                if regle.supportregle(self) >= minsup and regle.confiance(self) >= minconf:
                    liste_asso.append(regle)
        return liste_asso