import pygame, sys
from useful_classes.piano_sound import Piano_sound
import random


class Read_Question():
    def __init__(self, app, question_no):
        self.checked = 0
        print("read")
        self.question_no = question_no
        self.mx = None
        self.my = None
        self.received_question = None
        self.received_answer = None
        self.app = app
        self.database_handler = self.app.database_handler
        self.question = "Press the written note"
        self.note_icon = 'icons/piano_notes/do1.jpg'
        self.right_ans = 0
        self.piano_sound = Piano_sound("sounds/piano-c.wav")
        self.right_icons = ['icons/right_piano/do.jpg', 'icons/right_piano/dod.jpg', 'icons/right_piano/re.jpg',
                            'icons/right_piano/mib.jpg', 'icons/right_piano/mi.jpg', 'icons/right_piano/fa.jpg',
                            'icons/right_piano/fad.jpg', 'icons/right_piano/sol.jpg',
                            'icons/right_piano/lab.jpg', 'icons/right_piano/la.jpg', 'icons/right_piano/sib.jpg',
                            'icons/right_piano/si.jpg']
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

        self.piano_icon = 'icons/pianoo.jpg'
        self.font = pygame.font.SysFont('inkfree', 32)
        self.a_buttons = []
        self.buttons_coord = [(450, 324, 30, 200), (466, 200, 18, 122), (484, 324, 30, 200),
                              (501, 200, 18, 122), (518, 324, 30, 200), (534, 324, 30, 200),
                              (550, 200, 18, 122), (567, 324, 30, 200), (582, 200, 18, 122),
                              (600, 324, 30, 200), (615, 200, 18, 122), (632, 324, 30, 200)]
        self.sounds_list = ["sounds/piano-c.wav", "sounds/piano-cd.wav", "sounds/piano-d.wav", "sounds/piano-eb.wav",
                            "sounds/piano-e.wav", "sounds/piano-f.wav", "sounds/piano-fd.wav", "sounds/piano-g.wav",
                            "sounds/piano-gd.wav", "sounds/piano-a.wav", "sounds/piano-bb.wav", "sounds/piano-b.wav"]

        for btn in self.buttons_coord:
            b = pygame.Rect(btn)
            self.a_buttons.append(b)

        self.note_icon1 = pygame.image.load(self.note_icon)
        self.piano_icon1 = pygame.image.load(self.piano_icon)
        # self.set_next()

    def receive_answer(self, mx, my):
        print(mx)
        print(my)
        for i in range(12):
            if (self.a_buttons[i].collidepoint((mx, my))):
                print(i)
                self.piano_sound.set_note(self.sounds_list[i])
                self.piano_icon1 = pygame.image.load(self.notes_icon_list[i])
                self.received_answer = i
                self.piano_sound.play()
                self.mx = mx
                self.my = my

    def check_answer(self):
        self.checked = 1

        self.database_handler.database_init("users")
        self.mycol = self.database_handler.set_collection("users_data")
        if self.right_ans == self.received_answer:

            self.database_handler.increment_database("username", self.app.current_user, "piano_r_s", 1)


            self.database_handler.database_init("users_progress")
            self.mycol = self.database_handler.set_collection(self.app.current_user)
            self.database_handler.insert(
                {"piano_c": 0, "piano_l": 0, "piano_r": 1, "gen_c": 0, "chords": 0,
                 "topic": self.right_ans, "result": 1})
        else:
            self.checked = -1
            self.database_handler.increment_database("username", self.app.current_user, "piano_r_f", 1)

            self.database_handler.database_init("users_progress")
            self.mycol = self.database_handler.set_collection(self.app.current_user)
            self.database_handler.insert(
                {"piano_c": 0, "piano_l": 0, "piano_r": 1, "gen_c": 0, "chords": 0,
                 "topic": self.right_ans, "result": 0})

    def set_random(self):
        i = random.randint(0, 11)

        self.right_ans = i
        self.note_icon1 = pygame.image.load(self.notes_icon_list1[i])


    def display(self):
        self.app.draw_text(self.question, self.font, (255, 255, 255), self.app.screen, 250, 50)
        self.app.screen.blit(self.note_icon1, (250, 250))

        self.app.screen.blit(self.piano_icon1, (450, 200))

        if self.checked != 0:
            self.piano_icon1 = pygame.image.load(self.right_icons[self.right_ans])
            if self.checked == -1:
                pygame.draw.line(self.app.screen, (255, 1, 1), (self.mx - 10, self.my + 10),
                                 (self.mx + 10, self.my - 10))
                pygame.draw.line(self.app.screen, (255, 1, 1), (self.mx - 10, self.my - 10),
                                 (self.mx + 10, self.my + 10))
