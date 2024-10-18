#Écrire en Python une classe « Somme » ayant deux variables « n1 » et « n2 »
#  et une fonction membre « som() » qui calcule la somme. Dans la méthode 
# principale main demandez à l’utilisateur d’entrez deux entiers et passez-les
#  au constructeur par défaut de la classe « Somme » et afficher le résultat 
# de l’addition des deux nombres.
class Somme():
    def __init__(self, n1=0, n2=0):
        self.n1 = n1
        self.n2 = n2

    def addition(self):
        return self.n1+self.n2