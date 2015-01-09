from initialisation import *


def verif_saisie(nbcouleur, longsuite):
    liste = []
    liste_saisie = input('saisir une proposition :')

    if len(liste_saisie) != longsuite:
        return verif_saisie(nbcouleur, longsuite)

    for i in liste_saisie:
        try:
            temp = int(i)
        except ValueError:
            print("veuillez rentrer que des nombres")  # A corriger pour les charactères
            return verif_saisie(nbcouleur, longsuite)
        if temp < 1 or temp > nbcouleur:
            print("Entrer un nombre de couleur entre ", 1, " et ", nbcouleur)
            return verif_saisie(nbcouleur, longsuite)
        else:
            liste.append(temp)
    return liste


def compar_liste(liste_jeu, liste_joueur):
    nb_e_perfect_place, nb_e_bad_place, nb_e_wrong = 0, 0, 0

    if liste_jeu == liste_joueur:
        print('Vous avez trouvé la bonne solution')
        return True
    else:
        # regarder si le n°ème élement de la liste du joueur est dans la liste du jeu
        # si oui, regarder si il correspond au n°ème de la liste du jeu
        # si oui alors n°ème élément est bien placé, sinon il est dans la liste du jeu, mais mal placé
        for i, j in zip(liste_joueur, liste_jeu):

            if i in liste_jeu:
                if i == j:
                    nb_e_perfect_place += 1
                else:
                    nb_e_bad_place += 1
            else:
                nb_e_wrong += 1

        print("nombre d'éléments bien placés :", nb_e_perfect_place)
        print("nombre d'éléments mal placés :", nb_e_bad_place)
        print("nombre d'éléments mauvais :", nb_e_wrong)
        return False


test = False
parametre_init = param_init()  # initialisé les paramètres de jeu
print(parametre_init)

liste_to_guest = init(parametre_init[0], parametre_init[1])  # initialiser un liste à deviner
print(liste_to_guest)

while not test:
    liste_player = verif_saisie(parametre_init[0], parametre_init[1])  # Essai du joueur
    print(liste_player)
    test = compar_liste(liste_to_guest, liste_player)  # Comparaison des listes
    print(test)