from SimpleClass.Point import Point

class Carre (Point):
    long = 20
    larg = 10

    def __init__(self, long, larg, x, y):
        self.long = long
        self.larg = larg
        Point.__init__(self, x, y)

    def affich(self):
        return super().affich()