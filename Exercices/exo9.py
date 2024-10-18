##Écrivez un programme Python pour saisir un nombre et calculer la
#  somme de ses chiffres en utilisant la boucle for.
num = int(input("Saisir un nombre :"));
somme = 0;
while(num!=0):
    somme += num%10;
    num = num//10;
print("Somme de chiffres = ", somme);




## Écrire un programme Python qui permet d'inverser les chiffres d'un
#  entier N saisi par l'utilisateur.   par exemple  N=35672  
# le résultat affiché doit être  27653 
#nb = int(input("Saisir un nombre :"));
#r = 0;
#while nb > 0:
#    r = r*10;
#    r = r + nb%10;
#    nb = int(nb/10);
#print(r);


## Écrivez un programme Python pour saisir un nombre de l'utilisateur
#  et recherchez le premier et le dernier chiffre d'un nombre en 
# utilisant une boucle.
#nb = int(input("Saisir un nombre :"));
#last = nb%10;
#first = nb;
#while(first>=10):
#    first = first//10;
#print("Premier chiffre= ",first);
#print("Dernier chiffre= ",last);



## Écrivez un programme Python pour entrer un nombre de l'utilisateur
#  et comptez le nombre de chiffres dans l'entier donné en utilisant
#  une boucle.
#num = int(input("Saisir un nombre :"));
#compteur = 0;
#while num!=0:
#    compteur += 1;
#    num //=10;
#print("Nombre de chiffres :",compteur);

