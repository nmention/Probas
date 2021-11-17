from random import *
import random
compteur = 0
nbFaceDees = (int)(input("Donnez le nombre de faces de ce dé"))
valeurDees = []
event = 2 # évènement associé à la probabilité

# initialisation du nb des faces du dées + initialisation des valeurs pour chaque face
for faceDee in range(nbFaceDees):
    valeurDees.append((int)((input("Donnez la valeur de la face : " + (str)(faceDee)))))
print(valeurDees)

# tirage aléatoire pour 100 expériences
for i in range(100):
    tirage = random.choice(valeurDees);
    print(tirage)
    if(tirage == 2):
        compteur +=1

proba = compteur / 100
print(proba)
