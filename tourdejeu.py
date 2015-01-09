from initialisation import *


def verif_saisie(nbcouleur, longsuite):
    liste = []
    listeSaisie = input('saisir une proposition :')

    if len(listeSaisie) != longsuite:
        return verif_saisie(nbcouleur, longsuite)

    for i in listeSaisie:
        try:
            temp = int(i)
        except ValueError:
            print("veuillez rentrer que des nombres")
            return verif_saisie(nbcouleur, longsuite)
        if temp < 1 or temp > nbcouleur:
            return verif_saisie(nbcouleur, longsuite)
        else:
            # print(temp)
            liste.append(temp)
    return liste


def compar_liste(liste_to_guest, liste_player):
    if (liste_to_guest == liste_player):
        print('vous avez trouvé la bonne solution')
        return True
    else:
        return False


test = False
param_init = param_init()  # initialisé les paramètres de jeu
print(param_init)

liste_to_guest = init(param_init[0], param_init[1])  # initialiser un liste à deviner
print(liste_to_guest)

while (test != True):
    liste_player = verif_saisie(param_init[0], param_init[1])  # Essai du joueur à comparer avec la liste à deviner
    print(liste_player)

    test = compar_liste(liste_to_guest, liste_player)
    print(test)