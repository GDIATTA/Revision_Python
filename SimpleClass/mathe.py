class Mathe():
    x=0
    y=0
    def __init__(self, x, y):
        self.x=x
        self.y=y
    
    def addition(self):
        return self.x+self.y
    
    def soustraction(self):
        return self.x-self.y
    
    def multiplication(self):
        return self.x*self.y
    
    def division(self):
        if self.y==0:
            return "Impossible to divide by zero"
        else:
            return self.x/self.y