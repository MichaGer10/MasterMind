import sys
from PyQt5.QtWidgets import *   #QApplication, QMainWindow
from qtpy import *              #QtWidgets
from mainwindow import *        #Ui_MasterMind
from PyQt5 import *             #QtCore, QtGui, QtWidgets
from helper_ui import Color
import game_class
from helper_game import Color


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MasterMind()
        self.ui.setupUi(self)
        self.show()
        self.colorsButtons = []
        self.colorsFeedback = []
        self.Turn=1
        self.newTry(self.Turn)
        self.connectColors()
        self.connectNewButtons(self.Turn)
        self.ui.LogIn.clicked.connect(lambda: self.nextTurn())
        self.ColorFeedBack(0,[1,-1,0,-1,1])
        self.ChoosenColor= ""
        self.colors = []
        
        #implement game
        self.game = game_class.Game()

    def nextTurn(self):
        allChoosen = True
        for button in self.colorsButtons[self.Turn - 1]:
            if button.styleSheet() == "background-color: rgb(255,255,255);":
                allChoosen = False
   
        if allChoosen == True:
            self.Turn+=1
            self.newTry(self.Turn)
            self.connectNewButtons(self.Turn)
      
    def connectColors(self):
        self.ui.Blue.clicked.connect(lambda: self.ColorChoice(self.ui.Blue.styleSheet()))
        self.ui.Red.clicked.connect(lambda: self.ColorChoice(self.ui.Red.styleSheet()))
        self.ui.Green.clicked.connect(lambda: self.ColorChoice(self.ui.Green.styleSheet()))
        self.ui.DeepGreen.clicked.connect(lambda: self.ColorChoice(self.ui.DeepGreen.styleSheet()))
        self.ui.Lila.clicked.connect(lambda: self.ColorChoice(self.ui.Lila.styleSheet()))
        self.ui.Yellow.clicked.connect(lambda: self.ColorChoice(self.ui.Yellow.styleSheet()))
        self.ui.Orange.clicked.connect(lambda: self.ColorChoice(self.ui.Orange.styleSheet()))
        self.ui.Turquish.clicked.connect(lambda: self.ColorChoice(self.ui.Turquish.styleSheet()))

    def ColorChoice(self,color):
        self.ChoosenColor = color
         

    def connectNewButtons(self, rowNumber):
        rowNumber -= 1
        self.colorsButtons[rowNumber][0].clicked.connect(lambda: self.colorsButtons[rowNumber][0].setStyleSheet(self.ChoosenColor))
        self.colorsButtons[rowNumber][1].clicked.connect(lambda: self.colorsButtons[rowNumber][1].setStyleSheet(self.ChoosenColor))
        self.colorsButtons[rowNumber][2].clicked.connect(lambda: self.colorsButtons[rowNumber][2].setStyleSheet(self.ChoosenColor))
        self.colorsButtons[rowNumber][3].clicked.connect(lambda: self.colorsButtons[rowNumber][3].setStyleSheet(self.ChoosenColor))
        self.colorsButtons[rowNumber][4].clicked.connect(lambda: self.colorsButtons[rowNumber][4].setStyleSheet(self.ChoosenColor))
    
              
            

    def getColorsRow(self, rowNumber):
        ColorsTry = []
        for columnButton in self.colorsButtons[rowNumber]:

            color = [int(color) for color in columnButton.styleSheet()[22:-2].split(",") if color.isdigit()]
            color = tuple(color)
            ColorsTry.append(Color(color).name)

        return ColorsTry

    def ColorFeedBack(self,rowNumber, feedbacks):
        feedbacks.sort(reverse=True)
        for idx, feedback in enumerate(feedbacks):
            if feedback == 2:
                self.colorsFeedback[rowNumber][idx].setStyleSheet("background-color: rgb(0,0,0);")
            elif feedback == 1:
                self.colorsFeedback[rowNumber][idx].setStyleSheet("background-color: rgb(255,255,255);")
            else:
                self.colorsFeedback[rowNumber][idx].setStyleSheet("background-color: transparent;")

    def newTry(self,columnNumber):
            colorsButtonTemp  = []
            colorsFeedbackTemp = []
            for x in range (1,11):
                if x >5:
                    colorsFeedbackTemp.append(self.createNewButtonsSmall(columnNumber,x))
                    
                else:
                    colorsButtonTemp.append(self.createNewButtonsBig(columnNumber,x))

            self.colorsButtons.append(colorsButtonTemp)
            self.colorsFeedback.append(colorsFeedbackTemp)

        
    def createNewButtonsSmall(self, rowNumber, columnNumber):
        Feld = QtWidgets.QPushButton(self.ui.frame_5)
        Feld.setMinimumSize(QtCore.QSize(20, 20))
        Feld.setMaximumSize(QtCore.QSize(20, 20))
        Feld.setStyleSheet("background-color: rgb(0,0,0)")
        Feld.setObjectName("FeedbackFeld" + str(rowNumber) + str(columnNumber))
        self.ui.gridLayout.addWidget(Feld, rowNumber, columnNumber, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        return Feld

    def createNewButtonsBig(self, rowNumber, columnNumber):
        Feld = QtWidgets.QPushButton(self.ui.frame_5)
        Feld.setMinimumSize(QtCore.QSize(100, 40))
        Feld.setStyleSheet("background-color: rgb(255,255,255);")
        Feld.setObjectName("Feld"+ str(rowNumber) + str(columnNumber))
        Feld.setText("Feld"+ str(rowNumber) + str(columnNumber))
        self.ui.gridLayout.addWidget(Feld, rowNumber, columnNumber, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        return Feld

