from sklearn import svm

class Prediction_Algorithm:
    def __init__(self, app):
        self.app = app
        self.click= False
        self.database_handler = self.app.database_handler
        self.trained_model=None

    def train_model(self):
        self.database_handler.database_init("users_progress")
        self.mycol = self.database_handler.set_collection(self.app.current_user)
        a=self.mycol.find()
        vectorX=[]
        vectorY=[]
        for instance in a:
            vectorX.append([instance["piano_c"],instance["piano_l"],instance["piano_r"],instance["gen_c"],instance["chords"],instance["topic"]])
            vectorY.append(instance["result"])
        #print(vectorX)
        #print(vectorY)
        clf = svm.SVC(probability=True)
        clf.fit(vectorX, vectorY)
        self.trained_model=clf
        #self.predict([0,0,0,1,0,1])



    def predict(self,type):
        a = self.trained_model.predict(type)
        print(a)

    def get_probabillity(self,type):
        a=self.trained_model.predict_proba(type)[:,1]
        print(a)
        return a
