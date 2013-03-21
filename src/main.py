import sys

import pygame
from pygame.locals import QUIT

if __name__ == '__main__':
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((900, 800))
    pygame.display.set_caption('pytanque')
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                pygame.display.update()
    
    
    
    
    
    