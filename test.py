from random import randrange
# def verif_saisie(nbcouleur, longsuite):
#     liste = []
#     liste_saisie = input('Saisir une proposition :')
#
#     if len(liste_saisie) != longsuite:
#         return verif_saisie(nbcouleur, longsuite)
#
#     for i in liste_saisie:
#         try:
#             temp = int(i)
#         except ValueError:
#             print("Veuillez rentrer que des nombres")  # A corriger pour les charactères
#             return verif_saisie(nbcouleur, longsuite)
#         if temp < 1 or temp > nbcouleur:
#             print("Entrer un nombre de couleur entre ", 1, " et ", nbcouleur)
#             return verif_saisie(nbcouleur, longsuite)
#         else:
#             liste.append(temp)
#     return liste

def liste_ia(nbcouleur, longsuite, liste):
    if liste == None: # on initialise la première proposistion
        liste = []
        for i in range(longsuite):
            liste.append(randrange(1, nbcouleur + 1))
        return liste
    else:
        print('1')

liste = None

liste_ordi = liste_ia(6,4, liste)

print(liste_ordi)