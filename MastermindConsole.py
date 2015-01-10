from initialisation import *
from tourdejeu import *

print("Bienvenue sur le jeu MASTERMIND !\n\n")
play = 0

while play != 'non':
    play = input("voulez-vous jouer (oui or non)? ")
    if play == 'oui':
        print('Prener place, la partie va commencer !!\n')

        test = False
        parametre_init = param_init()  # initialisé les paramètres de jeu
        # print(parametre_init)

        liste_to_guest = init(parametre_init[0], parametre_init[1])  # initialiser un liste à deviner
        # print(liste_to_guest)

        liste_player, essai = 0, 1

        while not test:
            print('Essai n°', essai)
            liste_player = verif_saisie(parametre_init[0], parametre_init[1])  # Essai du joueur
            # print(liste_player)
            test = compar_liste(liste_to_guest, liste_player)  # Comparaison des listes
            essai += 1
            if essai == parametre_init[2] + 1:
                print("Nombre d'essais atteind\n PERDU !")
                print("Il fallait trouver :", liste_to_guest)
                break
            elif test == True:
                print('FELICITATION !!')
                # print(test)
    elif play == 'non':
        print('Une prochaine fois!')
    else:
        print('Veuiller dire oui ou non..')