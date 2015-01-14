import pygame, sys
from pygame.locals import *
from MastermindConsole import console
from MastermindGUI import gui


# def language():
#     lang = 'french'
#     if lang == 'french':
#         fLang = open('lang/french.cfg', 'r')
#         for ligne in fLang:
#             lang.append(ligne)
#
#     return lang

# Couleurs utilisées
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Initialisation de la fenêtre
pygame.init()
screen = pygame.display.set_mode((750, 800))
pygame.display.set_caption('Mastermind')

# Background
background = pygame.image.load('img/background.jpg')
screen.blit(background, (0, 0))

# Format - police
fontObjTitre = pygame.font.Font('font/GameCube.ttf', 48) # Format Titre
fontObj = pygame.font.Font('font/GameCube.ttf', 20) # Format standart
fontObjMini = pygame.font.Font('font/GameCube.ttf', 10) # Format standart

# Language par défaut
#lang = language()
#print(lang)

# Titre
texteTitre = fontObjTitre.render('Mastermind', True, WHITE)
texteRectTitre = texteTitre.get_rect()
texteRectTitre.topleft = (200, 300)
screen.blit(texteTitre, texteRectTitre)

# Interaction
texteStart = fontObj.render("Appuyer sur 'Entrer' pour continuer...", True, WHITE)
texteRectStart = texteStart.get_rect()
texteRectStart.topleft = (130, 650)
screen.blit(texteStart, texteRectStart)

step = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_RETURN and step == 0:
            pygame.mixer.music.load("sound/Illusion.ogg")
            pygame.mixer.music.play()

            print('coucou')
            screen.blit(background, (0, 0))
            texteRectTitre = texteRectTitre.move(0, -300)
            screen.blit(texteTitre, texteRectTitre)

            texteJouer = fontObj.render("Jouer", True, WHITE)
            texteRectJouer = texteJouer.get_rect()
            texteRectJouer.topright = (700, 400)
            screen.blit(texteJouer, texteRectJouer)

            texteGuide = fontObj.render("Guide", True, WHITE)
            texteRectGuide = texteGuide.get_rect()
            texteRectGuide.topright = (700, 450)
            screen.blit(texteGuide, texteRectGuide)

            texteOption = fontObj.render("Option", True, WHITE)
            texteRectOption = texteOption.get_rect()
            texteRectOption.topright = (700, 500)
            screen.blit(texteOption, texteRectOption)

            fichierVersion = open('version.txt', 'r')
            version = fichierVersion.read()
            texteVersion = fontObjMini.render(version, True, WHITE)
            texteRectVersion = texteVersion.get_rect()
            texteRectVersion.topleft = (10, 780)
            screen.blit(texteVersion, texteRectVersion)

            step += 1
        #if event.type ==KEYDOWN and event.key == K_RETURN and step == 1:
    pygame.display.update()
