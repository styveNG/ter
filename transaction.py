# Permet de creer les transactions
class Transaction:
    def __init__(self,nom_transac,lst_item):
        self.nom_transac=nom_transac
        self.lst_item=lst_item

    def __repr__(self):
        return "{} : {}".format(self.nom_transac,self.lst_item)





#####################
# PROGRAMME PRINCIPAL
#####################

monCaddie1= Transaction("T1",["pain", "lait"])
monCaddie2= Transaction("T2",["pain", "couches", "biere", "œufs"])
monCaddie3= Transaction("T3",["lait", "couches", "biere", "coca"])
monCaddie4= Transaction("T4",["pain", "lait", "couches", "biere"])
monCaddie5= Transaction("T5",["pain", "lait", "couches", "coca"])
monCaddie6= Transaction("T6",["pain", "lait", "coca"])

print(monCaddie1)
print(monCaddie2)
print(monCaddie3)
print(monCaddie4)
print(monCaddie5)
print(monCaddie6)
