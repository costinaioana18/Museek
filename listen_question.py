import pygame, sys
from pygame.locals import *
from database import Database
class Listen_Question():
    def __init__(self, app,question_no):
        print("listed")
        self.question_no=question_no
        self.app=app
        self.question="aa"
        self.note_icon='icons/piano_notes/do1.jpg'
        self.right_ans="None"
        self.piano_icon='icons/piano_notes/do.jpg'
        self.font=pygame.font.SysFont('simsunnsimsun', 32)
        # self.database_handler = Database(
        #     "mongodb+srv://test:test@cluster0.6borp.mongodb.net/test?retryWrites=true&w=majority")
        # self.database_handler.database_init("questions")
        # self.mycol = self.database_handler.set_collection("piano_questions")
        self.note_icon1 = pygame.image.load(self.note_icon)
        self.piano_icon1 = pygame.image.load(self.piano_icon)
        #self.set_next()
    def set_next(self):
        # question = self.database_handler.get("question_no",self.question_no,"question")
        # a1 = self.database_handler.get("question_no", self.question_no, "a1")
        # a2 = self.database_handler.get("question_no", self.question_no, "a2")
        # a3 = self.database_handler.get("question_no", self.question_no, "a3")
        # a4 = self.database_handler.get("question_no", self.question_no, "a4")
        # right_ans = self.database_handler.get("question_no", self.question_no, "correct")
        # answers=[a1,a2,a3,a4]
        question="cf"
        right_ans=0
        self.question = question
        self.right_ans = right_ans
        self.question_no+=1
    def display(self):
        self.app.draw_text(self.question, self.font, (255, 255, 255), self.app.screen, 250, 50)
        self.app.screen.blit(self.note_icon1, (250, 250))
        self.app.screen.blit(self.piano_icon1, (400, 200))


