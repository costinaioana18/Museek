import pygame, sys
from pygame.locals import *
from useful_classes.piano_sound import Piano_sound
from useful_classes.hands_free import *

class Play_the_piano_screen():
    def __init__(self, app):
        self.text_audio=None
        self.app = app
        self.click= False
        self.mic_icon=pygame.image.load('icons/mic_on.jpg')
        self.mic_icon_off=pygame.image.load('icons/mic_off.jpg')
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
        self.voice_notes=("play note c","play note c charp","play note d","play note e flat","play note e","play note f","play note fd","play note g","play note g diez","play note a","play note b flat","play note b")
        self.sounds_list = ["sounds/piano-c.wav", "sounds/piano-cd.wav", "sounds/piano-d.wav", "sounds/piano-eb.wav",
                            "sounds/piano-e.wav", "sounds/piano-f.wav", "sounds/piano-fd.wav", "sounds/piano-g.wav",
                            "sounds/piano-ab.wav", "sounds/piano-a.wav", "sounds/piano-bb.wav", "sounds/piano-b.wav"]
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
        self.hands_free_button=pygame.Rect(0,0,100,100)

    def text_to_command(self,text):
        selected=-1
        greetings=["hello","hi","good morning","good evening","good afternoon","goodnight","have a great day"]
        negations=["don't","do not","avoid"]
        grateful=["thank you","thanks","grateful","appreciate"]
        convo=["how are you","how you doing","how is your","how was your","how do you","you alright"]
        notes = ["note c", "c sharp", "note d", "e flat", "note e", "note f","f sharp", "note g", "g sharp", "note a", "b flat", "note b"]
        aprobs=["play","sound","hear","listen to"]

        for greet in greetings:
            if text.find(greet) >= 0:
                self.text_audio = greet + ", " + self.app.current_user + "!"
                return -1
        for question in convo:
            if text.find(question) >= 0:
                self.text_audio = "I am pretty fine, thank you, " + self.app.current_user
                return -1
        for thank in grateful:
            if text.find(thank) >= 0:
                self.text_audio = "It really was my pleasure, " + self.app.current_user
                return -1
        for i in range(11):
            if text.find(notes[i])>=0:
                selected=i
                print("found note")
        for i in range(3):
            if text.find(negations[i])>=0:
                if i==2:
                    self.text_audio="Ok, we'll avoid to"
                else:
                    for j in range(4):
                        if text.find(aprobs[j])>=0:
                            print(aprobs[j])
                            print(j)
                            if j<2:
                                self.text_audio="Ok, we won't play it"
                            else:
                                self.text_audio="Ok "+ self.app.current_user+ ", you won't " + aprobs[j] + " it"
                #pygame.display.update()
                return -1
        for i in aprobs:
            if text.find(i):
                if(selected>-1):
                    self.text_audio="...playing "+ notes[selected]
                else:
                    self.text_audio="I'm sorry, I didn't understand that"
                return selected
        return -1

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
            #self.app.draw_text('play_the_piano', self.app.font, (255, 255, 255), self.app.screen, 20, 20)
            mx, my = pygame.mouse.get_pos()

            if self.hands_free_button.collidepoint((mx,my)):
                self.app.screen.blit(self.mic_icon_off, (0, 0))
                self.text_audio = "...listening..."
                if click:

                    n=Hands_Free()
                    text=n.voice_input()
                    nott=self.text_to_command(text)

                    if nott!=-1:
                        if (playing):
                            self.piano_sound.set_note(self.sounds_list[nott])
                            self.piano_sound.play()
                            playing = False
                        else:
                            self.piano_sound.set_note(self.sounds_list[nott])
                            self.piano_sound.play()
                            playing = True

            else:
                if self.text_audio=="...listening...":
                    self.text_audio =None
                self.app.screen.blit(self.mic_icon, (0, 0))
            #self.mic_icon = pygame.image.load('icons/mic_on.jpg')


            if click:

                print(str(mx) + ' ' + str(my))
            for i in range(36):
                if self.buttons[i].collidepoint((mx, my)):
                    if click:
                        self.text_audio = None
                        # self.login_screen.login()
                        if (playing):
                            print(i)
                            self.piano_sound.set_note(self.sounds_list[i%12])
                            #self.note_icon1=pygame.image.load(self.notes_icon_list[i])
                            self.piano_sound.play()
                            playing = False
                        else:
                            self.piano_sound.set_note(self.sounds_list[i%12])
                            #self.note_icon1 = pygame.image.load(self.notes_icon_list[i])
                            self.piano_sound.play()
                            playing = True


            self.app.draw_text(self.text_audio, self.app.font, (255, 255, 255), self.app.screen, 120, 20)

            self.app.screen.blit(self.note_icon1, (100, 200))



            pygame.display.update()