## Créez un programme Python qui crée et initialise un tableau,
#  puis insère un élément à la position spécifiée dans ce tableau
#  (de 0 à N-1).Pour insérer un nouvel élément dans le tableau,
#  déplacez les éléments de la position d'insertion donnée vers
#  une position vers la droite.
validInput = False;
while not validInput:
    try:
        nbelt=int(input("Entrer le nb elt : "));
        elt = int(input("Entrer l'elt : "));
        pos = int(input("Entrer la position : "));
        validInput=True;
    except:
        print("Entrer un nbr entier valid!");
tab = [0]*(nbelt+1);
for i in range(nbelt):
    validInput=False;
    while not validInput:
        try:
            tab[i] = int(input("Entrer un elt i : "));
            validInput=True;
        except:
            print("Entrer un nbr entier valid!");
   
for i in range(nbelt,pos,-1):
    tab[i] = tab[i-1];

tab[pos]= elt;
for i in range(nbelt+1) :
    print(tab[i]);






##Écrire un programme Python pour déclarer un tableau, 
# puis saisir ses éléments à partir de l'utilisateur et
#  trouver la somme des éléments du tableau
#validInput = False;
#while not validInput:
#    try:
#        nbelt= int (input("Entrer un nb elt : "));
#        validInput = True;
#     except:
#        print("Entrer un nbr entier valid! ");
#tab = [0]*nbelt;
#for i in range(nbelt):
#    validInput = False;
#    while not validInput:
#        try:
#            tab[i] = int (input("Entrer un elt i : "));
#            validInput =True;
#        except:
#            print("Entrer un nbr entier valid!");

    
#Som = 0;
#for i in range(nbelt):
#    Som += tab[i];
#print(Som);   


## Écrivez un programme Python pour déclarer et initialiser un tableau,
#  puis saisissez ses éléments à partir de l'utilisateur et affichez le tableau.
#validInput = False;
#while not validInput:
#    try:
#        print("Entrer le nombre d'éléments");
#        nb = int(input("Entrer le nombre d'éléments :"));
#        validInput = True;
#    except ValueError:
#        print("Entrer un nombre entier valide");
#tab = [0]*nb;
#for i in range(nb):
#    tab[i] = input("Entrer un élément : ");
#for i in range(nb):
#    print(tab[i]);