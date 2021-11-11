from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import cv2 as cv
import time
from Traitement import *


class Ui_LettersRecognition(object):
    def __init__(self):
        self.tr = Traitement()
        self.path = ""

    def setupUi(self, LettersRecognition):
        LettersRecognition.setObjectName("LettersRecognition")
        LettersRecognition.resize(392, 269)
        self.centralwidget = QtWidgets.QWidget(LettersRecognition)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 0, 1, 2)
        self.multi = QtWidgets.QPushButton(self.centralwidget)
        self.multi.setObjectName("multi")
        self.gridLayout.addWidget(self.multi, 2, 2, 1, 1)
        self.DecisionTreeResult = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DecisionTreeResult.setFont(font)
        self.DecisionTreeResult.setText("")
        self.DecisionTreeResult.setObjectName("DecisionTreeResult")
        self.gridLayout.addWidget(self.DecisionTreeResult, 2, 3, 1, 1)
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setText("")
        self.img.setObjectName("img")
        self.gridLayout.addWidget(self.img, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 2, 1, 1)
        self.ExtraTreeResult = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ExtraTreeResult.setFont(font)
        self.ExtraTreeResult.setText("")
        self.ExtraTreeResult.setObjectName("ExtraTreeResult")
        self.gridLayout.addWidget(self.ExtraTreeResult, 3, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 4, 0, 2, 2)
        self.DecisionTreeExecution = QtWidgets.QLabel(self.centralwidget)
        self.DecisionTreeExecution.setText("")
        self.DecisionTreeExecution.setObjectName("DecisionTreeExecution")
        self.gridLayout.addWidget(self.DecisionTreeExecution, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.DecisionTreeRate = QtWidgets.QLabel(self.centralwidget)
        self.DecisionTreeRate.setText("")
        self.DecisionTreeRate.setObjectName("DecisionTreeRate")
        self.gridLayout.addWidget(self.DecisionTreeRate, 6, 2, 1, 1)
        self.ExtraTreeRate = QtWidgets.QLabel(self.centralwidget)
        self.ExtraTreeRate.setText("")
        self.ExtraTreeRate.setObjectName("ExtraTreeRate")
        self.gridLayout.addWidget(self.ExtraTreeRate, 7, 2, 1, 1)
        self.ExtraTreeExecution = QtWidgets.QLabel(self.centralwidget)
        self.ExtraTreeExecution.setText("")
        self.ExtraTreeExecution.setObjectName("ExtraTreeExecution")
        self.gridLayout.addWidget(self.ExtraTreeExecution, 7, 1, 1, 1)
        LettersRecognition.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LettersRecognition)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 392, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        LettersRecognition.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LettersRecognition)
        self.statusbar.setObjectName("statusbar")
        LettersRecognition.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(LettersRecognition)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(LettersRecognition)
        QtCore.QMetaObject.connectSlotsByName(LettersRecognition)

    def retranslateUi(self, LettersRecognition):
        _translate = QtCore.QCoreApplication.translate
        LettersRecognition.setWindowTitle(_translate("LettersRecognition", "MainWindow"))
        self.multi.setText(_translate("LettersRecognition", "DecisionTree"))
        self.pushButton_2.setText(_translate("LettersRecognition", "ExtraTree"))
        self.label_4.setText(_translate("LettersRecognition", "temps d\'execution"))
        self.label_5.setText(_translate("LettersRecognition", "test_success_rate"))
        self.label_2.setText(_translate("LettersRecognition", "DecisionTreeClassifier"))
        self.label_3.setText(_translate("LettersRecognition", "ExtraTreeClassifier"))
        self.menuFile.setTitle(_translate("LettersRecognition", "File"))
        self.actionOpen.setText(_translate("LettersRecognition", "Open"))

        self.actionOpen.triggered.connect(self.openImg)
        self.multi.clicked.connect(self.decisionTreeRecognize)
        self.pushButton_2.clicked.connect(self.extraTreeRecognize)

    #openImg() fonction pour ouvrir les images dans l'interface graphique
    def openImg(self):
        pathx = QFileDialog.getOpenFileName()[0]
        self.path = pathx
        pixmap = QtGui.QPixmap(pathx)
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        self.img.setPixmap(QtGui.QPixmap(pixmap4))

    #traiter l'image choisie
    def decisionTreeRecognize(self):
        img = cv.imread(self.path)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = cv.threshold(img,127,1,cv.THRESH_BINARY)[1]
        img = img.flatten()
        result = self.tr.decisionTreeClf.predict([img])
        self.DecisionTreeResult.setText(' '+result[0])
        return result

    def extraTreeRecognize(self):
        img = cv.imread(self.path)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = cv.threshold(img,127,1,cv.THRESH_BINARY)[1]
        img = img.flatten()
        result = self.tr.extraTreeClf.predict([img])
        self.ExtraTreeResult.setText(' '+result[0])
        return result

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LettersRecognition = QtWidgets.QMainWindow()
    ui = Ui_LettersRecognition()
    ui.setupUi(LettersRecognition)
    t1 = time.perf_counter()
    ui.tr.decisionTreeLearning()
    t2 = time.perf_counter()
    ui.DecisionTreeExecution.setText(str(t2-t1))
    t1 = time.perf_counter()
    ui.tr.extraTreeLearning()
    t2 = time.perf_counter()
    ui.ExtraTreeExecution.setText(str(t2-t1))
    ui.DecisionTreeRate.setText(str(ui.tr.decisionTreeSuccessRate()))
    ui.ExtraTreeRate.setText(str(ui.tr.extraTreeSuccessRate()))
    LettersRecognition.show()
    sys.exit(app.exec_())
