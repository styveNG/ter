# ==> Règle d'association : SI antécédent ALORS conséquent (Si X → Y)
# Elle represente l'estimation de proba conditionnelle Y sachant X

# ==> Une règle d'association est mesurée en utilisant un support minimum et une confiance minimum

### Soit X un itemset frequent de taille n et Y un itemset frequent de taille m
### !!!!!! n et m peuvent etre egales !!!!!!!!!!

## Le support de la regle d'association X→Y est egale au support de l'union (X,Y) de taille n+m des itemsets X et Y
## divisé par le nombre total de transactions presentes dans le data
#    support(X→Y) =  support(X,Y)/ N


## La confiance de la regle d'association X→Y, est egale au support de l'union (X,Y) de taille n+m des itemsets X et Y
## divisé par le support de X
#    confiance(X→Y)= support(X,Y) / support(X)


#_______________________________________________________________________________________________________________________

# Creation de la Classe Association

# La classe association prend en entree deux itemsets de taille differente ou egale
# et renvoie une association de la forme X→Y
class Association:
    def __init__(self, antecedent, consequent):
        #antecedent et consequent sont des itemsets (qui peuvent etre de taille differente)
        self.antecedent=antecedent
        self.consequent=consequent

    def __repr__(self):
        return "{}      =>      {}".format(self.antecedent, self.consequent)

    def supportregle(self, unDataset):
        union = self.antecedent.unionItemset(self.consequent)
        print(union.supportItemset(unDataset))
        support = union.supportItemset(unDataset) / unDataset.nbTransactions()
        return support


    def confiance(self, unDataset):
        union = self.antecedent.unionItemset(self.consequent)
        conf = union.supportItemset(unDataset) / self.antecedent.supportItemset(unDataset)
        return conf


#_________________________________________________________

# => Creer une methode qui genere des relations :

# Par exemple pour un itemset freq (biere, lait couches), generer toutes les relations possibles:
#  i.e:  Itemset(biere,couche) => Itemset(lait)
#        Itemset(biere, lait) = > Itemset(couches)
#        Itemset(lait, couches) => Itemset(biere)

# mettre la methode des regle d'asso dans itemset qui sera un self
# itere sur la lst des itemset freq
# on genere des itemsets de taille n-1 et on recupere l'itemset retiré qu'on mettra en consequent


# RAPPEL: on ne generera que des relations X=n et Y=1
# pas de regle pour les itemsetfre de taille 1


# => Creer une methode qui prend en entree un support minimum et une confiance minimum,
#    qui recupere le support d'un itemset frequent (ex: Itemset(biere, lait couches))
