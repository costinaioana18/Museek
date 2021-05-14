import pygame, sys
from pygame.locals import *
from choise_question import Choice_Question
from piano_tutorial_screen import Piano_tutorial_screen
from piano_question import Piano_Question

class Piano_screen():
    def __init__(self, app):
        self.app = app
        self.click= False
        self.q = Piano_Question(self.app, 0,"choice")
        self.tutorial_icon = pygame.image.load('icons/tutorial.jpg')
        self.piano_tutorial_screen=Piano_tutorial_screen(self.app)


    def piano(self):
        running = True
        next_button = pygame.Rect(250, 450, 400, 50)
        piano_button = pygame.Rect(725, 25, 100, 100)
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
            if piano_button.collidepoint((mx, my)):
                if click:
                    print("piano_tutorial")

                    self.piano_tutorial_screen.piano_tutorial()

            self.app.screen.fill((0, 0, 0))
            self.app.draw_text('piano', self.app.font, (255, 255, 255), self.app.screen, 20, 20)




            mx, my = pygame.mouse.get_pos()

            if next_button.collidepoint((mx, my)):
                if click:
                    self.q.check_answer()
                    self.q = Piano_Question(self.app, 0, "read")
                    #self.q.set_next()
            else:
                if click:
                    received=self.q.receive_answer(mx, my)


            pygame.draw.rect(self.app.screen, (255, 162, 193), next_button)
            self.app.screen.blit(self.tutorial_icon, (775, 25))
            self.q.display()
            pygame.display.update()