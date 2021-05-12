import pygame, sys
from pygame.locals import *
from piano_sound import Piano_sound

class Play_the_piano_screen():
    def __init__(self, app):
        self.app = app
        self.click= False
        self.note_icon1 = pygame.image.load('icons/pianoFUL.jpg')
        self.notex_title_list = ['C (Do)', 'C# (Do#)', 'D (Re)', 'Eb (Mi b)', 'E (Mi)', 'F (Fa)', 'F (Fa#)', 'G (Sol)',
                                 'Ab (La b)', 'A (La)', 'Bb (Si b)', 'B (Si)']
        self.notes_icon_list1 = ['icons/piano_notes/do1.jpg', 'icons/piano_notes/dod1.jpg', 'icons/piano_notes/re1.jpg',
                                 'icons/piano_notes/mib1.jpg', 'icons/piano_notes/mi1.jpg', 'icons/piano_notes/fa1.jpg',
                                 'icons/piano_notes/fad1.jpg', 'icons/piano_notes/sol1.jpg',
                                 'icons/piano_notes/lab1.jpg', 'icons/piano_notes/la1.jpg',
                                 'icons/piano_notes/sib1.jpg', 'icons/piano_notes/si1.jpg']
        self.notes_icon_list = ['icons/piano_notes/do.jpg', 'icons/piano_notes/dod.jpg', 'icons/piano_notes/re.jpg',
                                'icons/piano_notes/mib.jpg', 'icons/piano_notes/mi.jpg', 'icons/piano_notes/fa.jpg',
                                'icons/piano_notes/fad.jpg', 'icons/piano_notes/sol.jpg',
                                'icons/piano_notes/lab.jpg', 'icons/piano_notes/la.jpg', 'icons/piano_notes/sib.jpg',
                                'icons/piano_notes/si.jpg']
        self.piano_sound = Piano_sound("sounds/piano-c.wav")
        self.sounds_list = ["sounds/piano-c.wav", "sounds/piano-cd.wav", "sounds/piano-d.wav", "sounds/piano-eb.wav",
                            "sounds/piano-e.wav", "sounds/piano-f.wav", "sounds/piano-fd.wav", "sounds/piano-g.wav",
                            "sounds/piano-gd.wav", "sounds/piano-a.wav", "sounds/piano-bb.wav", "sounds/piano-b.wav"]
        self.button_coordinates_list = [(450, 200, 30, 200), (466, 200, 18, 122), (484, 200, 18, 200),
                                        (501, 200, 18, 122), (518, 200, 30, 200), (534, 200, 30, 200),
                                        (550, 200, 18, 122), (567, 200, 18, 200), (582, 200, 18, 122),
                                        (600, 200, 25, 200), (615, 200, 18, 122), (632, 200, 18, 200)]
        self.new_button_list=[(100,348,30,82),(118,200,18,150),(133,348,30,82),(161,200,18,150),(166,348,30,82),(200,348,30,82),
                              (220,200,18,150),(234,348,30,82),(257,200,18,150),(266,348,30,82),(292,200,18,150),(300,348,30,82),
                              (334,348,30,82),(354,200,18,150),(367,348,30,82),(392,200,18,150),(401,348,30,82),(434,348,30,82),
                              (451,200,18,150),(467,348,30,82),(490,200,18,150),(501,348,30,82),(528,200,18,150),(534,348,30,82),
                              (567,348,30,82),(586,200,18,150),(601,348,30,82),(625,200,18,150),(635,348,30,82),(667,348,30,82),
                              (686,200,18,150),(700,348,30,82),(724,200,18,150),(734,348,30,82),(761,200,18,150),(769,348,30,82),]
        self.sound_piano_button = pygame.Rect(450, 200, 30, 200)
        self.buttons=[]
        for coord in self.new_button_list:
            self.buttons.append(pygame.Rect(coord))




    def play_the_piano(self):
        running = True
        playing = True
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
            self.app.draw_text('play_the_piano', self.app.font, (255, 255, 255), self.app.screen, 20, 20)
            mx, my = pygame.mouse.get_pos()
            if click:
                print(str(mx) + ' ' + str(my))
            for i in range(36):
                if self.buttons[i].collidepoint((mx, my)):
                    if click:
                        # self.login_screen.login()
                        if (playing):
                            print(i)
                            self.piano_sound.set_note(self.sounds_list[i%6])
                            #self.note_icon1=pygame.image.load(self.notes_icon_list[i])
                            self.piano_sound.play()
                            playing = False
                        else:
                            self.piano_sound.set_note(self.sounds_list[i%6])
                            #self.note_icon1 = pygame.image.load(self.notes_icon_list[i])
                            self.piano_sound.play()
                            playing = True

            self.app.screen.blit(self.note_icon1, (100, 200))
            pygame.display.update()