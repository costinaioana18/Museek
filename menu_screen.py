import pygame, sys
from pygame.locals import *


class Menu_screen():
    def __init__(self, app):
        self.app = app
        self.click= False

    def menu(self):
        running = True
        while running:
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            self.app.screen.fill((0, 0, 0))
            self.app.draw_text('menu', self.app.font, (255, 255, 255), self.app.screen, 20, 20)



            pygame.display.update()