import time,pygame
from pygame.locals import *

def localtime():
    WHITE = (255, 255, 255)
    fontObjMini = pygame.font.Font('font/GameCube.ttf', 10)
    Localtime = time.asctime( time.localtime(time.time()))
    txtLocalTime = fontObjMini.render(Localtime, True, WHITE)
    return txtLocalTime