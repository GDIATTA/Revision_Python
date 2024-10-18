## Écrire en Python une classe «Rectangle» ayant deux variables « a »
#  et « b » et une fonction membre « surface() » qui retournera la
#  surface du rectangle.


class Rectangle :
    a=0;
    b=0;
    def __init__(self, x, y) : 
        self.a = x;
        self.b = y;

    def surface(self) :
        return self.a*self.b;


p1=Rectangle(2,3);
print(p1.surface());

