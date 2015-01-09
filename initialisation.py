from random import *


def param_init():
    leave = 0
    liste = []

    while (leave != 1):
        leave = 0
        nbcouleur = input("Nombre de couleur ?")
        if (nbcouleur.isnumeric()):
            liste.append(int(nbcouleur))
            break

    leave = 0

    while (leave != 1):
        longsuite = input("Longueur de la suite ?")
        if (longsuite.isnumeric()):
            liste.append(int(longsuite))
            break

    leave = 0

    while (leave != 1):
        nbessai = input("Nombre d'essai ?")
        if (nbessai.isnumeric()):
            liste.append(int(nbessai))
            break

    return (liste)


def init(nbcouleur, longsuite):
    liste = []  # Liste à découvrir

    for i in range(longsuite):
        liste.append(randrange(1, nbcouleur + 1))

    return (liste)


#liste = param_init()
# print(liste)
#
#print(init(liste[0], liste[1]))