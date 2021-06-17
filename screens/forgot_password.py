import pygame, sys
from pygame.locals import *
from screens.menu_screen import Menu_screen
from useful_classes.inputBox import InputBox
from useful_classes.encryption import *


class Forgot_password_screen():
    def __init__(self, app):
        self.play_icon = pygame.image.load('icons/play.jpg')
        self.app = app
        self.click = False
        self.font = pygame.font.SysFont('inkfree', 22)
        self.u = None
        self.p = None
        self.database_handler = self.app.database_handler
        self.database_handler.database_init("users")
        self.mycol = self.database_handler.set_collection("users")
        self.password = "None"
        self.complete_fields = 0
        self.succes = None
        self.recovery_questions = ["your first dog", "your first crush", "your favourite flavour",
                                   "your favourite uncle", "your secret talent"]

        self.recovery_index = 0
        self.recovery_question = "your first dog"

    def database_check(self):
        print("hai verilor")
        q = self.database_handler.exists("username", self.u)
        if q:
            recovery_question = self.database_handler.get("username", self.u, "recovery_question")
            recovery_answer = self.database_handler.get("username", self.u, "recovery_answer")
            self.password = self.database_handler.get("username", self.u, "password")
            self.password = decrypt(self.password)
            if recovery_answer == self.p and recovery_question == self.recovery_question:
                self.succes = 1
                self.app.set_user(self.u)
            else:
                self.succes = 0

        else:
            self.succes = 0

    def forgot_password(self):
        running = True
        username_input = InputBox(250, 180, 400, 50, "username")
        password_input = InputBox(250, 300, 400, 50, "your recovery answer")
        input_boxes = [username_input, password_input]
        menu_button = pygame.Rect(250, 450, 400, 50)
        # next_button = pygame.Rect(500, 100, 50, 50)
        # next_icon = pygame.image.load("icons/next.jpg")
        next_button = pygame.Rect(660, 260, 30, 30)
        back_next_button = pygame.Rect(210, 260, 30, 30)
        next_icon = pygame.image.load("icons/little_next.jpg")
        back_next_icon = pygame.image.load("icons/little_backwards_next.jpg")

        while running:
            click = False
            self.app.screen.fill((0, 0, 0)) #beginning
            for event in pygame.event.get(): #code borrowed and improved from source: https://www.youtube.com/watch?v=0RryiSjpJn0&t=386s
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        u = username_input.handle_event(event)
                        p = password_input.handle_event(event)  #code borrowed and improved from source: https://www.youtube.com/watch?v=0RryiSjpJn0&t=386s
                        if u != None:                           #end
                            self.u = u
                        if p:
                            self.p = p

                        print(self.u)
                        print(self.p)
                        if self.u and self.p:
                            self.complete_fields = 1

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

                username_input.handle_event(event)
                password_input.handle_event(event)
            for box in input_boxes:
                box.update()

            if (self.succes == 0):
                self.app.draw_text('Wrong username or password', self.app.font, (255, 255, 255), self.app.screen, 20,
                                   500)
            # self.app.draw_text('login', self.app.font, (255, 255, 255), self.app.screen, 20, 20)
            mx, my = pygame.mouse.get_pos()
            if menu_button.collidepoint((mx, my)):
                if click and self.complete_fields:
                    self.database_check()
                    if (self.succes == 1):
                        # elf.menu_screen.menu()
                        print(self.password)
                        # recovery_question = self.database_handler.get("username", self.u, "recovery_question")

            username_input.draw(self.app.screen)
            password_input.draw(self.app.screen)

            if next_button.collidepoint((mx, my)):
                if click:
                    if self.recovery_index == 4:
                        self.recovery_index = 0
                    else:
                        self.recovery_index += 1
                    self.recovery_question = self.recovery_questions[self.recovery_index]
                    print("click")

            if back_next_button.collidepoint((mx, my)):
                if click:
                    if self.recovery_index == 0:
                        self.recovery_index = 4
                    else:
                        self.recovery_index -= 1
                    self.recovery_question = self.recovery_questions[self.recovery_index]
                    print("click")

            if (self.succes == 1):
                self.app.draw_text("Your password is: " + self.password, self.app.font, (255, 255, 255),
                                   self.app.screen, 120,
                                   500)

            # self.app.screen.blit(next_icon, (500, 100))
            self.app.screen.blit(self.play_icon, (250, 450))
            self.app.draw_text("recovery question: " + self.recovery_question, self.font, self.app.color,
                               self.app.screen, 250,
                               260)
            self.app.draw_text("Account recovery", pygame.font.SysFont('inkfree', 42), self.app.color,
                               self.app.screen, 300,
                               60)
            self.app.screen.blit(self.app.bg, (20, 50))
            self.app.screen.blit(self.app.bg1, (700, 50))
            self.app.screen.blit(next_icon, (660, 260))
            self.app.screen.blit(back_next_icon, (210, 260))
            self.app.screen.blit(pygame.image.load('icons/mouse.png'), (mx - 25, my - 25))

            pygame.display.flip()

            pygame.display.update()
