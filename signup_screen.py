import pygame,sys
from pygame.locals import *
from menu_screen import Menu_screen

class Signup_screen():
    def __init__(self, app):
        self.app=app
        self.menu_screen = Menu_screen(self.app)
        self.click = False
        self.icon = pygame.image.load('icons/signup.jpg')
        self.play_icon = pygame.image.load('icons/play.jpg')


    def signup(self):
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
            self.app.draw_text('signup', self.app.font, (255, 255, 255), self.app.screen, 20, 20)
            mx, my = pygame.mouse.get_pos()
            menu_button = pygame.Rect(250, 500, 400, 50)

            if menu_button.collidepoint((mx, my)):
                if click:
                    self.menu_screen.menu()

            self.app.screen.blit(self.icon, (250, 20))
            self.app.screen.blit(self.play_icon, (250, 450))
            #pygame.draw.rect(self.app.screen, (255, 162, 193), menu_button)



            pygame.display.update()