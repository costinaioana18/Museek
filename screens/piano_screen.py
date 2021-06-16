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
        self.case=0
        self.next_submit_icon=pygame.image.load('icons/play.jpg')

    def hover_photo(self):
        if self.case==1:
            self.next_submit_icon = pygame.image.load('icons/submit_btn_hov.jpg')
        else:
            self.next_submit_icon = pygame.image.load('icons/play_hov.jpg')

    def unhover_photo(self):
        if self.case==1:
            self.next_submit_icon = pygame.image.load('icons/submit_btn.jpg')
        else:
            self.next_submit_icon = pygame.image.load('icons/play.jpg')

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
                self.app.draw_text('explore & learn', self.app.font, (255, 255, 255), self.app.screen, 500, 40)
                if click:
                    print("piano_tutorial")
                    self.piano_tutorial_screen.piano_tutorial()



            #self.app.draw_text('piano', self.app.font, (255, 255, 255), self.app.screen, 20, 20)




            if next_button.collidepoint((mx, my)):
                self.hover_photo()
                if click:
                    if(self.started==0):
                        self.checked=1
                    self.started = 1
                    self.next_submit_icon = pygame.image.load('icons/submit_btn.jpg')
                    self.case=1
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
                        self.next_submit_icon = pygame.image.load('icons/play.jpg')
                        self.case=0
            else:
                self.unhover_photo()
                if click:
                    received=self.q.receive_answer(mx, my)


            #pygame.draw.rect(self.app.screen, (255, 162, 193), next_button)
            self.app.screen.blit(self.next_submit_icon, (250, 450))
            self.app.screen.blit(self.app.bg, (20, 50))
            self.app.screen.blit(self.app.bg1, (700, 50))
            self.app.screen.blit(self.tutorial_icon, (775, 25))
            self.q.display()
            x=60
            y=40
            if(self.started==0):
                self.app.draw_text("Press 'continue' to start the test", self.app.font, (255, 255, 255), self.app.screen, 150+x, 120+y)
                self.app.draw_text(
                    "Press the hint icon to explore",
                    self.app.font, (255, 255, 255), self.app.screen, 150+x, 160+y)
                self.app.draw_text(
                    "the piano's simulator ",
                    self.app.font, (255, 255, 255), self.app.screen, 326+x, 200+y)
                self.app.draw_text(
                    "& the beginner's manual",
                    self.app.font, (255, 255, 255), self.app.screen, 280+x, 240+y)
            self.app.screen.blit(pygame.image.load('icons/mouse.png'), (mx - 25, my - 25))

            pygame.display.update()