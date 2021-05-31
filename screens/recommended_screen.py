import pygame, sys
from pygame.locals import *
from useful_classes.prediction_algorithm import *


class Recommended_screen():
    def __init__(self, app):
        self.app = app
        self.click= False

    def recommended(self):
        next_button = pygame.Rect(250, 450, 400, 50)
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
            self.app.draw_text('recommended', self.app.font, (255, 255, 255), self.app.screen, 20, 20)
            self.app.screen.blit(self.app.bg, (20, 50))
            self.app.screen.blit(self.app.bg1, (700, 50))

            mx, my = pygame.mouse.get_pos()
            if next_button.collidepoint((mx, my)):
                if click:
                    rec=Prediction_Algorithm(self.app)
                    rec.train_model()

            pygame.display.update()