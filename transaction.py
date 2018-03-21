class Item:
    def __init__(self,nom_item,spe_tech=None):
        self.nom_item=nom_item
        self.spe_tech=spe_tech
    def __repr__(self):
        return "{} ({})".format(self.nom_item, self.spe_tech)


# Permet de creer les transactions
class Transaction:
    def __init__(self,nom_transac,lst_item):
        self.nom_transac=nom_transac
        self.lst_item=lst_item
        maListe=[]
        for item in lst_item:
            maListe.append(Item(item))

    def __repr__(self):
        return "{} : {}".format(self.nom_transac,self.lst_item)






#####################
# PROGRAMME PRINCIPAL
#####################

monCaddie1= Transaction("T1","Pain")
monCaddie2 = Transaction("T2",["pain", "couches", "biere", "œufs"])



print(monCaddie1)
print(monCaddie2)


