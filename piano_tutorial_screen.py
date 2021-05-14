import pygame, sys
from pygame.locals import *
from piano_notes_screen import Piano_notes_screen
from play_the_piano_screen import Play_the_piano_screen


class Piano_tutorial_screen():
    def __init__(self, app):
        self.app = app
        self.click= False
        self.notes_icon= pygame.image.load('icons/next.jpg')
        self.piano_notes_screen=Piano_notes_screen(self.app)
        self.piano_play_screen = Play_the_piano_screen(self.app)
        self.play_icon = pygame.image.load('icons/next.jpg')

    def piano_tutorial(self):
        running = True
        notes_button = pygame.Rect(400, 525, 100, 50)
        play_piano_button = pygame.Rect(100, 525, 100, 50)
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
            self.app.draw_text('piano tutorial screen', self.app.font, (255, 255, 255), self.app.screen, 20, 20)
            mx, my = pygame.mouse.get_pos()
            if notes_button.collidepoint((mx, my)):
                if click:
                    print("piano_notes")
                    self.piano_notes_screen.piano_notes()
            if play_piano_button.collidepoint((mx, my)):
                if click:
                    print("piano_play")
                    self.piano_play_screen.play_the_piano()

            self.app.screen.blit(self.notes_icon, (400, 525))
            self.app.screen.blit(self.play_icon, (100, 525))

            pygame.display.update()