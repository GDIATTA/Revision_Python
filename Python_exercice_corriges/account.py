# Écrire un programme en Python
# qui simule la gestion d’un simple compte bancaire. Le compte est créé
#  avec un solde initial. Il est possible de déposer et de retirer des fonds,
#  d’ajouter des intérêts et de connaître le solde actuel. Cela devrait être
#  implémenté dans une classe nommée Account qui comprend:


# 1) Un constructeur par défaut qui met le solde initial à zéro.
# 2) Un constructeur qui accepte une balance initial comme paramètre.
# 3) Une fonction getBalance qui renvoie le solde actuel.
# 4) Une méthode deposer pour déposer un montant spécifié.
# 5) Une méthode retirer pour retirer un montant spécifié.
# 6) Une méthode ajouter_Interet pour ajouter de l’intérêt au compte.
#La méthode  ajouter_Interet  prend le taux d’intérêt comme paramètre 
# et modifie le solde du compte en solde * (1 + taux d’intérêt).

class Account():
    def __init__(self,balance=0):
        self.balance = balance

    def get_balance(self):
        return self.balance
    
    def depose(self, montant):
        return self.get_balance()+montant
    
    def retire(self, montant):
        return self.get_balance()-montant
    
    def ajout_Interet(self, taux):
        return self.get_balance()*(1+taux)