import pygame, sys
from pygame.locals import *
from questions.choise_question import Choice_Question
from questions.gen_kno_question import Gen_Kno_Question
from screens.piano_tutorial_screen import Piano_tutorial_screen
from questions.piano_question import Piano_Question
import random

from useful_classes.prediction_algorithm import Prediction_Algorithm


class Recommended_screen():
    def __init__(self, app):
        self.checked=0
        self.app = app
        self.click= False
        self.q = Piano_Question(self.app, 0,"choice")
        self.piano_tutorial_screen=Piano_tutorial_screen(self.app)
        self.count=0
        self.started=0
        self.next_submit_icon=pygame.image.load('icons/play.jpg')



    def recommended(self):

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

            self.app.screen.fill((0, 0, 0))

            mx, my = pygame.mouse.get_pos()



            #self.app.draw_text('piano', self.app.font, (255, 255, 255), self.app.screen, 20, 20)




            if next_button.collidepoint((mx, my)):

                if click:
                    vector=[]
                    for topic in range(11):
                        vector.append([1, 0, 0, 0, 0, topic])
                    for topic in range(11):
                        vector.append([0, 1, 0, 0, 0, topic])
                    for topic in range(11):
                        vector.append([0, 0, 1, 0, 0, topic])
                    n = Prediction_Algorithm(self.app)  # antrenam un model cu datele pe care le avem despre progres
                    n.train_model()
                    n=n.get_biggest(vector)

                    if(self.started==0):
                        self.checked=1
                    self.started = 1
                    self.next_submit_icon = pygame.image.load('icons/submit_btn.jpg')
                    if self.checked==1:
                        #n=self.count%5
                        if(n==1):
                            self.q = Piano_Question(self.app, 0, "listen")
                        elif(n==2):
                            self.q = Piano_Question(self.app, 0, "read")
                        elif(n==3):
                            self.q = Piano_Question(self.app, 0, "choice")
                        else:
                            self.q=Gen_Kno_Question(self.app, 0)
                        self.q.set_next()
                        self.count+=1
                        self.checked=0
                    else:
                        self.q.check_answer()
                        self.checked=1
                        self.next_submit_icon = pygame.image.load('icons/play.jpg')
            else:
                if click:
                    received=self.q.receive_answer(mx, my)


            #pygame.draw.rect(self.app.screen, (255, 162, 193), next_button)
            self.app.screen.blit(self.next_submit_icon, (250, 450))
            self.app.screen.blit(self.app.bg, (20, 50))
            self.app.screen.blit(self.app.bg1, (700, 50))
            self.q.display()
            x=60
            y=40
            if(self.started==0):
                self.app.draw_text("Press 'continue' to start the test", self.app.font, (255, 255, 255), self.app.screen, 150+x, 120+y)


            pygame.display.update()