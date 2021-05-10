import pygame, sys
from pygame.locals import *


class My_account_screen():
    def __init__(self, app):
        self.app = app
        self.click= False

    def my_account(self):
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
            self.app.draw_text('Progress', self.app.font, self.app.color, self.app.screen, 330, 70)
            self.app.draw_text('Graduation', self.app.font, self.app.color, self.app.screen, 630, 70)
            self.app.draw_text('my account', self.app.font, self.app.color, self.app.screen, 20, 20)

            pygame.draw.rect(self.app.screen, (255, 162, 193), pygame.Rect(300, 150, 100, 30))
            pygame.draw.rect(self.app.screen, (255, 162, 193), pygame.Rect(300, 150, 200, 30), 1)
            self.app.draw_text('Piano', self.app.font, self.app.color, self.app.screen, 150, 145)
            self.app.draw_text('15 days', self.app.font, self.app.color, self.app.screen, 650, 145)

            pygame.draw.rect(self.app.screen, (255, 162, 193), pygame.Rect(300, 250, 34, 30))
            pygame.draw.rect(self.app.screen, (255, 162, 193), pygame.Rect(300, 250, 200, 30), 1)
            self.app.draw_text('Guitar', self.app.font, self.app.color, self.app.screen, 150, 245)
            self.app.draw_text('89 days', self.app.font, self.app.color, self.app.screen, 650, 245)

            pygame.draw.rect(self.app.screen, (255, 162, 193), pygame.Rect(300, 350, 180, 30))
            pygame.draw.rect(self.app.screen, (255, 162, 193), pygame.Rect(300, 350, 200, 30), 1)
            self.app.draw_text('General', self.app.font, self.app.color, self.app.screen, 150, 345)
            self.app.draw_text('3 days', self.app.font, self.app.color, self.app.screen, 650, 345)



            pygame.display.update()