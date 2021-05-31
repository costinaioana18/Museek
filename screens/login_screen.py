import pygame,sys
from pygame.locals import *
from menu_screen import Menu_screen
from inputBox import InputBox
from database import Database
from encryption import *

class Login_screen():
    def __init__(self, app):
        self.app=app
        self.menu_screen = Menu_screen(self.app)
        self.click = False
        self.icon = pygame.image.load('icons/login.jpg')
        self.play_icon = pygame.image.load('icons/play.jpg')
        self.u = None
        self.p = None
        self.database_handler = self.app.database_handler
        self.database_handler.database_init("users")
        self.mycol = self.database_handler.set_collection("users")
        self.complete_fields = 0
        self.succes=None

    def database_check(self):
        print("hai verilor")
        q=self.database_handler.exists("username",self.u)
        if q:
            password = self.database_handler.get("username",self.u,"password")
            if password==self.p:
                self.succes = 1
                self.app.set_user(self.u)
            else:
                self.succes=0

        else:
            self.succes = 0

    def login(self):
        running = True
        username_input = InputBox(250, 200, 400, 50,"username")
        password_input = InputBox(250, 300, 400, 50,"password")
        input_boxes = [username_input, password_input]
        menu_button = pygame.Rect(250, 450, 400, 50)


        while running:
            click = False
            self.app.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        u=username_input.handle_event(event)
                        p=password_input.handle_event(event,True)
                        if u!=None:
                            self.u=u
                        if p:
                            self.p=encrypt(p)

                        print(self.u)
                        print(self.p)
                        if self.u and self.p:
                            self.complete_fields=1

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True


                username_input.handle_event(event)
                password_input.handle_event(event,True)
            for box in input_boxes:
                box.update()

            if (self.succes==0):
                self.app.draw_text('Wrong username or password', self.app.font, (255, 255, 255), self.app.screen, 20,
                                   500)
            #self.app.draw_text('login', self.app.font, (255, 255, 255), self.app.screen, 20, 20)
            mx, my = pygame.mouse.get_pos()
            if menu_button.collidepoint((mx, my)):
                if click and self.complete_fields:
                    self.database_check()
                    if(self.succes==1):
                        self.menu_screen.menu()
            self.app.screen.blit(self.icon, (250, 20))
            self.app.screen.blit(self.play_icon, (250, 450))
            for box in input_boxes:
                box.draw(self.app.screen)

            self.app.screen.blit(self.app.bg, (20, 50))
            self.app.screen.blit(self.app.bg1, (700, 50))
            pygame.display.flip()

            pygame.display.update()