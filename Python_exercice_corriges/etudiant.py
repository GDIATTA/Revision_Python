# Écrire classe Python appelée « Etudiant » avec les membres suivant :
# nom : (de type char),
# note1, note2 : (de type float)
# calc_moy() : calcule la note moyenne.
# afficher () : affiche le nom et la note moyenne.
 # Le programme principal (main) demande à l’utilisateur d’entrer le nom
 #  et les notes d'un étudiant. et affiche leur nom et la note moyenne.

class Etudiant():
    def __init__(self, nom, note1, note2):
        self.nom = nom
        self.note1 = note1
        self.note2 = note2

    # calcule the average point 
    def calc_moy(self):
        return (self.note1 + self.note2)/2
    
    def affich(self):
        print(self.nom + " a une note moyenne de : " + str(self.calc_moy()))