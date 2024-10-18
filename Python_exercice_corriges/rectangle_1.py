# Écrire en Python
# un programme utilisant une classe rectangle dont le constructeur prend
#  deux paramètres, largeur et hauteur et qui offre les fonctions suivantes :

# 1) calcul du périmètre

# 2) calcul de la surface

# 3)  affichage

# ainsi que les accesseurs et mutateurs triviaux (lecture et modification
#  de la largeur et de la hauteur).
from rectangle import Rectangle

class Rectangle_1(Rectangle):
    def __init__(self, a, b):
        Rectangle.__init__(self, a, b)

    def get_a(self):
        return self.a
    
    def get_b(self):
        return self.b

    def perimetre(self):
        return 2*(self.get_a() + self.get_b())
    