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
            self.ajouterItem(produit) #appel à la méthode ajouter item

    def __repr__(self):
        return "{} : {}".format(self.nom_transac,self.lst_item)

