import pygame,sys
from pygame.locals import *
from useful_classes.inputBox import InputBox
from useful_classes.encryption import *
#from screens.forgot_password import Forgot_password_screen

class Feedback_screen():
    def __init__(self, app):
        self.app=app
        self.click = False
        self.rate0=pygame.image.load('icons/filled_note.jpg')
        self.rate1 = pygame.image.load('icons/empty_note.jpg')
        self.current_collide_rate=-1
        self.play_icon = pygame.image.load('icons/send_icon.jpg')
        self.font=pygame.font.SysFont('inkfree', 20)
        self.u = None
        self.database_handler = self.app.database_handler
        self.database_handler.database_init("feedback")
        self.mycol = self.database_handler.set_collection("feedbacks")
        self.feedbacks=["Amazing","Wonderful","Fun and useful"]
        self.setted_rating=-1
        self.complete_fields = 0
        self.succes=None
        self.avg_rating=5.00
        self.rating_buttons=[]
        x=350
        y=50
        for i in range(5):
            self.rating_buttons.append(pygame.Rect(x+i*35,y,35,60))

    def get_rating_fromdb(self):
        self.database_handler.database_init("feedback")
        self.mycol = self.database_handler.set_collection("ratings")
        ratings=self.mycol.find()
        sum=0.0
        count=0
        for rate in ratings:
            sum+=rate["rating"]
            count+=1
        self.avg_rating=sum/count

    def rate(self):

        self.database_handler.database_init("feedback")
        self.mycol = self.database_handler.set_collection("ratings")
        q = self.database_handler.exists("username", self.app.current_user)
        if q:
            print("da")
            self.mycol.update(
                {"username": self.app.current_user}, {"username": self.app.current_user,"rating": self.setted_rating+1})
        else:
            self.database_handler.insert(
                {"username": self.app.current_user, "rating": self.setted_rating + 1})
        self.get_rating_fromdb()

    def database_check(self):
        print("hai verilor")
        self.database_handler.database_init("feedback")
        self.mycol = self.database_handler.set_collection("feedbacks")
        self.database_handler.insert(
            {"username": self.u, "feedback":self.u})

    def get_from_database(self):
        self.database_handler.database_init("feedback")
        self.mycol = self.database_handler.set_collection("feedbacks")
        feedbacks = self.mycol.find()
        self.feedbacks[0]=feedbacks[0]["feedback"]
        self.get_rating_fromdb()


    def feedback_screen(self):
        running = True
        username_input = InputBox(250, 475, 400, 50,"feedback")
        #menu_button = pygame.Rect(250, 450, 400, 50)
        menu_button = pygame.Rect(650, 475, 50, 50)


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

                        print(self.u)
                        if self.u:
                            self.complete_fields=1

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True


                username_input.handle_event(event)

            username_input.update()

            if (self.succes==0):
                self.app.draw_text('Wrong username or password', self.app.font, (255, 255, 255), self.app.screen, 20,
                                   500)
            #self.app.draw_text('login', self.app.font, (255, 255, 255), self.app.screen, 20, 20)
            mx, my = pygame.mouse.get_pos()
            if menu_button.collidepoint((mx, my)):
                if click and self.complete_fields:
                    print("click")
                    self.database_check()
                    username_input = InputBox(250, 475, 400, 50, "feedback")
                    if(self.succes==1):
                        pass
                        #self.menu_screen.menu()
            self.current_collide_rate=-1
            for i in range(5):
                if self.rating_buttons[i].collidepoint((mx,my)):
                    self.current_collide_rate=i
                    if click:
                        print(self.current_collide_rate)
                        self.setted_rating=self.current_collide_rate
                        self.rate()




            self.app.screen.blit(self.play_icon, (650, 475))

            username_input.draw(self.app.screen)



            self.app.screen.blit(self.app.bg, (20, 50))
            self.app.screen.blit(self.app.bg1, (700, 50))
            self.app.draw_text("Avg rating: "+str(self.avg_rating), self.font, (255, 255, 255), self.app.screen, 350,
                               115)
            if(self.setted_rating>-1):
                self.app.draw_text("Your rating: " + str(self.setted_rating +1)+'.0', self.font, (255, 255, 255), self.app.screen,
                               350,
                               145)


            for i in range(3):
                self.app.draw_text('"'+self.feedbacks[i]+'"', self.app.font, (255, 255, 255), self.app.screen, 200,
                                   200+50*i)

            x = 350
            y = 50


            if self.current_collide_rate==-1:
                self.current_collide_rate=self.setted_rating
            if self.current_collide_rate!=-1:
                for i in range(self.current_collide_rate+1):
                    self.app.screen.blit(self.rate0, (x + i * 35, y))
                for i in range(self.current_collide_rate+1,5):
                    self.app.screen.blit(self.rate1, (x + i * 35, y))
            else:
                for i in range(5):
                    self.app.screen.blit(self.rate1, (x + i * 35, y))




            pygame.display.flip()

            pygame.display.update()