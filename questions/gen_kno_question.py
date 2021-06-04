import pygame, sys
class Gen_Kno_Question():
    def __init__(self, app,question_no):
        self.question_no=question_no
        self.app=app
        self.received_answer=""
        self.question=""
        self.answers=["","","",""]
        self.right_ans=0
        self.font=pygame.font.SysFont('inkfree', 32)
        self.database_handler = self.app.database_handler
        self.database_handler.database_init("questions")
        self.mycol = self.database_handler.set_collection("general_questions")
        self.a_buttons=[]
        self.buttons_coord=[(200, 150, 50, 50),(200, 225, 50, 50),(200, 300, 50, 50),(200, 375, 50, 50)]
        for i in range(4):
            b=pygame.Rect(self.buttons_coord[i])
            self.a_buttons.append(b)
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

    def receive_answer(self,mx,my):
        print(mx)
        print(my)
        for i in range(4):
            if( self.a_buttons[i].collidepoint((mx, my))):
                self.received_answer=i
                print(i)

    def check_answer(self):
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
        self.mycol = self.database_handler.set_collection("general_questions")

    def display(self):
        self.app.draw_text(self.question, self.font, (255, 255, 255), self.app.screen, 250, 50)
        self.app.draw_text(self.answers[0], self.font, (255, 255, 255), self.app.screen, 250, 150)
        self.app.draw_text(self.answers[1], self.font, (255, 255, 255), self.app.screen, 250, 225)
        self.app.draw_text(self.answers[2], self.font, (255, 255, 255), self.app.screen, 250, 300)
        self.app.draw_text(self.answers[3], self.font, (255, 255, 255), self.app.screen, 250, 375)


