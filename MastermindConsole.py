from initialisation import *
from tourdejeu import *
from MastermindIA import *

def mastermindconsole(main):
    play = True
    while play:
        play = input("voulez-vous jouer (oui or non)? Ou voulez vous que l'ordinateur joue (IA)?").capitalize()
        essai = 0
    # -------- JOUEUR --------
        if play == 'Oui' or play == 'Yes' or play == 'Y':
            print('Prener place, la partie va commencer !!\n')

            test = False
            parametre_init = param_init()  # initialisé les paramètres de jeu

            liste_to_guest = init(parametre_init[0], parametre_init[1])  # initialiser un liste à deviner

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

            print('\n')
    # -------- IA --------  # A compléter
        elif play == 'IA' or play == 'I':
            print('Prener place, la partie va commencer !!\n')

            test = False
            liste_to_guest = init(6, 4)  # initialiser un liste à deviner
            print(liste_to_guest)

            while not test:
                print('Essai n°', essai)

                essai += 1
                if essai == 11:
                    print("Nombre d'essais atteind\n PERDU !")
                    print("Il fallait trouver :", liste_to_guest)
                    break
                elif test == True:
                    print('FELICITATION !!')
                    # print(test)

            print('\n')
    # -------------------
        elif play == 'Non' or play == 'Not' or play == 'N':
            play = False
            print('Une prochaine fois!')
        else:
            play = True
            print('Veuiller dire oui ou non..')

    main = True

    return main