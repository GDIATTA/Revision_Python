class Point():
    x = 0
    y = 0

    def __init__(self, x=0, y):
        self.x = x
        self.y = y
    
    def affich(self):
        print("This point have of coordinate : (" + str(self.x)+ "," + str(self.y)+ ")")


