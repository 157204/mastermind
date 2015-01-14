import pygame, sys
from pygame.locals import *

def gui(main):
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
    fontObj = pygame.font.Font('font/GameCube.ttf', 48)
    texteSurface = fontObj.render('Mastermind', True, WHITE)
    texteRect = texteSurface.get_rect()
    texteRect.topleft = (200, 300)
    maSurface.blit(texteSurface, texteRect)
    #pygame.draw.rect(maSurface, RED, (10, 100, 200, 100))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    main = True

    return main