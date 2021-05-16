import pygame, sys
from pygame.locals import *
from database import Database
from piano_sound import Piano_sound
import random

class Read_Question():
    def __init__(self, app,question_no):
        print("read")
        self.question_no=question_no
        self.received_question=None
        self.received_answer = None
        self.app=app
        self.question="Press the written note"
        self.note_icon='icons/piano_notes/do1.jpg'
        self.right_ans=0
        self.piano_sound=Piano_sound("sounds/piano-c.wav")
        self.notes_icon_list1 = ['icons/piano_notes/do1.jpg', 'icons/piano_notes/dod1.jpg', 'icons/piano_notes/re1.jpg',
                                 'icons/piano_notes/mib1.jpg', 'icons/piano_notes/mi1.jpg', 'icons/piano_notes/fa1.jpg',
                                 'icons/piano_notes/fad1.jpg', 'icons/piano_notes/sol1.jpg',
                                 'icons/piano_notes/lab1.jpg', 'icons/piano_notes/la1.jpg',
                                 'icons/piano_notes/sib1.jpg', 'icons/piano_notes/si1.jpg']

        self.piano_icon='icons/piano_notes/do.jpg'
        self.font=pygame.font.SysFont('simsunnsimsun', 32)
        self.a_buttons = []
        self.buttons_coord = [(450, 324, 30, 200), (466, 200, 18, 122), (484, 324, 30, 200),
                                        (501, 200, 18, 122), (518, 324, 30, 200), (534, 324, 30, 200),
                                        (550, 200, 18, 122), (567, 324, 30, 200), (582, 200, 18, 122),
                                        (600, 324, 30, 200), (615, 200, 18, 122), (632, 324, 30, 200)]
        self.sounds_list = ["sounds/piano-c.wav", "sounds/piano-cd.wav", "sounds/piano-d.wav", "sounds/piano-eb.wav",
                            "sounds/piano-e.wav", "sounds/piano-f.wav", "sounds/piano-fd.wav", "sounds/piano-g.wav",
                            "sounds/piano-gd.wav", "sounds/piano-a.wav", "sounds/piano-bb.wav", "sounds/piano-b.wav"]

        for btn in self.buttons_coord:
            b=pygame.Rect(btn)
            self.a_buttons.append(b)


        self.note_icon1 = pygame.image.load(self.note_icon)
        self.piano_icon1 = pygame.image.load(self.piano_icon)
        #self.set_next()

    def receive_answer(self,mx,my):
        print(mx)
        print(my)
        for i in range(12):
            if( self.a_buttons[i].collidepoint((mx, my))):
                print(i)
                self.piano_sound.set_note(self.sounds_list[i])
                self.received_answer=i
                self.piano_sound.play()

    def check_answer(self):
        if(self.right_ans==self.received_answer):
            print("raspuns corect")
        else:
            print("raspuns gresit")

    def set_random(self):
        i=random.randint(0, 11)
        print('stil')
        print(i)
        self.right_ans = i
        self.note_icon1=pygame.image.load(self.notes_icon_list1[i])
        print('stil')
        print(i)

    def display(self):
        self.app.draw_text(self.question, self.font, (255, 255, 255), self.app.screen, 250, 50)
        self.app.screen.blit(self.note_icon1, (250, 250))
        self.app.screen.blit(self.piano_icon1, (450, 200))


