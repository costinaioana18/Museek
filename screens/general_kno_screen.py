import pygame, sys
from pygame.locals import *
from questions.choise_question import Choice_Question
from questions.gen_kno_question import Gen_Kno_Question
from screens.piano_tutorial_screen import Piano_tutorial_screen
from questions.piano_question import Piano_Question
import random


class General_kno_screen():
    def __init__(self, app):
        self.checked = 0
        self.app = app
        self.click = False
        self.q = Piano_Question(self.app, 0, "choice")
        self.tutorial_icon = pygame.image.load('icons/tutorial.jpg')
        self.piano_tutorial_screen = Piano_tutorial_screen(self.app)
        self.started = 0
        self.next_submit_icon = pygame.image.load('icons/play.jpg')
        self.case = 0

    def hover_photo(self):
        if self.case == 1:
            self.next_submit_icon = pygame.image.load('icons/submit_btn_hov.jpg')
        else:
            self.next_submit_icon = pygame.image.load('icons/play_hov.jpg')

    def unhover_photo(self):
        if self.case == 1:
            self.next_submit_icon = pygame.image.load('icons/submit_btn.jpg')
        else:
            self.next_submit_icon = pygame.image.load('icons/play.jpg')

    def general_kno(self):

        running = True
        next_button = pygame.Rect(250, 450, 400, 50)
        while running:
            click = False
            for event in pygame.event.get():  #start
                if event.type == QUIT:          #code borrowed and improved from source: https://www.youtube.com/watch?v=0RryiSjpJn0&t=386s
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True                #code borrowed and improved from source: https://www.youtube.com/watch?v=0RryiSjpJn0&t=386s
                                                    #end
            self.app.screen.fill((0, 0, 0))

            mx, my = pygame.mouse.get_pos()

            if next_button.collidepoint((mx, my)):
                self.hover_photo()
                if click:
                    if (self.started == 0):
                        self.checked = 1
                    self.started = 1
                    self.next_submit_icon = pygame.image.load('icons/submit_btn.jpg')
                    if self.checked == 1:
                        self.q = Gen_Kno_Question(self.app, 0)
                        self.q.set_next()
                        self.checked = 0
                    else:
                        self.q.check_answer()
                        self.checked = 1
                        self.next_submit_icon = pygame.image.load('icons/play.jpg')
            else:
                self.unhover_photo()
                if click:
                    received = self.q.receive_answer(mx, my)

            self.app.screen.blit(self.next_submit_icon, (250, 450))
            self.app.screen.blit(self.app.bg, (20, 50))
            self.app.screen.blit(self.app.bg1, (700, 50))
            self.q.display()
            x = 60
            y = 40
            if (self.started == 0):
                self.app.draw_text("Press 'continue' to start the test", self.app.font, (255, 255, 255),
                                   self.app.screen, 150 + x, 120 + y)

            self.app.screen.blit(pygame.image.load('icons/mouse.png'), (mx - 25, my - 25))

            pygame.display.update()
