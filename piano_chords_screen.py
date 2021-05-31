import pygame, sys
from pygame.locals import *
from piano_sound import Piano_sound
from chord_question import *

class Piano_chords_screen():
    def __init__(self, app):
        self.question=Chord_Question(app)
        self.app = app
        self.click= False
        self.note_icon1 = pygame.image.load('icons/pianoFUL.jpg')
        self.notex_title_list = ['C (Do)', 'C# (Do#)', 'D (Re)', 'Eb (Mi b)', 'E (Mi)', 'F (Fa)', 'F (Fa#)', 'G (Sol)',
                                 'Ab (La b)', 'A (La)', 'Bb (Si b)', 'B (Si)']
        self.piano_sound = Piano_sound("sounds/piano-c.wav")
        self.sounds_list = ["sounds/piano-c.wav", "sounds/piano-cd.wav", "sounds/piano-d.wav", "sounds/piano-eb.wav",
                            "sounds/piano-e.wav", "sounds/piano-f.wav", "sounds/piano-fd.wav", "sounds/piano-g.wav",
                            "sounds/piano-gd.wav", "sounds/piano-a.wav", "sounds/piano-bb.wav", "sounds/piano-b.wav"]
        self.new_button_list=[(100,348,30,82),(118,200,18,150),(133,348,30,82),(161,200,18,150),(166,348,30,82),(200,348,30,82),
                              (220,200,18,150),(234,348,30,82),(257,200,18,150),(266,348,30,82),(292,200,18,150),(300,348,30,82),
                              (334,348,30,82),(354,200,18,150),(367,348,30,82),(392,200,18,150),(401,348,30,82),(434,348,30,82),
                              (451,200,18,150),(467,348,30,82),(490,200,18,150),(501,348,30,82),(528,200,18,150),(534,348,30,82),
                              (567,348,30,82),(586,200,18,150),(601,348,30,82),(625,200,18,150),(635,348,30,82),(667,348,30,82),
                              (686,200,18,150),(700,348,30,82),(724,200,18,150),(734,348,30,82),(761,200,18,150),(769,348,30,82),]

        self.buttons=[]
        for coord in self.new_button_list:
            self.buttons.append(pygame.Rect(coord))

        self.next_chord_button=pygame.Rect(0,0,100,100)


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
            mx, my = pygame.mouse.get_pos()



            if click:

                print(str(mx) + ' ' + str(my))
            for i in range(36):
                if self.buttons[i].collidepoint((mx, my)):
                    if click:
                        i = i % 12

                        if (playing):


                            self.piano_sound.set_note(self.sounds_list[i])
                            self.piano_sound.play()
                            playing = False
                        else:
                            self.piano_sound.set_note(self.sounds_list[i])
                            self.piano_sound.play()
                            playing = True
                        self.question.receive_answer(i)
            self.question.display()

            if self.next_chord_button.collidepoint((mx,my)):
                if click:
                    self.question.next_question()

            self.app.screen.blit(self.note_icon1, (100, 200))

            self.app.screen.blit(pygame.image.load("icons/next.jpg"),(0,0))



            pygame.display.update()