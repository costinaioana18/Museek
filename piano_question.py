import pygame, sys
from choise_question import Choice_Question
from read_question import Read_Question
from listen_question import Listen_Question

class Piano_Question():
    def __init__(self, app,question_no,type):
        self.app=app
        if type=="choice":
            self.q=Choice_Question(self.app, 0)
        if type=="read":
            self.q = Read_Question(self.app, 0)
        if type=="listen":
            self.q = Listen_Question(self.app, 0)

    def set_next(self):
        self.q.set_next()

    def display(self):
        self.q.display()

    def receive_answer(self,mx,my):
        self.q.receive_answer(mx,my)