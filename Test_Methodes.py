from item import Item
from itemset import Itemset
from dataset import Dataset
from transaction import Transaction
from regles_asso import Association

#_______________________________________________________________________________________________________________________

    #############################################
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

    #############################################
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

monCaddie4= Transaction("T4")
monCaddie4.ajouterItem(pain)
monCaddie4.ajouterItem(lait)

monCaddie5= Transaction("T5")
monCaddie5.ajouterItem(pain)
monCaddie5.ajouterItem(couches)
monCaddie5.ajouterItem(biere)
monCaddie5.ajouterItem(oeufs)

monCaddie6= Transaction("T6")
monCaddie6.ajouterItem(lait)
monCaddie6.ajouterItem(couches)
monCaddie6.ajouterItem(biere)
monCaddie6.ajouterItem(coca)

monCaddie7= Transaction("T7")
monCaddie7.ajouterItem(pain)
monCaddie7.ajouterItem(lait)
monCaddie7.ajouterItem(couches)
monCaddie7.ajouterItem(biere)

monCaddie8= Transaction("T8")
monCaddie8.ajouterItem(pain)
monCaddie8.ajouterItem(lait)
monCaddie8.ajouterItem(couches)
monCaddie8.ajouterItem(coca)

# Methode2: Creation d'une transaction a l'aide d'une liste de produits transformer en item !!!!! AREVOIR !!!!

monCaddie9 = Transaction("T9")
monCaddie9.ajouterListeProd([Item("pommes",["Golden","10kg"]), Item("pain")])
#print(monCaddie4)

#print(monCaddie4.lst_item[1].nomItem)   #permet d'accéder à l'item d'indice 1 du caddie 4

#_______________________________________________________________________________________________________________________

    #############################################
    ######## TEST CLASS DATASET #############

# Creation du dataset

monData=Dataset()
monData.ajouterTransaction(monCaddie1)
monData.ajouterTransaction(monCaddie2)
monData.ajouterTransaction(monCaddie3)
monData.ajouterTransaction(monCaddie4)
#print(monData)

monData2=Dataset()
monData2.ajouterTransaction(monCaddie4)
monData2.ajouterTransaction(monCaddie5)
monData2.ajouterTransaction(monCaddie6)
monData2.ajouterTransaction(monCaddie7)
monData2.ajouterTransaction(monCaddie8)

#___________________________________________________________

    ##### TEST METHODE SINGLETON (Dataset) #####

#print(monData.singleton())

#___________________________________________________________

    ##### TEST METHODE ITEMSETFREQ (Dataset) #####

    # Recuperation de la liste de singleton qui est une liste d'itemset de taille 1

lst_itemset=monData.singleton()
#print(lst_itemset)

    # Recherche d'itemset frequent à partir d'une liste d'itemset de taille 1 et d'un minSup

#print(monData.itemsetFreq(lst_itemset))



#_______________________________________________________________________________________________________________________

    #############################################
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

    ##### TEST METHODE SUPPORT (Itemset) #####

monsupportItemset=Itemset3.supportItemset(monData)
#print(monsupportItemset)

#___________________________________________________________

    ##### TEST METHODE UNIONITEMSET (Itemset) #####

monUnionitemset=Itemset1.unionItemset(Itemset2)
#print(monUnionitemset)

#___________________________________________________________

    ##### TEST METHODE UNIONVALIDE (Itemset) #####

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

    ##### TEST METHODE VERIFSUBSET (Itemset) #####


    ## pour rappel: comment sont définis les itemsets créés plus haut (quels items ils contiennent)
# Itemset1= Itemset([pain, lait, couches, coca]) : taille 4
# Itemset2 = Itemset([pain, pain, couches, cake, couches]) : taille 3
# Itemset3= Itemset([coca]) : taille 1
# Itemset4 = Itemset([pain, lait]) : taille 2
# Itemset5 = Itemset([pain, biere]) : taille 2
# Itemset6 = Itemset([couches, biere]) : taille 2
# Itemset8=Itemset([pain]) : taille 1


## on verifie que tous les subsets de taille 1 d'un itemset de taille 2 sont frequants
monItemset1 = Itemset([pain, lait])

#monverifSubset=monItemset1.verifSubset([pain, lait])
#print(monverifSubset)

## on vérifie que tous les subsets de taille 2 d'un itemset de taille 3 sont fréquents

monItemset2 = Itemset([pain,lait,coca])
monItemsetFreq1 = Itemset([pain,lait])
monItemsetFreq2 = Itemset([pain,coca])
monItemsetFreq3 = Itemset([lait,coca])
    #Itemset([lait,coca]) = Itemset([coca,lait])

    #cas où tous les subsets sont fréquents
monverifSubset = monItemset2.verifSubset([monItemsetFreq1, monItemsetFreq2, monItemsetFreq3]) #censé retourner True
#print(monverifSubset)

    #cas où l'un des subsets est fréquent
#monverifSubset2 = monItemset2.verifSubset([monItemsetFreq1, monItemsetFreq2]) # censé retourner False
#print(monverifSubset2)

    #cas où aucun des subsets n'est fréquent
#monverifSubset3 = monItemset2.verifSubset([Itemset5]) # censé retourner False
#print(monverifSubset3)

#___________________________________________________________

    ##### TEST METHODE  DE CLASSE SUPERSETCAND (Itemset) #####
#superset = Itemset.supersetCand([monItemsetFreq1, monItemsetFreq2, monItemsetFreq3])
#print(superset)


#___________________________________________________________

    ##### TEST REGLES_ASSO (Itemset) #####
#print(monItemset2.regles_asso())

#_______________________________________________________________________________________________________________________

    ##### TEST APRIORI (Dataset) #####

#print(monData.aPriori(minsup=2))
#print(monData2.aPriori(minsup=2))

#_______________________________________________________________________________________________________________________

    #############################################
    ######## TEST CLASS REGLES_ASSO #############
monAsso = Association(monItemset2, Itemset3)
print(monAsso)