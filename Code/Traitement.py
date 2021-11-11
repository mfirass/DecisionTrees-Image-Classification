import numpy as np
import cv2 as cv
from sklearn import tree, ensemble
import matplotlib.pyplot as plt

class Traitement(object):
    
    def __init__(self):
        #Le gain d'information est calcule selon l'entropie
        #Par defaut le parametre criterion est 'gini', cad Gini Impurity
        self.decisionTreeClf = tree.DecisionTreeClassifier(criterion='entropy', splitter='random', max_depth=None)
        self.extraTreeClf = ensemble.RandomForestClassifier()

        #Les sorties désirées pour notre exemples d'apprentissage
        self.d_learning = ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'E',
                           'F', 'F', 'G', 'G', 'H', 'H', 'I', 'I', 'I', 'I', 'I', 'J', 'J',
                           'K', 'K', 'L', 'L', 'M', 'M', 'N', 'N', 'O', 'O', 'O', 'P', 'P',
                           'Q', 'Q', 'R', 'R','S', 'S', 'T', 'T','U', 'U', 'U', 'V', 'V',
                           'W', 'W', 'X', 'X', 'Y', 'Y', 'Z', 'Z']

        #Sorties du test
        self.d_test = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E',
                       'F', 'F', 'G', 'H', 'H', 'I', 'I', 'J', 'J',
                       'K', 'L', 'M', 'M', 'N', 'N', 'O', 'O', 'P', 'P',
                       'Q', 'R','S', 'S', 'T', 'U', 'U', 'V',
                       'W', 'X', 'Y', 'Z']
    
    #import_img() fonction qui fait des pre-traitements sur les images de nos exemples (apprentissage ou test)
    def import_img(self, phase, n):
        imgs = []
        for i in range(1, n):
            img = "D:/Master SIR/TAAD/TPs/TAAD_TP05_FIRASS_Mohammed/images/"+phase+"/".__add__(i.__str__()).__add__(".png")
            img = cv.imread(img)
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            img = cv.threshold(img,127,1,cv.THRESH_BINARY)[1]
            imgs.append(img.flatten())
        return imgs

    #apprentissage basee sur la methode fit() du classificateur
    def decisionTreeLearning(self):
        images = self.import_img('apprentissage', 63)
        self.decisionTreeClf.fit(images, self.d_learning)

    def extraTreeLearning(self):
        images = self.import_img('apprentissage', 63)
        self.extraTreeClf.fit(images, self.d_learning)

    
    #faire des tests sur nos exemples du test et calculer le taux de reussite
    def decisionTreeSuccessRate(self):
        images = self.import_img('test', 42)
        count = 0
        for i in range(len(images)):
            result = self.decisionTreeClf.predict([images[i]])
            if result[0] == self.d_test[i]:
                count += 1
        return format((count/41)*100, ".2f")

    def extraTreeSuccessRate(self):
        images = self.import_img('test', 42)
        count = 0
        for i in range(len(images)):
            result = self.extraTreeClf.predict([images[i]])
            if result[0] == self.d_test[i]:
                count += 1
        return format((count/41)*100, ".2f")    