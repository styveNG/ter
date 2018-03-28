from Items import Item

# Permet de creer les transactions
class Transaction:
    def __init__(self,nom_transac):
        self.nom_transac=nom_transac
        self.lst_item= []


    #permet d'ajouter un item dans la liste d'item
    def ajouterItem(self, unItem):
        self.lst_item.append(unItem)

    #IDEE: Creer une methode qui rajoute les spetech
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

#Creation des items
pain = Item("pain", ["250g"])
couches = Item("couches", ["20couches", "5euros"])

#Creation d'une transaction avec des items crees precedement
monCaddie1= Transaction("T1")
monCaddie1.ajouterItem(pain)
monCaddie1.ajouterItem(couches)
#print(monCaddie1)
#print(monCaddie1.lst_item[0].spetech) : permet d'accéder à la spetech de l'item d'indice 0 du caddie 1

#Creation d'une transaction a l'aide d'une liste de produit transformer en item
monCaddie2 = Transaction("T2")
monCaddie2.ajouterListeProd(["pain", "couches", "biere", "œufs"])
#print(monCaddie2)
#print(monCaddie2.lst_item[1].nomItem)   #permet d'accéder à l'item d'indice 1 du caddie 2


