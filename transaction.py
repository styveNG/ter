from Items import Item


# Permet de creer les transactions
class Transaction:
    def __init__(self,nom_transac):
        self.nom_transac=nom_transac
        self.lst_item= []


    #permet d'ajouter un item dans la liste d'item
    def ajouterItem(self, unItem):
        self.lst_item.append(unItem)

    #transforme chaque produit de la liste en item
    def ajouterListeProd(self, listeProd):
        for produit in listeProd:
            item = Item(produit)  #transformation du produit parcouru en item
            self.ajouterItem(item) #appel à la méthode ajouter item

    def __repr__(self):
        return "{} : {}".format(self.nom_transac,self.lst_item)






#####################
# PROGRAMME PRINCIPAL
#####################

pain = Item("pain", ["250g"])
couches = Item("couches", ["20couches", "5euros"])

monCaddie1= Transaction("T1")
monCaddie2 = Transaction("T2")

monCaddie1.ajouterItem(pain)
monCaddie1.ajouterItem(couches)

monCaddie2.ajouterListeProd(["pain", "couches", "biere", "œufs"])

#print(monCaddie1)
#
#print(monCaddie2)
# # affiche T2 : [pain: None, couches: None, biere: None, œufs: None] : c'est une liste qui contient des objets de type item
# # c'est parce que dans le repr de item on lui a demandé d'afficher le nom et la spé tech qu'on a ce résultat*
# #si on n'avait demandé dans ce repr de n'afficher que le nom, on n'aurait eu que le nom des items
#
# print(monCaddie2.lst_item[1].nom)   #permet d'accéder à l'item d'indice 1 du caddie 2


