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

        # Recuperation des singletons du dataset
        liste_singleton=Dataset.singleton(self)
        # On cree une liste vide d'itemset qu'on retournera
        mesItemsetFrq=[]

        # Recupere les Unions d'itemset pour verifier si elles sont valident
        mesUnions = []

        # Pour chaque singleton (qui sont des itemset de taille 1) dans la liste des singletons Calculer le support
        for monSingleton in liste_singleton:
            mesSupports=monSingleton.supportItemset(self)

            # Pour chaque support(des singletons) >= au minSup, on rajoute le singleton dans mesItemsetFreq
            for unSupport in [mesSupports]:
                if unSupport >= minsup:
                    mesItemsetFrq.append(monSingleton) #DATA

                    # Pour chaque itemeset(singleton) dans mesItemsetFreq, faire une union d'itemset
                    # Pas tres sur de cette boucle!!!!!!! NONNNN
                    # for unItemset in mesItemsetFrq:
                    #     uneUnion=unItemset.unionItemset(unItemset)
                    #     mesUnions.append(uneUnion)
                    #     print(mesUnions)

                        # Pour une union verifier qu'elle est valide
                        # Pas sur de cette boucle non plus
                        # for monUnion in mesUnions:
                        #     monUnionvalide=monUnion.unionValide(monUnion)
                        #     mesUnions.append(monUnionvalide)
                            #print(mesUnions)

                            # si l'union est valide, il faut verifier que tous les subsets sont frequents
                            # if monUnionvalide is not None:
                            #     mesUnions.verifSubSet(mesItemsetFrq)
                            #
                            #
                            #
                            #
                            #
                            # # et calculer le support de l'union
                            # for monUnionvalide in mesUnions:
                            #     monUnionvalide.verifSubset(monUnionvalide)
                            #     SupUnionvalide=monUnionvalide.supportItemset(self)
                            #     if SupUnionvalide >=minsup:
                            #         mesItemsetFrq.append(monUnionvalide)


        return mesItemsetFrq


#####################
# PROGRAMME PRINCIPAL
#####################






# D1.itemsetFreq(lst_itemset,minsup)
# retourne une lst itemset frequent qui est sous ensemble de la liste d'itemset en parametre