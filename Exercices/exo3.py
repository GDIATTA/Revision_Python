while True:
    try:
        nb = int(input("Saisir un nombre entier :"))
        break
    except ValueError:
        print("Ceci n'est pas un nombre entier :")
print("Ok")
if nb %2==0:
    print("Ce nombre est pair :")
elif nb %2==1 and nb%3==0:
    print("Ce nombre est impair, mais est multiple de 3")
else:
    print("Ce nombre n'est ni pair ni multiple de 3")
     