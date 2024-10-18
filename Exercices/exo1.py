x,y,z ="Bonjour",5,5.5;
print(type(x))
print(type(y))
print(type(z))

import math
#rayon = float(input("Saisir le rayon :"))
#hauteur = float(input("Saisir la hauteur :"))
#V = math.pi*rayon**2*hauteur
#print(V)

x = 3
print("Le chat " + str(x))

Hypotenuse = float(input("Saisir le hypothénus :"))
CoteOppose = float(input("Saisir le coté opposé :"))
sinalpha = CoteOppose/Hypotenuse

print("angle ", math.degrees(sinalpha))

x = int(input("Saisir un nombre entier : "))
print(x)


while True:
    try:
        x = int(input("Saisir un nombre :"))
        break
    except:
        print("Ceci n'est pas un nombre entier ")

print("Ok!")