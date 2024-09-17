import random
import string
import time

mot_de_passe = input("quel est le mot de passe : ") #le mot de passe a trouver

def mot_aleatoire():
     lettres = string.ascii_letters
     suiv = ""
     resultat = ""
     for carac in range(len(mot_de_passe)):
         while mot_de_passe[carac] != suiv:
             suiv = random.choice(lettres)
         resultat += suiv
     return resultat


debut = time.time()
print(mot_aleatoire())
print("Duree : " +str(time.time() - debut) + "secondes")