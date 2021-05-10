import pygame, sys
from pygame.locals import *
from database import Database
class Choice_Question():
    def __init__(self, app,question_no):
        self.question_no=question_no
        self.app=app
        self.question=None
        self.answers=None
        self.right_ans=None
        self.font=pygame.font.SysFont('simsunnsimsun', 32)
        self.database_handler = Database(
            "mongodb+srv://test:test@cluster0.6borp.mongodb.net/test?retryWrites=true&w=majority")
        self.database_handler.database_init("questions")
        self.mycol = self.database_handler.set_collection("piano_questions")
        self.set_next()
    def set_next(self):
        question = self.database_handler.get("question_no",self.question_no,"question")
        a1 = self.database_handler.get("question_no", self.question_no, "a1")
        a2 = self.database_handler.get("question_no", self.question_no, "a2")
        a3 = self.database_handler.get("question_no", self.question_no, "a3")
        a4 = self.database_handler.get("question_no", self.question_no, "a4")
        right_ans = self.database_handler.get("question_no", self.question_no, "correct")
        answers=[a1,a2,a3,a4]
        self.question = question
        self.answers = answers
        self.right_ans = right_ans
        self.question_no+=1
    def display(self):
        self.app.draw_text(self.question, self.font, (255, 255, 255), self.app.screen, 250, 50)
        self.app.draw_text(self.answers[0], self.font, (255, 255, 255), self.app.screen, 250, 150)
        self.app.draw_text(self.answers[1], self.font, (255, 255, 255), self.app.screen, 250, 250)
        self.app.draw_text(self.answers[2], self.font, (255, 255, 255), self.app.screen, 250, 350)
        self.app.draw_text(self.answers[3], self.font, (255, 255, 255), self.app.screen, 250, 450)


