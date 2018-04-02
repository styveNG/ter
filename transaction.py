from item import Item

# Permet de creer les transactions
class Transaction:
    def __init__(self,nom_transac):
        self.nom_transac=nom_transac
        self.lst_item= []

    #permet d'ajouter un item dans la liste d'item
    def ajouterItem(self, unItem):
        self.lst_item.append(unItem)

    #IDEE: Creer une methode qui rajoute les spetech???
    def ajouterSpetech(self):
        self.lst_spetech=[]
        pass

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




