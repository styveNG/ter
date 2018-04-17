# from item import Item
# from dataset import Dataset
# from transaction import Transaction
from association import  Association

# la classe Itemset herite de la class set
class Itemset(set):
    def __init__(self, lst_item):
        super().__init__(lst_item)

    # # => comment faire pour accéder à un élément d'un itemset??

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
            #print("L'union de ces deux itemsets n'est pas valide.")
                #on commente cette ligne sinon s'affiche dans le resultat de a priori
            return None
        else: #cas ou les itemset sont de meme taille n et leur union est de taille n+1
            return self.unionItemset(monItemset)

    # Permet de verifier que TOUS les subset de taille n-1 qui composent un itemset de taille n sont frequents
    # => les elts de lst_frq doivent etre de taille n-1 (vérification non faite ici)
    # retourne un booleen
    def verifSubset(self,lst_itemset_frq): #retourne T / F
        test = []  # variable qui va stocker les resultats de test de la presence du subset courant dans lst_itemset_frq
        for item in self:
            subset = Itemset(self - Itemset([item]))
            if subset in lst_itemset_frq:
                test.append(1)
            else:
                test.append(0)
        if 0 in test:
            return False
        else:
            return True

    #méthode pour générer toutes les règles d'association dérivées d'un itemset (supposé fréquent par rapport à un dataset)
    #que doit retourner cette méthode? une liste?
    def regles_asso(self):
        liste_regles = []
        for item in self:
            antecedent = Itemset(self - Itemset([item]))
            consequent = Itemset([item])
            asso = Association(antecedent, consequent)
            liste_regles.append(asso)
        return liste_regles

    @classmethod
    def supersetCand(cls,lst_itemset_frq):  #lst_itemset_frq: liste d'itemsets de meme taille
        ## prendre deux par deux des itemsets de lst_itemset_frq, en faire l'union. si l'union est de taille n+1 cf. unionValide,
        ## verifier que tous les subsets de cette union font partie de lst_itemset_frq (exemple concret où ce n'est pas le cas)
        ## si cette condition est vérifiée, stocker l'itemset obtenu dans une liste
        ## on passe aux paires suivantes, meme démarche. si l'itemset est deja dans la liste, pas la peine de le rajouter de nouveau
        ## à la fin de la boucle, retourner la liste d'itemsets (qui doivent tous etre de taille n+1)
        ## comment prendre des éléments d'une liste deux par deux???? (résolu)
        lst_superset = []   #liste vide de superset candidats
        for itemset1 in lst_itemset_frq:
            for itemset2 in lst_itemset_frq:
                if itemset1 != itemset2:
                    union = itemset1.unionValide(itemset2)
                    if union is not None and union.verifSubset(lst_itemset_frq) and union not in lst_superset:
                        lst_superset.append(union)
        return lst_superset

