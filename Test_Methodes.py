from item import Item
from itemset import Itemset
from dataset import Dataset
from transaction import Transaction

#_______________________________________________________________________________________________________________________

######## TEST CLASS ITEM #############

# Creation des items

pain = Item("pain")
lait = Item("lait", ["1L", "brique"])
couches = Item("couches", ["20couches"])
biere = Item("biere", ["50cL", "canette"])
oeufs = Item("oeufs", ["6", "barquette"])
coca = Item("coca", ["2L", "bouteille", "zero"])
cake = Item("cake")
# print(biere)

#_______________________________________________________________________________________________________________________

######## TEST CLASS TRANSACTION #############

# Methode1: Creation d'une transaction avec des items existants (cf.CLASS ITEM)

monCaddie1= Transaction("T1")
monCaddie1.ajouterItem(pain)
monCaddie1.ajouterItem(couches)
monCaddie1.ajouterItem(biere)
monCaddie1.ajouterItem(lait)

#print(monCaddie1)

#print(monCaddie1.lst_item[0].spetech) #: permet d'accéder à la spetech de l'item d'indice 0 du caddie 1

monCaddie2 = Transaction("T2")
monCaddie2.ajouterItem(couches)
monCaddie2.ajouterItem(cake)
monCaddie2.ajouterItem(coca)
monCaddie2.ajouterItem(oeufs)
#print(monCaddie2)

monCaddie3 = Transaction("T3")
monCaddie3.ajouterItem(lait)
monCaddie3.ajouterItem(pain)
monCaddie3.ajouterItem(oeufs)
#print(monCaddie3)

# Methode2: Creation d'une transaction a l'aide d'une liste de produits transformer en item !!!!! AREVOIR !!!!

monCaddie4 = Transaction("T4")
monCaddie4.ajouterListeProd([Item("pommes",["Golden","10kg"]), Item("pain")])
#print(monCaddie4)

#print(monCaddie4.lst_item[1].nomItem)   #permet d'accéder à l'item d'indice 1 du caddie 4

#_______________________________________________________________________________________________________________________

######## TEST CLASS DATASET #############

# Creation du dataset

monData=Dataset()
monData.ajouterTransaction(monCaddie1)
monData.ajouterTransaction(monCaddie2)
monData.ajouterTransaction(monCaddie3)
monData.ajouterTransaction(monCaddie4)
#print(monData)

#___________________________________________________________

    ##### TEST METHODE SINGLETON #####

#print(monData.singleton())

#___________________________________________________________

    ##### TEST METHODE ITEMSETFREQ  #####

    # Recuperation de la liste de singleton qui est une liste d'itemset de taille 1

lst_itemset=monData.singleton()
#print(lst_itemset)

    # Recherche d'itemset frequent à partir d'une liste d'itemset de taille 1 et d'un minSup

#print(monData.itemsetFreq(lst_itemset))

#___________________________________________________________

    ##### TEST APRIORI  #####

#monData.aPriori(minsup=2)


#_______________________________________________________________________________________________________________________

######## TEST CLASS ITEMSET #############

# Itemset herite de la classe set, elle prend en entree une liste_d'item
# retourne une liste d'itemset

Itemset1= Itemset([pain, lait, couches, coca])
Itemset2 = Itemset([pain, pain, couches, cake, couches])
Itemset3= Itemset([coca])
Itemset4 = Itemset([pain, lait])
Itemset5 = Itemset([pain, biere])
Itemset6 = Itemset([couches, biere])
Itemset8=Itemset([pain])


#print(Itemset1)
#print(Itemset2.lst_item[0].nomItem)
#print(Itemset2)
#print(Itemset3)

# Recherche d'itemset frequent à partir d'une liste d'itemset de taille n et d'un minSup

#lst_itemset2=[Itemset1,Itemset2,Itemset3,Itemset4,Itemset5,Itemset6]
#print(monData.itemsetFreq(lst_itemset2))

#___________________________________________________________

    ##### TEST METHODE SUPPORT #####

monsupportItemset=Itemset3.supportItemset(monData)
#print(monsupportItemset)

#___________________________________________________________

    ##### TEST METHODE UNIONITEMSET #####

monUnionitemset=Itemset1.unionItemset(Itemset2)
#print(monUnionitemset)

#___________________________________________________________

    ##### TEST METHODE UNIONVALIDE #####

    # Les deux itemsets doivent etre de meme taille n et leur union doit etre de taille n+1

    #cas ou les deux itemsets sont de meme taille et leur union est de taille n+1

# Itemset1= Itemset([pain, lait, couches, coca]) : taille 4
# Itemset2 = Itemset([pain, pain, couches, cake, couches]) : taille 3
# Itemset3= Itemset([coca]) : taille 1
# Itemset4 = Itemset([pain, lait]) : taille 2
# Itemset5 = Itemset([pain, biere]) : taille 2
# Itemset6 = Itemset([couches, biere]) : taille 2
# Itemset8=Itemset([pain]) : taille 1

#monUnionvalide1=Itemset4.unionValide(Itemset5)
#print(monUnionvalide1)

    #cas ou l'union des deux itemsets n'est pas de taille n+1

# monUnionvalide2=Itemset4.unionValide(Itemset6)
# print(monUnionvalide2)

    #cas ou les deux itemsets ne sont pas de meme taille

# monUnionvalide3=Itemset3.unionValide(Itemset4)
# print(monUnionvalide3)

# monUnionvalide4=Itemset1.unionValide(Itemset2)
# print(monUnionvalide4)

# # pour conserver les items qui sont soit dans monItemset, soit dans monItemset2 = retirer les items qui sont dans les 2
#print(monItemset ^ monItemset2)

#___________________________________________________________

##### TEST METHODE VERIFSUBSET #####

# Itemset1= Itemset([pain, lait, couches, coca]) : taille 4
# Itemset2 = Itemset([pain, pain, couches, cake, couches]) : taille 3
# Itemset3= Itemset([coca]) : taille 1
# Itemset4 = Itemset([pain, lait]) : taille 2
# Itemset5 = Itemset([pain, biere]) : taille 2
# Itemset6 = Itemset([couches, biere]) : taille 2
# Itemset8=Itemset([pain]) : taille 1


## on verifie que tous les subsets de taille 1 d'un itemset de taille 2 sont frequants
monItemset1 = Itemset([pain, lait])

monverifSubset=monItemset1.verifSubset([pain, lait])
#print(monverifSubset)

## on vérifie que tous les subsets de taille 2 d'un itemset de taille 3 sont fréquents

monItemset2 = Itemset([pain,lait,coca])
monItemsetFreq1 = Itemset([pain,lait])
monItemsetFreq2 = Itemset([pain,coca])
monItemsetFreq3 = Itemset([lait,coca]) #essayer avc coca lait

monverifSubset2 = monItemset2.verifSubset([monItemsetFreq1, monItemsetFreq2, monItemsetFreq3])