import pygame, sys
from pygame.locals import *
from questions.choise_question import Choice_Question
from screens.piano_tutorial_screen import Piano_tutorial_screen
from questions.piano_question import Piano_Question
import random


class Piano_screen():
    def __init__(self, app):
        self.checked=0
        self.app = app
        self.click= False
        self.q = Piano_Question(self.app, 0,"choice")
        self.tutorial_icon = pygame.image.load('icons/tutorial.jpg')
        self.piano_tutorial_screen=Piano_tutorial_screen(self.app)
        self.count=0
        self.started=0



    def piano(self):

        running = True
        next_button = pygame.Rect(250, 450, 400, 50)
        piano_button = pygame.Rect(775, 25, 100, 100)
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

            mx, my = pygame.mouse.get_pos()
            if piano_button.collidepoint((mx, my)):
                self.app.draw_text('get help', self.app.font, (255, 255, 255), self.app.screen, 725, 140)
                if click:
                    print("piano_tutorial")
                    self.piano_tutorial_screen.piano_tutorial()



            #self.app.draw_text('piano', self.app.font, (255, 255, 255), self.app.screen, 20, 20)




            if next_button.collidepoint((mx, my)):

                if click:
                    if(self.started==0):
                        self.checked=1
                    self.started = 1
                    if self.checked==1:
                        n=self.count%3
                        if(n==1):
                            self.q = Piano_Question(self.app, 0, "listen")
                        elif(n==2):
                            self.q = Piano_Question(self.app, 0, "read")
                        else:
                            self.q = Piano_Question(self.app, 0, "choice")
                        self.q.set_next()
                        self.count+=1
                        self.checked=0
                    else:
                        self.q.check_answer()
                        self.checked=1
            else:
                if click:
                    received=self.q.receive_answer(mx, my)


            pygame.draw.rect(self.app.screen, (255, 162, 193), next_button)
            self.app.screen.blit(self.app.bg, (20, 50))
            self.app.screen.blit(self.app.bg1, (700, 50))
            self.app.screen.blit(self.tutorial_icon, (775, 25))
            self.q.display()
            if(self.started==0):
                self.app.draw_text('Press the button to start the test', self.app.font, (255, 255, 255), self.app.screen, 120, 120)

            pygame.display.update()