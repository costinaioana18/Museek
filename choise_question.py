

import pygame, sys
from pygame.locals import *
from database import Database
class Choice_Question():
    def __init__(self, app,question_no):
        self.checked=0
        self.question_no=question_no
        self.outcome=""
        self.app=app
        self.received_answer=-2
        self.question=""
        self.answers=["","","",""]
        self.right_ans=""
        self.font=pygame.font.SysFont('simsunnsimsun', 32)
        self.database_handler = self.app.database_handler
        self.database_handler.database_init("questions")
        self.mycol = self.database_handler.set_collection("piano_questions")
        self.a_buttons=[]
        self.buttons_coord=[(200, 150-5, 50-10, 50-10),(200, 225-5, 40, 40),(200, 300-5, 40, 40),(200, 375-5, 40, 40)]
        for i in range(4):
            b=pygame.Rect(self.buttons_coord[i])
            self.a_buttons.append(b)

    def get_question_no(self):
        self.database_handler.database_init("users")
        self.mycol = self.database_handler.set_collection("users_data")
        s_count = self.database_handler.get("username", self.app.current_user, "piano_c_s")
        s_count += self.database_handler.get("username", self.app.current_user, "piano_c_f")
        print("TOTAL")
        print(s_count )



    def set_next(self):

        self.get_question_no()
        self.database_handler.database_init("questions")
        self.mycol = self.database_handler.set_collection("piano_questions")
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

    def receive_answer(self,mx,my):
        print(mx)
        print(my)
        for i in range(4):
            if( self.a_buttons[i].collidepoint((mx, my))):
                self.received_answer=i
                print(i)

    def check_answer(self):
        self.checked = 1
        self.database_handler.database_init("users")
        self.mycol = self.database_handler.set_collection("users_data")
        if(self.right_ans==self.received_answer):
            print("raspuns corect")


            self.database_handler.increment_database("username",self.app.current_user,"piano_c_s",1)
            print("incremented")

        else:
            print("raspuns gresit")
            self.database_handler.increment_database("username", self.app.current_user, "piano_c_f", 1)
        self.database_handler.database_init("questions")
        self.mycol = self.database_handler.set_collection("piano_questions")



    def display(self):
        self.app.draw_text(self.question, self.font, (255, 255, 255), self.app.screen, 250, 50)
        if(self.checked):
            self.app.draw_text(self.outcome, self.font, (255, 255, 255), self.app.screen, 250, 100)


        for i in range(4):
            self.app.draw_text(self.answers[i], self.font, (255, 255, 255), self.app.screen, 250, 150+i*75)

        # self.app.draw_text(self.answers[0], self.font, (255, 255, 255), self.app.screen, 250, 150)
        # self.app.draw_text(self.answers[1], self.font, (255, 255, 255), self.app.screen, 250, 225)
        # self.app.draw_text(self.answers[2], self.font, (255, 255, 255), self.app.screen, 250, 300)
        # self.app.draw_text(self.answers[3], self.font, (255, 255, 255), self.app.screen, 250, 375)


        if self.received_answer>-1 and self.received_answer<4:
            pygame.draw.rect(self.app.screen, (255, 162, 193), self.buttons_coord[self.received_answer])

        if self.question !="":
            for i in range(4):
                pygame.draw.rect(self.app.screen, (255, 162, 193), pygame.Rect(self.buttons_coord[i]), 1)


