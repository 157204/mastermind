from random import randrange
# def verif_saisie(nbcouleur, longsuite):
# liste = []
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

def changelettre(lettre):
    x = ord(lettre)
    if x >= 65 and x <= 90:  # to miniscule
        x += 32
    elif x >= 97 and x <= 122:
        x -= 32

    x = chr(x)
    print(x)

    return x


changelettre(input('lettre : '))

