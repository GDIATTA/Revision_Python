from somme import Somme
from etudiant import Etudiant

# enter n1 and n2 like input and then print the result of their sum
n1=int(input("Entrer n1 : "))
n2=int(input("Entrer n2  : "))
print(Somme(n1,n2).addition())

# require the student to enter its name and its notes and then print the average

name = input("Enter your name : ")
note1 = float(input("Enter your note1 : "))
note2 = float(input("Enter your note2 : "))
print(Etudiant(name,note1,note2).affich())


