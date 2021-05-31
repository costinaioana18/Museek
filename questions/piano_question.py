import pygame, sys
from questions.choise_question import Choice_Question
from questions.read_question import Read_Question
from questions.listen_question import Listen_Question

class Piano_Question():
    def __init__(self, app,question_no,type):
        self.app=app
        self.type=type
        if type=="choice":
            self.q=Choice_Question(self.app, 0)
        if type=="read":
            self.q = Read_Question(self.app, 0)
        if type=="listen":
            self.q = Listen_Question(self.app, 0)

    def set_next(self):
        if self.type=="choice":
            self.q.set_next()
        if self.type=="read" or self.type=="listen":
            self.q.set_random()

    def display(self):
        self.q.display()

    def receive_answer(self,mx,my):
        self.q.receive_answer(mx,my)

    def check_answer(self):
        self.q.check_answer()