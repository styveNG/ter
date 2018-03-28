# # Methode Transaction:

#print(monCaddie2)
# # affiche T2 : [pain: None, couches: None, biere: None, œufs: None] : c'est une liste qui contient des objets de type item
# # c'est parce que dans le repr de item on lui a demandé d'afficher le nom et la spé tech qu'on a ce résultat*
# #si on n'avait demandé dans ce repr de n'afficher que le nom, on n'aurait eu que le nom des items


######## Test de la class DATASET #############
from Items import Item
from transaction import Transaction

# Permet de creer le jeu de donnees TRANSACTIONS --> Items
class Dataset:
    def __init__(self):
        self.lst_transactions=[]

    def ajouterTransaction(self,maTransaction):
        self.lst_transactions.append(maTransaction)

    def __repr__(self):
        return "{}".format(self.lst_transactions)

##################
#Programme Principal
##################
# Creation des items
pain = Item("pain")
lait = Item("lait", ["1L", "brique"])
couches = Item("couches", ["20couches"])
biere = Item("biere", ["50cL", "canette"])
oeufs = Item("oeufs", ["6", "barquette"])
coca = Item("coca", ["2L", "bouteille", "zero"])
cake = Item("cake")


# Creation des transactions
monCaddie1= Transaction("T1")
monCaddie1.ajouterItem(pain)
monCaddie1.ajouterItem(couches)
monCaddie1.ajouterItem(biere)

monCaddie2 = Transaction("T2")
monCaddie2.ajouterItem(couches)
monCaddie2.ajouterItem(cake)
monCaddie2.ajouterItem(coca)
monCaddie2.ajouterItem(oeufs)

monCaddie3 = Transaction("T3")
monCaddie3.ajouterItem(lait)
monCaddie3.ajouterItem(pain)
monCaddie3.ajouterItem(oeufs)
#### Fin des transactions ####

# Creation du dataset
monData=Dataset()
monData.ajouterTransaction(monCaddie1)
monData.ajouterTransaction(monCaddie2)
monData.ajouterTransaction(monCaddie3)

print(monData)