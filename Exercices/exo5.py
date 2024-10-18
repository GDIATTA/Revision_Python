def affich(nom,age):
    print(nom + " a " + str(age) + " ans.")

import math
def volume(rayon,hauteur):
    return (pow(rayon,2)*hauteur*math.pi)/3

def affich1():
    vec1=["Luka","27","marié"]
    print("Je m'appelle "+ vec1[0] +", j'ai "+ vec1[1] +" ans.")

def affich2():
    vec2=[[1230,"ALLON","TIN",13],[1230,"ALLON","TIN",13],[1230,"GAUSS","TIN",13]]
    print("bon"+ vec2[2][1])
#affich("Mohammed",30)
print(volume(3,2))
affich1()
affich2()
