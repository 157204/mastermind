def verif_saisie(nbcouleur, longsuite):
    liste = []
    liste_saisie = input('Saisir une proposition :')

    if len(liste_saisie) != longsuite:
        return verif_saisie(nbcouleur, longsuite)

    for i in liste_saisie:
        try:
            temp = int(i)
        except ValueError:
            print("Veuillez rentrer que des nombres")
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
        for i, j in zip(liste_joueur, liste_jeu):  # petit probleme de quantité

            if i in liste_jeu:
                if i == j:
                    nb_e_perfect_place += 1
                else:
                    nb_e_bad_place += 1
            else:
                nb_e_wrong += 1

    print(nb_e_perfect_place, 'Bien placé (s)', nb_e_bad_place, 'Mal placé (s)', '\n')
    return False


