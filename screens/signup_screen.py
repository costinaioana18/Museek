import pygame, sys
from pygame.locals import *
from screens.menu_screen import Menu_screen
from useful_classes.inputBox import InputBox
from datetime import date
from useful_classes.encryption import *


class Signup_screen():
    def __init__(self, app):
        self.app = app
        self.menu_screen = Menu_screen(self.app)
        self.click = False
        self.icon = pygame.image.load('icons/signup.jpg')
        self.play_icon = pygame.image.load('icons/play.jpg')
        self.play_icon_hov = pygame.image.load('icons/play_hov.jpg')
        self.u = None
        self.p = None
        self.n = None
        self.font = pygame.font.SysFont('inkfree', 22)
        self.database_handler = self.app.database_handler
        self.database_handler.database_init("users")
        self.mycol = self.database_handler.set_collection("users")
        self.complete_fields = 0
        self.already_exists = 0
        self.success = 0
        self.recovery_questions = ["your first dog", "your first crush", "your favourite flavour",
                                   "your favourite uncle", "your secret talent"]
        self.recovery_index = 0
        self.recovery_question = "your first dog"

    def insert_into_database(self, name, username, password):
        print("insert into database new user")
        q = self.database_handler.exists("username", self.u)
        if (q):
            print("the username already exists")
            self.already_exists = 1
        else:
            self.already_exists = 0
            self.database_handler.insert({"username": self.u, "password": self.p,
                                          "recovery_question": self.recovery_questions[self.recovery_index],
                                          "recovery_answer": self.n})
            self.create_user_data()
            self.success = 1
            self.app.set_user(self.u)

    def create_user_data(self):
        print("here")
        today = date.today()
        day = today.strftime('%d')
        month = today.strftime('%m')
        year = today.strftime('%y')
        self.database_handler.database_init("users")
        self.mycol = self.database_handler.set_collection("users_data")
        self.database_handler.insert(
            {"username": self.u, "piano_c_s": 0, "piano_c_f": 0, "piano_l_s": 0, "piano_l_f": 0, "piano_r_s": 0,
             "piano_r_f": 0, "chords_s": 0, "chords_f": 0, "gen_c_s": 0, "gen_c_f": 0, "day": int(day),
             "month": int(month), "year": int(year)})
        self.database_handler.database_init("users")
        self.mycol = self.database_handler.set_collection("users")
        print("here")

    def signup(self):
        running = True
        nickname_input = InputBox(250, 150, 400, 50, "your recovery answer")
        username_input = InputBox(250, 250, 400, 50, "username")
        password_input = InputBox(250, 350, 400, 50, "password")
        input_boxes = [nickname_input, username_input, password_input]
        menu_button = pygame.Rect(250, 450, 400, 50)
        next_button = pygame.Rect(660, 110, 30, 30)
        back_next_button = pygame.Rect(210, 110, 30, 30)
        next_icon = pygame.image.load("icons/little_next.jpg")
        back_next_icon = pygame.image.load("icons/little_backwards_next.jpg")

        while running:
            click = False
            self.app.screen.fill((0, 0, 0))
            for event in pygame.event.get(): #start: code borrowed and improved from source: https://www.youtube.com/watch?v=0RryiSjpJn0&t=386s
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        u = username_input.handle_event(event)
                        if u != None:
                            self.u = u
                        p = password_input.handle_event(event, True)
                        if p:
                            self.p = encrypt(p)
                        n = nickname_input.handle_event(event)
                        if n:
                            self.n = n
                        print(self.n)
                        print(self.u)
                        print(self.p)
                        if self.u and self.n and self.p:
                            self.complete_fields = 1

                if event.type == MOUSEBUTTONDOWN:   #end: code borrowed and improved from source: https://www.youtube.com/watch?v=0RryiSjpJn0&t=386s
                    if event.button == 1:
                        click = True

                nickname_input.handle_event(event)
                username_input.handle_event(event)
                password_input.handle_event(event, True)
            for box in input_boxes:
                box.update()

            # self.app.draw_text('signup', self.app.font, (255, 255, 255), self.app.screen, 20, 20)
            if (self.already_exists):
                self.app.draw_text('The username already exists', self.app.font, (255, 255, 255), self.app.screen, 20,
                                   500)

            mx, my = pygame.mouse.get_pos()

            if next_button.collidepoint((mx, my)):
                if click:
                    if self.recovery_index == 4:
                        self.recovery_index = 0
                    else:
                        self.recovery_index += 1
                    self.recovery_question = self.recovery_questions[self.recovery_index]

            if back_next_button.collidepoint((mx, my)):
                if click:
                    if self.recovery_index == 0:
                        self.recovery_index = 4
                    else:
                        self.recovery_index -= 1
                    self.recovery_question = self.recovery_questions[self.recovery_index]

            if menu_button.collidepoint((mx, my)):
                self.app.screen.blit(self.play_icon_hov, (250, 450))
                if click and self.complete_fields:
                    print("insert")
                    self.insert_into_database(self.n, self.u, self.p)
                    if self.success:
                        self.menu_screen.menu()
            else:
                self.app.screen.blit(self.play_icon, (250, 450))
            self.app.screen.blit(self.icon, (250, 20))

            nickname_input.draw(self.app.screen)
            for box in input_boxes:
                if box != nickname_input:
                    box.draw(self.app.screen)

            self.app.screen.blit(self.app.bg, (20, 50))
            self.app.screen.blit(self.app.bg1, (700, 50))
            self.app.screen.blit(next_icon, (660, 110))
            self.app.screen.blit(back_next_icon, (210, 110))
            self.app.draw_text("recovery question: " + self.recovery_question, self.font, self.app.color,
                               self.app.screen,
                               250, 110)

            self.app.screen.blit(pygame.image.load('icons/mouse.png'), (mx - 25, my - 25))
            pygame.display.flip()
            # pygame.draw.rect(self.app.screen, (255, 162, 193), menu_button)
            pygame.display.update()
