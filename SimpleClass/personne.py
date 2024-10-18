class Personne():
    firstname   = "Gauss"
    lastname = "Jatta"

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def affich(self):
        print(self.firstname,self.lastname)

#class Student(Personne):
 #   pass

    