# from item import Item
# from dataset import Dataset
# from transaction import Transaction

# la classe Itemset herite de la class set
class Itemset(set):
    def __init__(self, lst_item):
        super().__init__(lst_item)

    # # => comment faire pour accéder à un élément d'un itemset??

    # Doit afficher uniquement une liste d'item avec leur nom sans les spetech
    # --- PB n'affiche pas la liste generee grace au set

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
        return support

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

    # Permet de verifier que TOUS les subset de taille n-1 qui composent un itemset de taille n sont frequents
    # => les elts de lst_frq doivent etre de taille n-1
    # retourne un booleen
    def verifSubset(self,lst_itemset_frq): #retourne T / F
        for item in self:
            subset = Itemset(self - Itemset([item]))  ## fonctionne bien jusqu'ici
            print(subset)
            while subset in lst_itemset_frq:
                return True
            # if not subset in (lst_itemset_frq):   ## si au moins un des subsets de self ne fait pas partie de lst_frq
            #     return False
            else:  ## si tous les subsets de self sont dans lst_frq
                return False

        # ne fait le test que sur le premier subset !!!! => logique car la condition if ne porte que sur le premier item
        ## pourquoi apres le return la fonction ne remonte plus vers la boucle for?
        ## le return marque la fin d'une fonction??

        ## idee de solution: retirer un itemset à self (pour ainsi creer un premier subset de taille n-1
        # si ce premier subset fait partie de lst_itemset_frq, on passe au deuxieme subset
        # le problème est: comment générer ces subsets ?
            #on sait que les subsets d'un itemset sont composés de l'itemset auquel on a retiré un element   

    @classmethod
    #a initialiser: liste vide d'itemset cand
    #prend une liste d'itemsets de meme taille en argument
    def supersetCand(cls,lst_itemset_frq):
        ## prendre deux par deux des itemsets de lst_itemset_frq, en faire l'union. si l'union est de taille n+1 cf. unionValide,
        ## verifier que tous les subsets de cette union font partie de lst_itemset_frq (exemple concret où ce n'est pas le cas)
        ## si cette condition est vérifiée, stocker l'itemset obtenu dans une liste
        ## on passe aux paires suivantes, meme démarche. si l'itemset est deja dans la liste, pas la peine de le rajouter de nouveau
        ## à la fin de la boucle, retourner la liste d'itemsets (qui doivent tous etre de taille n+1)
        ## comment prendre des éléments d'une liste deux par deux????
        lst_superset = []
        for itemset1 in lst_itemset_frq:
            for itemset2 in lst_itemset_frq:
                if itemset1 != itemset2:
                    union = itemset1.unionValide(itemset2)
                    if union.verifSubset(lst_itemset_frq):
                        lst_itemset_frq.append(union)
        return lst_superset


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