#i=0
#for i in range(0,101,2):
#    print(i)

#while(i<101):
#    print(i)
#    i=i+2

import random
vec1=[]
for i in range(10):
    vec1.append(random.randint(1,10))

print(vec1)

nb=int(input("Saisir un nombre entier :"))
#if nb in vec1:
#    print("Gagné")
#else:
#    print("le nombre n'est pas trouvé")
vec1.sort()
print(vec1)
j=0
while j< len(vec1) and vec1[j] != nb:
    j+=1

if j < len(vec1):
    print("Gagné")
else :
    print("Perdu")


