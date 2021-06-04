import pygame, sys
from pygame.locals import *
from screens.piano_screen import Piano_screen
from screens.general_kno_screen import General_kno_screen
from screens.recommended_screen import Recommended_screen
from screens.my_account_screen import My_account_screen
from screens.piano_chords_screen import Piano_chords_screen
from screens.feedback_screen import Feedback_screen

class Menu_screen():
    def __init__(self, app):
        self.app = app
        self.click= False
        self.piano_screen = Piano_screen(self.app)
        self.chords_screen=Piano_chords_screen(self.app)
        self.general_kno_screen = General_kno_screen(self.app)
        self.recommended_screen = Recommended_screen(self.app)
        self.my_account_screen = My_account_screen(self.app)
        self.piano_icon = pygame.image.load('icons/piano.jpg')
        self.guitar_icon = pygame.image.load('icons/guitar.jpg')
        self.recommended_icon = pygame.image.load('icons/recommended.jpg')
        self.general_kno_icon = pygame.image.load('icons/general_kno.jpg')
        self.my_account_icon = pygame.image.load('icons/my_account.jpg')
        self.feedback_screen=Feedback_screen(self.app)

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
            self.app.draw_text(self.app.current_user, self.app.font, (255, 255, 255), self.app.screen, 20, 20)

            mx, my = pygame.mouse.get_pos()
            piano_button = pygame.Rect(250, 150, 400, 50)
            guitar_button = pygame.Rect(250, 250, 400, 50)
            recommended_button = pygame.Rect(250, 350, 400, 50)
            general_kno_button = pygame.Rect(250, 450, 400, 50)
            my_account_button = pygame.Rect(400, 525, 100, 25)
            feedback_button=pygame.Rect(400, 575, 100, 25)

            if piano_button.collidepoint((mx, my)):
                if click:
                    self.piano_screen.piano()
            if guitar_button.collidepoint((mx, my)):
                if click:
                    self.chords_screen.play_the_piano()
            if recommended_button.collidepoint((mx, my)):
                if click:
                    self.recommended_screen.recommended()
            if general_kno_button.collidepoint((mx, my)):
                if click:
                    self.general_kno_screen.general_kno()
            if my_account_button.collidepoint((mx, my)):
                if click:
                    self.my_account_screen.get_progress()
                    self.my_account_screen.graduation_expect()
                    self.my_account_screen.chord_graduation_expect()
                    print("here")
                    self.my_account_screen.my_account()
            if feedback_button.collidepoint((mx, my)):
                if click:
                    self.feedback_screen.get_from_database()
                    self.feedback_screen.feedback_screen()


            self.app.screen.blit(self.piano_icon, (250, 150))
            self.app.screen.blit(self.guitar_icon, (250, 250))
            self.app.screen.blit(self.recommended_icon, (250, 350))
            self.app.screen.blit(self.general_kno_icon, (250, 450))
            self.app.screen.blit(self.my_account_icon, (400, 525))
            self.app.screen.blit(self.my_account_icon, (400, 575))
            self.app.screen.blit(self.app.bg, (20, 50))
            self.app.screen.blit(self.app.bg1, (700, 50))
            # pygame.draw.rect(self.app.screen, (255, 162, 193), piano_button)
            # pygame.draw.rect(self.app.screen, (255, 162, 193), guitar_button)
            # pygame.draw.rect(self.app.screen, (255, 162, 193), recommended_button)
            # pygame.draw.rect(self.app.screen, (255, 162, 193), general_kno_button)
            #pygame.draw.rect(self.app.screen, (255, 162, 193), my_account_button)



            pygame.display.update()