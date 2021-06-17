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
        self.click = False
        self.piano_screen = Piano_screen(self.app)
        self.chords_screen = Piano_chords_screen(self.app)
        self.general_kno_screen = General_kno_screen(self.app)
        self.recommended_screen = Recommended_screen(self.app)
        self.my_account_screen = My_account_screen(self.app)
        self.piano_icon = pygame.image.load('icons/piano.jpg')
        self.guitar_icon = pygame.image.load('icons/guitar.jpg')
        self.recommended_icon = pygame.image.load('icons/recommended.jpg')
        self.general_kno_icon = pygame.image.load('icons/general_kno.jpg')
        self.my_account_icon = pygame.image.load('icons/my_account.jpg')
        self.piano_icon_hov = pygame.image.load('icons/piano_hov.jpg')
        self.guitar_icon_hov = pygame.image.load('icons/guitar_hov.jpg')
        self.recommended_icon_hov = pygame.image.load('icons/recommended_hov.jpg')
        self.general_kno_icon_hov = pygame.image.load('icons/general_kno_hov.jpg')
        self.my_account_icon = pygame.image.load('icons/my_account.jpg')
        self.locked_chord_icon = pygame.image.load('icons/locked_chord.jpg')
        self.feedback_screen = Feedback_screen(self.app)
        self.user_score = 0

    def get_user_score(self):
        if self.app.current_user:
            database_handler = self.app.database_handler
            database_handler.database_init("users")
            mycol = database_handler.set_collection("users_data")
            user = database_handler.exists("username", self.app.current_user)
            user_score = 0
            if user:
                user_score += database_handler.get("username", self.app.current_user, "piano_c_s")
                user_score += database_handler.get("username", self.app.current_user, "piano_l_s")
                user_score += database_handler.get("username", self.app.current_user, "piano_r_s")
            self.user_score = user_score
            return user_score

    def menu(self):

        running = True
        while running:
            click = False

            for event in pygame.event.get(): #code borrowed and improved from source: https://www.youtube.com/watch?v=0RryiSjpJn0&t=386s
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            self.app.screen.fill((0, 0, 0))         #code borrowed and improved from source: https://www.youtube.com/watch?v=0RryiSjpJn0&t=386s
                                                    #end
            if click:
                self.get_user_score()
            # self.app.draw_text( "Nice to C you, "+self.app.current_user, self.app.font, (255, 255, 255), self.app.screen, 20, 10)

            mx, my = pygame.mouse.get_pos()
            piano_button = pygame.Rect(250, 150, 400, 50)
            guitar_button = pygame.Rect(250, 250, 400, 50)
            recommended_button = pygame.Rect(250, 350, 400, 50)
            general_kno_button = pygame.Rect(250, 450, 400, 50)
            my_account_button = pygame.Rect(400, 525, 100, 25)
            feedback_button = pygame.Rect(400, 555, 100, 25)

            if piano_button.collidepoint((mx, my)):
                self.app.screen.blit(self.piano_icon_hov, (250, 150))
                if click:
                    self.piano_screen.piano()
            else:
                self.app.screen.blit(self.piano_icon, (250, 150))

            if guitar_button.collidepoint((mx, my)):
                if click:
                    if self.get_user_score() > 10:
                        self.chords_screen.play_the_piano()

            if recommended_button.collidepoint((mx, my)):
                self.app.screen.blit(self.recommended_icon_hov, (250, 350))
                if click:
                    self.recommended_screen.recommended()
            else:
                self.app.screen.blit(self.recommended_icon, (250, 350))

            if general_kno_button.collidepoint((mx, my)):
                self.app.screen.blit(self.general_kno_icon_hov, (250, 450))
                if click:
                    self.general_kno_screen.general_kno()
            else:
                self.app.screen.blit(self.general_kno_icon, (250, 450))

            if my_account_button.collidepoint((mx, my)):
                if click:
                    self.my_account_screen.get_progress()
                    self.my_account_screen.graduation_expect()
                    self.my_account_screen.gn_graduation_expect()
                    self.my_account_screen.chord_graduation_expect()
                    print("here")
                    self.my_account_screen.my_account()
                else:
                    self.app.draw_text("My account", pygame.font.SysFont('inkfree', 16, bold=True), (255, 168, 176),
                                       self.app.screen,
                                       408, 525)

            else:
                self.app.draw_text("My account", pygame.font.SysFont('inkfree', 16), (255, 168, 176),
                                   self.app.screen,
                                   408, 525)

            if feedback_button.collidepoint((mx, my)):

                self.app.draw_text("Feedback", pygame.font.SysFont('inkfree', 16, bold=True), (255, 168, 176),
                                   self.app.screen,
                                   413, 555)
                if click:
                    self.feedback_screen.get_from_database()
                    self.feedback_screen.feedback_screen()
            else:

                self.app.draw_text("Feedback", pygame.font.SysFont('inkfree', 16), (255, 168, 176), self.app.screen,
                                   413, 555)

            if self.user_score < 11:
                self.app.screen.blit(self.locked_chord_icon, (250, 250))
            else:
                if guitar_button.collidepoint((mx, my)):
                    self.app.screen.blit(self.guitar_icon_hov, (250, 250))
                else:
                    self.app.screen.blit(self.guitar_icon, (250, 250))

            self.app.screen.blit(self.app.bg, (20, 50))
            self.app.screen.blit(self.app.bg1, (700, 50))

            self.app.screen.blit(self.app.logo, (250, 20))

            self.app.screen.blit(pygame.image.load('icons/mouse.png'), (mx - 25, my - 25))

            pygame.display.update()
