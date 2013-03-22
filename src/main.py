import sys

import pygame
from pygame.locals import QUIT
from pygame import Surface

from views.PaneView import Pane

if __name__ == '__main__':
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((900, 800))
    main_surface = pygame.display.get_surface()
    pygame.display.set_caption('pytanque')
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                pygame.display.update()
    
    
    
    
    
    