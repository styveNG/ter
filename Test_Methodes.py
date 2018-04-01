from items import Item
from itemset import Itemset
from dataset import Dataset
from transaction import Transaction

######## Test de la classe Item #############
# Creation des items
pain = Item("pain")
lait = Item("lait", ["1L", "brique"])
couches = Item("couches", ["20couches"])
biere = Item("biere", ["50cL", "canette"])
oeufs = Item("oeufs", ["6", "barquette"])
coca = Item("coca", ["2L", "bouteille", "zero"])
cake = Item("cake")
#print(coca)

######## Test de la classe Transaction #############

# Methode1: Creation d'une transaction avec des items crees a la main
monCaddie1= Transaction("T1")
monCaddie1.ajouterItem(pain)
monCaddie1.ajouterItem(couches)
monCaddie1.ajouterItem(biere)

monCaddie2 = Transaction("T2")
monCaddie2.ajouterItem(couches)
monCaddie2.ajouterItem(cake)
monCaddie2.ajouterItem(coca)
monCaddie2.ajouterItem(oeufs)
monCaddie2.ajouterItem(pain)


monCaddie3 = Transaction("T3")
monCaddie3.ajouterItem(lait)
monCaddie3.ajouterItem(pain)
monCaddie3.ajouterItem(oeufs)

#print(monCaddie1)
#print(monCaddie1.lst_item[0].spetech) : permet d'accéder à la spetech de l'item d'indice 0 du caddie 1

# Methode2: Creation d'une transaction a l'aide d'une liste de produit transformer en item
monCaddie4 = Transaction("T4")
monCaddie4.ajouterListeProd(["pommes", "tomates", "eau", "biere"])
#print(monCaddie4)
#print(monCaddie4.lst_item[1].nomItem)   #permet d'accéder à l'item d'indice 1 du caddie 4


######## Test de la classe Dataset #############

# Creation du dataset
monData=Dataset()
monData.ajouterTransaction(monCaddie1)
monData.ajouterTransaction(monCaddie2)
monData.ajouterTransaction(monCaddie3)
monData.ajouterTransaction(monCaddie4)
#print(monData)

######## Test de la classe Itemset #############

# Itemset herite de la classe set, elle prend en entree une liste_d'item
# retourne une liste d'itemset
monItemset1= Itemset([pain, lait, couches,coca])
monItemset2 = Itemset([pain, pain, couches, cake, couches])
monItemset3= Itemset([coca])
monItemset4 = Itemset([pain,lait])
monItemset5 = Itemset([pain, biere])
monItemset6 = Itemset([couches, biere])

#print(monItemset1)
#print(monItemset2)
#print(monItemset3)

##### Test de la méthode supportItemset #####
# creation d'un itemset de taille 1
monItemset=Itemset([pain])

monsupportItemset=monItemset.supportItemset(monData)
#print(monsupportItemset)

##### Test de la méthode unionItemset #####

monUnionitemset=monItemset1.unionItemset(monItemset2)
#print(monUnionitemset)
# #test de unionItemset => les deux itemsets ne sont pas forcément de meme taille (?)

##### Test de la méthode unionValide #####
# #test de union valide : les deux itemsets doivent etre de meme taille n et leur union doit etre de taille n+1

#     #cas ou les deux itemsets sont de meme taille et leur union est de taille n+1
monUnionvalide1=monItemset4.unionValide(monItemset5)
#print(monUnionvalide1)

#     #cas ou l'union des deux itemsets n'est pas de taille n+1
monUnionvalide2=monItemset4.unionValide(monItemset6)
#print(monUnionvalide2)

#     #cas ou les deux itemsets ne sont pas de meme taille
monUnionvalide3=monItemset3.unionValide(monItemset4)
#print(monUnionvalide3)

# # => comment faire pour accéder à un élément d'un itemset
# # pour conserver les items qui sont soit dans monItemset, soit dans monItemset2 = retirer les items qui sont dans les 2
# #print(monItemset ^ monItemset2)


# ------ Pb !!!!!----
# ------ Renvoie: ''Les itemsets ne sont pas de la meme taille'' lorsqu'on fait l'union d'un itemset avec lui meme
# ------ Renvoie: ''L'union de ces deux itemsets n'est pas valide.'' et affiche quand meme
                  # l'union lorsqu'on l'union de 2 itemsets de taille 1

##### Test de la méthode verifSubset #####

monverifSubset= monItemset.verifSubSet([pain, lait, biere])
print(monverifSubset)



