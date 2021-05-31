import random
from useful_classes.database import *
import pygame


class Chord_Question():
    def __init__(self, app):
        self.database_handler = app.database_handler
        self.outcome=None
        self.checked=0
        self.app=app
        self.question="Play chord C major"
        self.notex_title_list = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G',
                                 'Ab', 'A', 'Bb', 'B']
        self.chords_name=["C major", "D major", "E major","F major","G major","A major","B major"]
        self.chords=[[0,3,7],[2,5,9],[4,7,11],[5,8,0],[7,10,2],[9,0,4],[11,2,6]]
        self.chords_sounds=["Cm.mp3","Dm.mp3","Em.mp3","Fm.mp3","Gm.mp3","Am.mp3","Bm.mp3"]
        self.sound=self.chords_sounds[0]
        self.topic=[0,2,4,5,7,9,11]
        self.answer=0
        self.current_answer=[-1,-1,-1]
        self.right_answer=[0,3,7]
        self.current_position=-1

    def set_random(self):
        i=self.answer
        while i==self.answer:
            i=random.randint(0, 6)
        self.answer=i

    def next_question(self):

        self.current_position=-1
        self.current_answer=[-1,-1,-1]
        self.set_random()
        print (self.answer)
        self.question="Play chord " + self.chords_name[self.answer]
        self.right_answer=self.chords[self.answer]
        self.sound=self.chords_sounds[self.answer]
        self.checked=0

    def receive_answer(self,i):
        if(self.current_position==-1):
            self.current_position=0
        if (self.current_position == 2):
            self.current_answer[self.current_position] = i
            self.check_answer()
        else:
            self.current_answer[self.current_position]=i
            self.current_position+=1
        print(self.current_answer)

    def is_correct(self):
        for i in range (0,3):
            if self.right_answer[i]!=self.current_answer[i]:
                return -1
        return 1

    def check_answer(self):

        self.current_position=0
        correct=self.is_correct()
        if correct==1:
            self.outcome="congratulations"
            self.database_handler.database_init("users")
            self.mycol = self.database_handler.set_collection("users_data")
            self.database_handler.increment_database("username", self.app.current_user, "chords_s", 1)
            print("raspuns corect")

            self.database_handler.database_init("users_progress")
            self.mycol = self.database_handler.set_collection(self.app.current_user)
            self.database_handler.insert(
                {"piano_c": 0, "piano_l": 0, "piano_r": 0, "gen_c": 0, "chords": 1,
                 "topic": self.topic[self.answer], "result": 1})

        else:
            self.outcome="wrong"
            self.database_handler.database_init("users")
            self.mycol = self.database_handler.set_collection("users_data")
            self.database_handler.increment_database("username", self.app.current_user, "chords_f", 1)

            self.database_handler.database_init("users_progress")
            self.mycol = self.database_handler.set_collection(self.app.current_user)
            self.database_handler.insert(
                {"piano_c": 0, "piano_l": 0, "piano_r": 0, "gen_c": 0, "chords": 1,
                 "topic": self.topic[self.answer], "result": 0})


        self.checked = 1





        print("check")


    def display(self):
        self.app.draw_text(self.question, self.app.font, (255, 255, 255), self.app.screen, 250, 50)
        if(self.checked==1):
            self.app.draw_text(self.outcome, self.app.font, (255, 255, 255), self.app.screen, 250, 150)
            for i in range(0,3):
                self.app.draw_text(self.notex_title_list[self.current_answer[i]], self.app.font, (255, 255, 255), self.app.screen, 300+i*50, 100)

        if(self.current_position!=-1):
            for i in range(0,self.current_position):
                self.app.draw_text(self.notex_title_list[self.current_answer[i]], self.app.font, (255, 255, 255), self.app.screen, 300+i*50, 100)