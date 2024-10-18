validInput = False;
while not validInput:
      try:
          nb = int(input("Entrer un nombre entier nb1 :"));
          validInput = True;
      except:
           print("Entrer un nombre entier");
total=0;
for i in range(1,nb):
     if nb%i == 0:
          total=total+i;
if nb==total:
     print("nb est parfait");
else:
     print("nb n'est pas parfait");
