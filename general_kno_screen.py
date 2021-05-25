import pygame, sys
from pygame.locals import *
from gen_kno_question import Gen_Kno_Question

class General_kno_screen():
    def __init__(self, app):
        self.app = app
        self.click= False
        self.q = Gen_Kno_Question(self.app, 0)

    def general_kno(self):
        running = True
        next_button = pygame.Rect(250, 450, 400, 50)
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

            mx, my = pygame.mouse.get_pos()

            if next_button.collidepoint((mx, my)):
                if click:
                    self.q.check_answer()
                    self.q.set_next()
            else:
                if click:
                    received = self.q.receive_answer(mx, my)

            self.app.screen.fill((0, 0, 0))
            self.app.draw_text('general knowledge', self.app.font, (255, 255, 255), self.app.screen, 20, 20)
            pygame.draw.rect(self.app.screen, (255, 162, 193), next_button)
            self.app.screen.blit(self.app.bg, (20, 50))
            self.app.screen.blit(self.app.bg1, (700, 50))
            self.q.display()
            pygame.display.update()