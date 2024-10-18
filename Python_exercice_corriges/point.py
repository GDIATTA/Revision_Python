#Réaliser en Python  une classe point permettant de manipuler un point
#  d'un plan.on prévoira :

# 1) un point est définit par ses coordonnées x et y (des membres privés)

# 2) les constructeurs 

# 3) une fonction membre déplace effectuant une translation définie par ses
#  deux arguments dx et dy (double)

# 4)une fonction membre affiche se contentant d'afficher les coordonnées cartésiennes du point.

# 5)une fonction membre saisir se contentant de saisir les coordonnées cartésiennes du point.

# 6)une fonction membre distance effectuant calculant la distance entre deux point.

# 7)une fonction membre milieu donnant le milieu d'un segment.

# 8)un petit programme d'essai (main) gérant la classe point.

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    # function of mouvment x+=dx,y+=dy
    def deplacement(self,dx,dy):
        return self.set_x(self.get_x()+dx), self.set_y(self.get_y()+dy)
    
    def affich(self):
        print(self.get_x, self.get_y)

    def saisir(self):
        self.x = float(input("Entrer x : "))
        self.y = float(input("Entrer y : "))

    def distance(self,p):
        x1 = (self.x - p.x)**2 
        y1 = (self.y - p.y)**2
        return (x1+y1)**1/2
    
    def milieu(self,p):
        p1 = Point()
        p1.x = (self.get_x()+p.x)/2
        p1.y = (self.get_y()+p.y)/2
        return p1
