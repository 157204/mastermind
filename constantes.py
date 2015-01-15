import pygame
#from pygame.locals import *

#Version du jeu
fichierVersion = open('version.txt', 'r')
version = fichierVersion.read()
fichierVersion.close()

#Couleur utilisé
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (  0, 0, 0)

#Initialisation de la fenêtre
window_width = 750
window_height = 800

#Personalisation de la fenêtre
title_window = 'Mastermind'
img_icon = 'img/dk_droite.png'

#Liste des images du jeu
img_background = 'img/background.jpg'

#Liste des musiqies/sons
music_global = 'sound/Illusion.ogg'

#Font
font = 'font/GameCube.ttf'

#Format - police
#fontObjTitre = pygame.font.Font(font, 48)  #Taille 48 - titre
#fontObj = pygame.font.Font(font, 20)  #Taille 20 - standart
#fontObjMini = pygame.font.Font(font, 10)  #Taille 10 - minuscule