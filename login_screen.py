import pygame,sys
from pygame.locals import *
from menu_screen import Menu_screen

class Login_screen():
    def __init__(self, app):
        self.app=app
        self.menu_screen = Menu_screen(self.app)
        self.click = False


    def login(self):
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
            self.app.draw_text('login', self.app.font, (255, 255, 255), self.app.screen, 20, 20)
            mx, my = pygame.mouse.get_pos()
            menu_button = pygame.Rect(50, 100, 200, 50)

            if menu_button.collidepoint((mx, my)):
                if click:
                    self.menu_screen.menu()


            pygame.draw.rect(self.app.screen, (255, 0, 0), menu_button)



            pygame.display.update()