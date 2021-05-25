import pygame, sys
from pygame.locals import *
from piano_sound import Piano_sound


class Piano_notes_screen():
    def __init__(self, app):

        self.notex_title_list=['C (Do)','C# (Do#)','D (Re)','Eb (Mi b)','E (Mi)','F (Fa)','F (Fa#)','G (Sol)','Ab (La b)','A (La)','Bb (Si b)','B (Si)']
        self.notes_icon_list1=['icons/piano_notes/do1.jpg','icons/piano_notes/dod1.jpg','icons/piano_notes/re1.jpg','icons/piano_notes/mib1.jpg','icons/piano_notes/mi1.jpg','icons/piano_notes/fa1.jpg','icons/piano_notes/fad1.jpg','icons/piano_notes/sol1.jpg','icons/piano_notes/lab1.jpg','icons/piano_notes/la1.jpg','icons/piano_notes/sib1.jpg','icons/piano_notes/si1.jpg']
        self.notes_icon_list = ['icons/piano_notes/do.jpg', 'icons/piano_notes/dod.jpg', 'icons/piano_notes/re.jpg',
                                'icons/piano_notes/mib.jpg', 'icons/piano_notes/mi.jpg', 'icons/piano_notes/fa.jpg',
                                'icons/piano_notes/fad.jpg', 'icons/piano_notes/sol.jpg',
                                'icons/piano_notes/lab.jpg', 'icons/piano_notes/la.jpg', 'icons/piano_notes/sib.jpg',
                                'icons/piano_notes/si.jpg']
        self.sounds_list=["sounds/piano-c.wav","sounds/piano-cd.wav","sounds/piano-d.wav","sounds/piano-eb.wav","sounds/piano-e.wav","sounds/piano-f.wav","sounds/piano-fd.wav","sounds/piano-g.wav","sounds/piano-gd.wav","sounds/piano-a.wav","sounds/piano-bb.wav","sounds/piano-b.wav"]
        self.button_coordinates_list=[(450, 200, 30, 200),(466, 200, 18, 122),(484, 200, 18, 200),(501, 200, 18, 122),(518, 200, 30, 200),(534, 200, 30, 200),(550, 200, 18, 122),(567, 200, 18, 200),(582, 200, 18, 122),(600, 200, 25, 200),(615, 200, 18, 122),(632, 200, 18, 200)]
        self.app = app
        self.click= False
        self.count=0
        self.piano_sound=Piano_sound("sounds/piano-c.wav")
        self.font = pygame.font.SysFont('simsunnsimsun', 32)
        self.note_icon1=pygame.image.load('icons/piano_notes/do.jpg')
        self.note_icon2=pygame.image.load('icons/piano_notes/do1.jpg')
        self.note_title="C (Do)"
        #self.sound_play_button = pygame.Rect(250, 150, 400, 50)
        self.sound_piano_button=pygame.Rect(450, 200, 30, 200)
        self.next_icon = pygame.image.load('icons/next.jpg')
        self.next_button=pygame.Rect(400, 450, 100, 50)

    def next_note(self):
        if self.count==11:
            self.count=0
        else:
            self.count+=1
        self.note_title=self.notex_title_list[self.count]
        self.note_icon1 = pygame.image.load(self.notes_icon_list[self.count])
        self.note_icon2 = pygame.image.load(self.notes_icon_list1[self.count])
        self.sound_piano_button = pygame.Rect(self.button_coordinates_list[self.count])
        self.piano_sound.set_note(self.sounds_list[self.count])
        print("next")

    def piano_notes(self):
        running = True

        playing = True
        while running:
            click = False
            mx, my = pygame.mouse.get_pos()

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
            #self.app.draw_text('piano notes screen', self.app.font, (255, 255, 255), self.app.screen, 20, 20)

            if  self.sound_piano_button.collidepoint((mx, my)):
                if click:
                    #self.login_screen.login()
                    if(playing):
                        print("playin")
                        self.piano_sound.play()
                        playing= False
                    else:
                        print("npt playin")
                        self.piano_sound.play()
                        playing=True


                    print("clicked")
                    pass

            if click:
                print(mx)
                print(my)
            if  self.next_button.collidepoint((mx, my)):
                if click:
                    self.next_note()

            self.app.screen.blit(self.note_icon1, (450, 200))
            self.app.screen.blit(self.note_icon2, (250, 250))
            self.app.screen.blit(self.next_icon, (400, 450))
            self.app.draw_text(self.note_title, self.font, (255, 255, 255), self.app.screen, 400, 50)
            self.app.screen.blit(self.app.bg, (20, 50))
            self.app.screen.blit(self.app.bg1, (700, 50))
            #pygame.draw.rect(self.app.screen, (255, 162, 193), self.sound_play_button)

            pygame.display.update()