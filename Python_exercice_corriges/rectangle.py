# Écrire en Python une classe «Rectangle» 
# ayant deux variables « a » et « b » et une fonction
#  membre « surface() » qui retournera la surface du rectangle.
class Rectangle():
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    # return the surface of the rectangle
    def surface(self):
        return self.a*self.b