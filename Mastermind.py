from pygame.locals import *
#from classes import *
from constantes import *
from MastermindConsole import *
from MastermindGUI import *

pygame.init()

#Ouverture de la fenêtre Pygame
screen = pygame.display.set_mode((window_width, window_height))

#Icone
# icon = pygame.image.load(img_icon).convert_alpha()
# pygame.display.set_icon(icon)

#Titre
pygame.display.set_caption(title_window)

#Format - police
fontObjTitre = pygame.font.Font('font/GameCube.ttf', 48)  # Format Titre
fontObj = pygame.font.Font('font/GameCube.ttf', 20)  # Format standart
fontObjMini = pygame.font.Font('font/GameCube.ttf', 10)  # Format standart

#Musique/Sons
pygame.mixer.music.load(music_global)

#Texte
txtTitre = fontObjTitre.render('Mastermind', True, WHITE)
txtStart = fontObj.render("Appuyer sur 'Entrer' pour continuer...", True, WHITE)
txtJouer = fontObj.render("Jouer", True, WHITE)
txtModJouer = fontObj.render("Jouer", True, WHITE)
txtModJouerC = fontObj.render("Jouer avec la console", True, WHITE)
txtGuide = fontObj.render("Guide", True, WHITE)
txtOption = fontObj.render("Option", True, WHITE)
txtQuitter = fontObj.render("Quitter", True, WHITE)
txtVersion = fontObjMini.render(version, True, WHITE)

#BOUCLE PRINCIPALE
continuer = 1
continuer_intro = 1
continuer_accueil = 0
continuer_jeu = 0
titre_intro = 1

box_jouer = 0

while continuer:

    #Chargement et affichage de l'écran d'acccueil
    accueil = pygame.image.load(img_background)
    screen.blit(accueil, (0, 0))

    if titre_intro == 0:
        RectTitre = txtTitre.get_rect()
        RectTitre.topleft = (200, 10)
        screen.blit(txtTitre, RectTitre)
        continuer_accueil = 1  #On Charge l'accueil

    #BOUCLE INTRO
    while continuer_intro:

        #limitation de la boucle
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer, continuer_intro, continuer_accueil, continuer_jeu = 0, 0, 0, 0
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    continuer_intro = 0  #On quitte l'intro
                    titre_intro = 0
                    pygame.mixer.music.play() #On Charge la musique

        #Titre
        RectTitre = txtTitre.get_rect()
        RectTitre.topleft = (200, 300)
        screen.blit(txtTitre, RectTitre)

        RectStart = txtStart.get_rect()
        RectStart.topleft = (130, 650)
        screen.blit(txtStart, RectStart)

        #Rafraichissement
        pygame.display.flip()

    #BOUCLE D'ACCUEIL
    while continuer_accueil:

        #limitation de la boucle
        pygame.time.Clock().tick(30)

        #Bouton Jouer
        RectJouer = txtJouer.get_rect()
        RectJouer.topright = (700, 400)
        screen.blit(txtJouer, RectJouer)

        #Bouton Guide
        RectGuide = txtGuide.get_rect()
        RectGuide.topright = (700, 450)
        screen.blit(txtGuide, RectGuide)

        #Bouton Option
        RectOption = txtOption.get_rect()
        RectOption.topright = (700, 500)
        screen.blit(txtOption, RectOption)

        #Bouton Quitter
        RectQuitter = txtOption.get_rect()
        RectQuitter.topright = (700, 550)
        screen.blit(txtQuitter, RectQuitter)

        #Version
        RectVersion = txtVersion.get_rect()
        RectVersion.topleft = (10, 780)
        screen.blit(txtVersion, RectVersion)

        for event in pygame.event.get():

            #Si on quitte, on met les variables de boucle à 0
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer, continuer_accueil, continuer_jeu = 0, 0, 0

            # choix menu
            elif event.type == MOUSEBUTTONUP:
                x, y = event.pos
                if RectQuitter.collidepoint((x, y)):
                    continuer, continuer_accueil = 0, 0
                if RectJouer.collidepoint((x, y)):

                    box_jouer = 1
                    continuer_accueil = 0

        #Rafraichissement
        pygame.display.flip()
    # ---------condition de l'accueil--------
    while box_jouer:

        # il faudra mettre un cadre et un bouton charger une partie
        #Mode normal
        RectModJouer = txtModJouer.get_rect()
        RectModJouer.topright = (600, 500)
        screen.blit(txtModJouer, RectModJouer)
        #Mode Console
        RectModJouerC = txtModJouerC.get_rect()
        RectModJouerC.topright = (600, 600)
        screen.blit(txtModJouerC, RectModJouerC)

        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
                box_jouer = 0
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    box_jouer = 0
            elif event.type == MOUSEBUTTONUP:
                x, y = event.pos
                if RectModJouer.collidepoint((x, y)):
                    mastermindgui(False)
                if RectModJouerC.collidepoint((x, y)):
                    mastermindconsole(False)


        #Rafraichissement
        pygame.display.flip()


    #BOUCLE JEU
    while continuer_jeu:

        #limitation de la boucle
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            #On ferme tout
            if event.type == QUIT:
                continuer_jeu = 0
                continuer = 0
            #On ferme la partie jeu seulement
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continuer_jeu = 0

        #Rafraichissement
        pygame.display.flip()

    #Rafraichissement
    pygame.display.flip()