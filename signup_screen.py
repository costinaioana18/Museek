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
        self.database_handler = Database(
            "mongodb+srv://test:test@cluster0.6borp.mongodb.net/test?retryWrites=true&w=majority")
        self.database_handler.database_init("users")
        self.mycol = self.database_handler.set_collection("users")
        self.complete_fields=0


    def insert_into_database(self,name,username,password):
        print("insert into database new user")
        q=self.database_handler.exists("username",self.u)
        if(q):
            print("the username already exists")
        else:
            self.database_handler.insert({"name":self.n,"username":self.u,"password":self.p})


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
                        p=password_input.handle_event(event,True)
                        if p:
                            self.p=p
                        n = nickname_input.handle_event(event)
                        if n:
                            self.n=n
                        print(self.n)
                        print(self.u)
                        print(self.p)
                        if self.u and self.n and self.p:
                            self.complete_fields=1

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

                nickname_input.handle_event(event)
                username_input.handle_event(event)
                password_input.handle_event(event,True)
            for box in input_boxes:
                box.update()


            self.app.draw_text('signup', self.app.font, (255, 255, 255), self.app.screen, 20, 20)
            mx, my = pygame.mouse.get_pos()
            if menu_button.collidepoint((mx, my)):
                if click and self.complete_fields:
                    print("insert")
                    self.insert_into_database(self.n, self.u, self.p)
                    self.menu_screen.menu()
            self.app.screen.blit(self.icon, (250, 20))
            self.app.screen.blit(self.play_icon, (250, 450))
            for box in input_boxes:
                box.draw(self.app.screen)
            pygame.display.flip()


            #pygame.draw.rect(self.app.screen, (255, 162, 193), menu_button)
            pygame.display.update()