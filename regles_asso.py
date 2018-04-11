# ==> Règle d'association : SI antécédent ALORS conséquent (Si X → Y)
# Elle represente l'estimation de proba conditionnelle Y sachant X

# ==> Une règle d'association est mesurée en utilisant un support minimum et une confiance minimum

### Soit X un itemset frequent de taille n et Y un itemset frequent de taille m
### !!!!!! n peut etre egale a m !!!!!!!!!!

## Le support de la regle d'association X→Y est egale au support de l'itemset frequent (X,Y) : de taille n+m
## divisé par le nombre total de transactions presentes dans le data
#    support(X→Y) =  support(X,Y)/ N


## La confiance de la regle d'association X→Y, est egale au support de l'itemset frequent (X,Y) : de taille n+m
## divisé par le support de X
#    confiance(X→Y)= support(X,Y) / sup(X)


#_______________________________________________________________________________________________________________________

# Creation de la Classe Association

# La classe association prend en entree deux itemsets frequents de taille differente ou egale
# et renvoie une association de la forme X→Y
class Association:
    def __init__(self, itemsetfreq1, itemsetfreq2):
        self.itemsetfreq1=itemsetfreq1
        self.itemsetfreq2=itemsetfreq2

    def __repr__(self):
        return "SI {} => {}".format(self.itemsetfreq1, self.itemsetfreq2)


#______________________________________________________

# => Creer une methode qui genere des relations :

# Par exemple pour un itemset freq (biere, lait couches), generer toutes les relations poissibles:
#  i.e:  Itemset(biere,couche) => Itemset(lait)
#        Itemset(biere, lait) = > Itemset(couches)
#        Itemset(biere) => Itemset(lait, couche)
#        Itemset(lait) => Itemset(biere, couches)


# => Creer une methode qui prend en entree un support minimum et une confiance minimum,
#    qui calcul le support d'un itemset frequent (ex: Itemset(biere, lait couches))

#    si le support de l'itemset est >= au support minimun:
        # on genere des relations
        # pour chaque relation on calcul la confiance:
                # si la confiance est >= a la confiance minimum:
                        # on retourne une association




