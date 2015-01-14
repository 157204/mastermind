# from random import randrange
# def verif_saisie(nbcouleur, longsuite):
# liste = []
# liste_saisie = input('Saisir une proposition :')
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

# def changelettre(lettre):
#     x = ord(lettre)
#     if x >= 65 and x <= 90:  # to miniscule
#         x += 32
#     elif x >= 97 and x <= 122:
#         x -= 32
#
#     x = chr(x)
#     print(x)
#
#     return x
#
#
# changelettre(input('lettre : '))

import pygame, sys
from pygame.locals import *

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

pygame.init()
maSurface = pygame.display.set_mode((750, 800))
pygame.display.set_caption('Hello supinfo')
maSurface.fill(BLUE)
monImage = pygame.image.load('img/base.jpg')
maSurface.blit(monImage, (0, 0))
fontObj = pygame.font.Font('GameCube.ttf', 48)
texteSurface = fontObj.render('Mastermind')
#pygame.draw.rect(maSurface, RED, (10, 100, 200, 100))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

