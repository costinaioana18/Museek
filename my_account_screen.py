import pygame, sys
from pygame.locals import *
from datetime import date
from database import Database
from prediction_algorithm import *
class My_account_screen():
    def __init__(self, app):
        self.app = app
        self.click= False
        self.database_handler = self.app.database_handler
        self.database_handler.database_init("users")
        self.mycol = self.database_handler.set_collection("users_data")
        self.p_progress = 0
        self.p_regress=0
        self.chords_progress = 0
        self.chords_regress = 0
        self.gn_progress = 0
        self.gn_regress = 0
        self.total_piano=50
        self.total_chords=20
        self.piano_days_left=63
        self.chords_days_left=35
        self.o_day=None
        self.o_month=None
        self.o_year=None

    def date_difference(self,cd,cm,cy,od,om,oy):
        mfy=0
        d=0
        if(cm>om):
            mfy=(cy-oy)*12+cm-om-1
        else:
            mfy=(cy-1-oy)*12+12-om-1+cm
        if(cd>od):
            mfy+=1
            d=cd-od
        else:
            d=30-od+cd
        d+=mfy*30
        if(d==0):
            return 1
        else:
            return d




    def get_progress(self):
        print("gettin")
        self.p_progress=0
        self.database_handler.database_init("users")
        self.mycol = self.database_handler.set_collection("users_data")
        print(self.app.current_user)
        user = self.database_handler.exists("username", self.app.current_user )

        if user:
            self.o_day = self.database_handler.get("username", self.app.current_user, "day")
            self.o_month = self.database_handler.get("username", self.app.current_user, "month")
            self.o_year = self.database_handler.get("username", self.app.current_user, "year")
            self.p_progress += self.database_handler.get("username",self.app.current_user,"piano_c_s")
            self.p_progress += self.database_handler.get("username", self.app.current_user, "piano_l_s")
            self.p_progress += self.database_handler.get("username", self.app.current_user, "piano_r_s")
            self.p_regress += self.database_handler.get("username", self.app.current_user, "piano_c_f")
            self.p_regress += self.database_handler.get("username", self.app.current_user, "piano_l_f")
            self.p_regress += self.database_handler.get("username", self.app.current_user, "piano_r_f")
            self.p_progress += self.database_handler.get("username", self.app.current_user, "piano_c_s")
            self.p_progress += self.database_handler.get("username", self.app.current_user, "piano_l_s")
            self.chords_progress = self.database_handler.get("username", self.app.current_user, "chords_s")
            self.chords_regress = self.database_handler.get("username", self.app.current_user, "chords_f")
            self.gn_progress = self.database_handler.get("username", self.app.current_user, "gen_c_s")
            self.gn_regress = self.database_handler.get("username", self.app.current_user, "gen_c_f")
            print("progress")
            print(self.chords_progress)
            print("progress")
            print(self.p_progress)



    def get_mean(self,vector):
        sum=0
        count=0
        for element in vector:
            sum+=element
            count+=1
        return float(sum/count)


    def graduation_expect(self):
        if(self.p_progress>0 and self.p_regress>0):
            left=self.total_piano-self.p_progress #numarul de intrebari pe care trebuie sa le completez
            vector=[]
            for topic in range(11):
                    vector.append([1,0,0,0,0,topic])
            for topic in range(11):
                    vector.append([0,1,0,0,0,topic])
            for topic in range(11):
                    vector.append([0,0,1,0,0,topic])

            n=Prediction_Algorithm(self.app) #antrenam un model cu datele pe care le avem despre progres
            n.train_model() #folosim SVM, vezi clasa Prediction_Algorithm
            prob=n.get_probabillity(vector) # aflam care este probabilitatea de a raspunde corect la intrebari
                                            #viitoare in functie de tip si topic

            today=date.today()
            c_day=int(today.strftime('%d'))
            c_month=int(today.strftime('%m'))
            c_year=int(today.strftime('%y'))

            days=self.date_difference(c_day,c_month,c_year,self.o_day,self.o_month,self.o_year)
            #ne folosim de data originii contului pentru a stabili frecventa cu care userul
            #Utilizeaza aplicatia
            frequency=float(self.p_progress/days)

            mean=self.get_mean(prob) #aflam probabilitatea medie de a raspunde corect la o intrebare
            self.p_days_left=int(left/float(frequency*mean))
            #aflam numarul de zile pana la finalizarea aplicatiei:
            # numarul de intrebari ramase impartit la
            # frecventa presiza/zi inmultita cu probabilitatea prezisa de a raspunde corect


    def chord_graduation_expect(self):
        if(self.chords_progress>0 and self.chords_regress>0):
            left=self.total_chords-self.chords_progress #numarul de intrebari pe care trebuie sa le completez
            vector=[]
            for topic in [0,2,4,5,7,9,11]:
                    vector.append([0,0,0,0,1,topic])

            n=Prediction_Algorithm(self.app) #antrenam un model cu datele pe care le avem despre progres
            n.train_model() #folosim SVM, vezi clasa Prediction_Algorithm
            prob=n.get_probabillity(vector) # aflam care este probabilitatea de a raspunde corect la intrebari
                                            #viitoare in functie de tip si topic

            today=date.today()
            c_day=int(today.strftime('%d'))
            c_month=int(today.strftime('%m'))
            c_year=int(today.strftime('%y'))

            days=self.date_difference(c_day,c_month,c_year,self.o_day,self.o_month,self.o_year)
            #ne folosim de data originii contului pentru a stabili frecventa cu care userul
            #Utilizeaza aplicatia
            frequency=float(self.chords_progress/days)

            mean=self.get_mean(prob) #aflam probabilitatea medie de a raspunde corect la o intrebare
            self.chords_days_left=int(left/float(frequency*mean))
            #aflam numarul de zile pana la finalizarea aplicatiei:
            # numarul de intrebari ramase impartit la
            # frecventa presiza/zi inmultita cu probabilitatea prezisa de a raspunde corect




    def my_account(self):
        running = True
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
            self.app.draw_text('Progress', self.app.font, self.app.color, self.app.screen, 330, 70)
            self.app.draw_text('Graduation', self.app.font, self.app.color, self.app.screen, 630, 70)
            self.app.draw_text('my account', self.app.font, self.app.color, self.app.screen, 20, 20)


            p_progress=int(self.p_progress*200/100)
            chord_progress=int(self.chords_progress*200/50)
            gn_progress=int(self.gn_progress*200/10)
            pygame.draw.rect(self.app.screen, (255, 162, 193), pygame.Rect(300, 150, p_progress, 30))
            pygame.draw.rect(self.app.screen, (255, 162, 193), pygame.Rect(300, 150, 200, 30), 1)
            self.app.draw_text('Piano basics', self.app.font, self.app.color, self.app.screen, 100, 145)
            self.app.draw_text(str(self.piano_days_left)+' days', self.app.font, self.app.color, self.app.screen, 650, 145)

            pygame.draw.rect(self.app.screen, (255, 162, 193), pygame.Rect(300, 250, chord_progress, 30))
            pygame.draw.rect(self.app.screen, (255, 162, 193), pygame.Rect(300, 250, 200, 30), 1)
            self.app.draw_text('Piano Chords', self.app.font, self.app.color, self.app.screen, 100, 245)
            self.app.draw_text(str(self.chords_days_left)+' days', self.app.font, self.app.color, self.app.screen, 650, 245)

            pygame.draw.rect(self.app.screen, (255, 162, 193), pygame.Rect(300, 350, gn_progress, 30))
            pygame.draw.rect(self.app.screen, (255, 162, 193), pygame.Rect(300, 350, 200, 30), 1)
            self.app.draw_text('General', self.app.font, self.app.color, self.app.screen, 100, 345)
            self.app.draw_text('3 days', self.app.font, self.app.color, self.app.screen, 650, 345)



            pygame.display.update()