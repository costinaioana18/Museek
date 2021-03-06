from math import sqrt

from sklearn import svm


class Prediction_Algorithm:
    def __init__(self, app):
        self.app = app
        self.click = False
        self.database_handler = self.app.database_handler
        self.trained_model = None

    def train_model(self):
        self.database_handler.database_init("users_progress")
        self.mycol = self.database_handler.set_collection(self.app.current_user)
        a = self.mycol.find()
        vectorX = []
        vectorY = []
        for instance in a:
            vectorX.append(
                [instance["piano_c"], instance["piano_l"], instance["piano_r"], instance["gen_c"], instance["chords"],
                 instance["topic"]])
            vectorY.append(instance["result"])
        clf = svm.SVC(probability=True)
        clf.fit(vectorX, vectorY)
        self.trained_model = clf
        # self.predict([0,0,0,1,0,1])

    def predict(self, type):
        a = self.trained_model.predict(type)
        print(a)

    def get_probabillity(self, type):
        a = self.trained_model.predict_proba(type)[:, 1]
        print(a)
        return a

    def gauss(self, x):
        g_x = (2.0 / (1.0 * sqrt(2.0 * 3.14))) * pow(2.718, -(x * x / 300.0))
        return 1 / g_x

    def get_biggest(self, type):
        a = self.get_probabillity(type)

        total = [10, 30, 20, 20, 30]
        done = [1, 3, 7, 5, 2]
        probs = [-1, -1, -1, -1, -1]

        for j in range(3):
            avg = 0.0
            count = 0
            for i in range(j * 11, 11 + 11 * j):
                avg += a[i]
                count += 1
            probs[j] = avg / count

        maxi = -999999.0
        maxi_el = None
        for i in range(5):
            probs[i] = probs[i] * self.gauss(2 * done[i] - total[i])
            if probs[i] > maxi:
                maxi = probs[i]
                maxi_el = i

        print(maxi_el)
        return maxi_el

