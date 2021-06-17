import pygame,sys
from pygame.locals import *
from screens.login_screen import Login_screen
from screens.signup_screen import Signup_screen
from useful_classes.database import *

class StartUp():
    def __init__(self):
        pygame.init()
        self.color=(255, 162, 193)
        pygame.display.set_caption('Museek')
        self.screen = pygame.display.set_mode((900, 600), 0, 32)
        self.database_handler = Database(
            "mongodb+srv://test:test@cluster0.6borp.mongodb.net/test?retryWrites=true&w=majority")
        self.current_user=None
        self.font = pygame.font.SysFont('inkfree', 32)
        self.click=False
        self.login_screen=Login_screen(self)
        self.signup_screen = Signup_screen(self)
        self.mainClock = pygame.time.Clock()
        self.logo = pygame.image.load('icons/museek.jpg')
        self.bg = pygame.image.load('icons/art.jpg')
        self.bg1 = pygame.image.load('icons/art_flipped.jpg')
        self.signup_btn = pygame.image.load('icons/signup_btn.jpg')
        self.signup_btn_hov = pygame.image.load('icons/signup_btn_hov.jpg')
        self.login_btn = pygame.image.load('icons/login_btn.jpg')
        self.login_btn_hov = pygame.image.load('icons/login_btn_hov.jpg')
        program_Icon = pygame.image.load('icons/prgic.png')
        pygame.display.set_icon(program_Icon)

    def set_user(self,username):
        self.current_user=username

    def draw_text(self,text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def main_menu(self):
        while True:
            click = False
            for event in pygame.event.get():    #start: code borrowed and improved from source: https://www.youtube.com/watch?v=0RryiSjpJn0&t=386s
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True    #end: code borrowed and improved from source: https://www.youtube.com/watch?v=0RryiSjpJn0&t=386s

            self.screen.fill((0, 0, 0))
            #self.draw_text("main menu", self.font, (255, 255, 255), self.screen, 20,20)

            mx, my = pygame.mouse.get_pos()


            button_1 = pygame.Rect(250, 150, 400, 50)
            button_2 = pygame.Rect(250, 250, 400, 50)
            if button_1.collidepoint((mx, my)):
                self.screen.blit(self.login_btn_hov, (250, 150))
                if click:
                    self.login_screen.login()
                    #self.signup_screen.signup()
            else:
                self.screen.blit(self.login_btn, (250, 150))

            if button_2.collidepoint((mx, my)):
                self.screen.blit(self.signup_btn_hov, (250, 250))
                if click:
                    self.signup_screen.signup()
            else:
                self.screen.blit(self.signup_btn, (250, 250))
            #pygame.draw.rect(self.screen, (255, 162, 193), button_1)
            #pygame.draw.rect(self.screen, (255, 162, 193), button_2)
            self.screen.blit(self.logo, (250, 20))
            self.screen.blit(self.bg, (20, 50))
            self.screen.blit(self.bg1, (700, 50))


            self.screen.blit(pygame.image.load('icons/mouse.png'), (mx - 25, my - 25))
            pygame.display.update()
            self.mainClock.tick(60)