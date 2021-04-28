import pygame,sys
from pygame.locals import *
from menu_screen import Menu_screen
from inputBox import InputBox
from database import Database

class Signup_screen():
    def __init__(self, app):
        self.app=app
        self.menu_screen = Menu_screen(self.app)
        self.click = False
        self.icon = pygame.image.load('icons/signup.jpg')
        self.play_icon = pygame.image.load('icons/play.jpg')
        self.u= None
        self.p=None
        self.n=None


    def insert_into_database(self,name,username,password):
        data={'username':'username', 'password':'password'}
        database_handler = Database(("mongodb+srv://museek:museek@museeku.nclk3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"))
        database_handler.database_init("appUsers")
        mycol = database_handler.set_collection("accounts")
        mycol.insert_one(data)
        print("inserted into database new user")


    def signup(self):
        running = True
        nickname_input = InputBox(250, 150, 400, 50, "nickname")
        username_input = InputBox(250, 250, 400, 50,"username")
        password_input = InputBox(250, 350, 400, 50,"password")
        input_boxes = [nickname_input,username_input, password_input]
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
                        if u!=None:
                            self.u=u
                        else:
                            self.u="dana"
                        p=password_input.handle_event(event)
                        if p:
                            self.p=p
                        n = nickname_input.handle_event(event)
                        if n:
                            self.n=n
                        print(n)
                        print(u)
                        print(p)
                        #if self.u and self.n and self.p:
                        #    self.insert_into_database(self.n,self.u,self.p)

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

                nickname_input.handle_event(event)
                username_input.handle_event(event)
                password_input.handle_event(event)
            for box in input_boxes:
                box.update()


            self.app.draw_text('signup', self.app.font, (255, 255, 255), self.app.screen, 20, 20)
            mx, my = pygame.mouse.get_pos()
            if menu_button.collidepoint((mx, my)):
                if click:
                    self.menu_screen.menu()
            self.app.screen.blit(self.icon, (250, 20))
            self.app.screen.blit(self.play_icon, (250, 450))
            for box in input_boxes:
                box.draw(self.app.screen)
            pygame.display.flip()


            #pygame.draw.rect(self.app.screen, (255, 162, 193), menu_button)
            pygame.display.update()