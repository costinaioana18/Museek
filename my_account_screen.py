import pygame, sys
from pygame.locals import *
from database import Database

class My_account_screen():
    def __init__(self, app):
        self.app = app
        self.click= False
        self.database_handler = Database(
            "mongodb+srv://test:test@cluster0.6borp.mongodb.net/test?retryWrites=true&w=majority")
        self.database_handler.database_init("users")
        self.mycol = self.database_handler.set_collection("users_data")
        self.p_progress = 0
        self.g_progress = 0
        self.gn_progress = 0
        self.username = "costinaioana"



    def get_progress(self):
        user = self.database_handler.exists("username", self.username )
        if user:
            self.p_progress = self.database_handler.get("username",self.username,"piano_c_s")
            print("progress")
            print(self.p_progress)

    def my_account(self):
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
            self.app.draw_text('Progress', self.app.font, self.app.color, self.app.screen, 330, 70)
            self.app.draw_text('Graduation', self.app.font, self.app.color, self.app.screen, 630, 70)
            self.app.draw_text('my account', self.app.font, self.app.color, self.app.screen, 20, 20)



            p_progress=int(self.p_progress*200/100)
            g_progress=int(self.g_progress*200/50)
            gn_progress=int(self.gn_progress*200/10)
            pygame.draw.rect(self.app.screen, (255, 162, 193), pygame.Rect(300, 150, p_progress, 30))
            pygame.draw.rect(self.app.screen, (255, 162, 193), pygame.Rect(300, 150, 200, 30), 1)
            self.app.draw_text('Piano', self.app.font, self.app.color, self.app.screen, 150, 145)
            self.app.draw_text('15 days', self.app.font, self.app.color, self.app.screen, 650, 145)

            pygame.draw.rect(self.app.screen, (255, 162, 193), pygame.Rect(300, 250, g_progress, 30))
            pygame.draw.rect(self.app.screen, (255, 162, 193), pygame.Rect(300, 250, 200, 30), 1)
            self.app.draw_text('Guitar', self.app.font, self.app.color, self.app.screen, 150, 245)
            self.app.draw_text('89 days', self.app.font, self.app.color, self.app.screen, 650, 245)

            pygame.draw.rect(self.app.screen, (255, 162, 193), pygame.Rect(300, 350, gn_progress, 30))
            pygame.draw.rect(self.app.screen, (255, 162, 193), pygame.Rect(300, 350, 200, 30), 1)
            self.app.draw_text('General', self.app.font, self.app.color, self.app.screen, 150, 345)
            self.app.draw_text('3 days', self.app.font, self.app.color, self.app.screen, 650, 345)



            pygame.display.update()