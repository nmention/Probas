from random import *
import random
compteur = 0
ballTotal = 0
couleur = []
nbBalles = []
liste = []
ballPile = []


evenement = "vert"

nbCouleur = (int)(input("Saisissez le nombre de couleurs"))
for i in range(nbCouleur):
    couleur.append((input("Saisissez la couleur " + str(i))))
    nb = (int)(input("Combien de balles de la couleur suivante : " + couleur[i]))
    ballTotal += nb
    nbBalles.append(nb)

liste = list(zip(couleur,nbBalles))
for element in liste:
    for i in range(element[1]):
        ballPile.append(str(element[0]))

print(ballPile)
random.shuffle(ballPile)
print(ballPile)
print(liste)
for i in range(100):
    tirage = random.choice(ballPile)
    if(tirage == evenement):
        compteur +=1

resultat = compteur / 100
print(resultat)





