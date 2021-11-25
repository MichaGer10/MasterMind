import sys
from PyQt5.QtWidgets import *   #QApplication, QMainWindow
from qtpy import *              #QtWidgets
from mainwindow import *        #Ui_MasterMind
from PyQt5 import *             #QtCore, QtGui, QtWidgets
from helper import Color


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MasterMind()
        self.ui.setupUi(self)
        self.show()
        self.colorsButtons = []
        self.colorsFeedback = []
        self.newTry(1,1)
        self.ColorFeedBack(0,[1,-1,0,-1,1])

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
            if feedback == 1:
                self.colorsFeedback[rowNumber][idx].setStyleSheet("background-color: rgb(0,0,0);")
            elif feedback == 0:
                self.colorsFeedback[rowNumber][idx].setStyleSheet("background-color: rgb(255,255,255);")
            else:
                self.colorsFeedback[rowNumber][idx].setStyleSheet("background-color: transparent;")



    def newTry(self,columnNumber, LogIn):
        if LogIn==True:
            colorsButtonTemp  = []
            colorsFeedbackTemp = []
            LogIn = False
            for x in range (1,11):
                if x >5:
                    colorsFeedbackTemp.append(self.createNewButtonsSmall(columnNumber,x))
                    
                else:
                    colorsButtonTemp.append(self.createNewButtonsBig(columnNumber,x))

            self.colorsButtons.append(colorsButtonTemp)
            self.colorsFeedback.append(colorsFeedbackTemp)


        # for y in range(1,10):
        #     for x in range (1,11):
        #         if x >5:
        #             self.createNewButtonsSmall(y,x)
        #         else:
        #             self.createNewButtonsBig(y,x)

        
    def createNewButtonsSmall(self, rowNumber, columnNumber):
        Feld = QtWidgets.QPushButton(self.ui.frame_5)
        Feld.setMinimumSize(QtCore.QSize(20, 20))
        Feld.setMaximumSize(QtCore.QSize(20, 20))
        Feld.setStyleSheet("background-color: rgb(255,0,0);")
        Feld.setObjectName("FeedbackFeld" + str(rowNumber) + str(columnNumber))
        self.ui.gridLayout.addWidget(Feld, rowNumber, columnNumber, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        return Feld

    def createNewButtonsBig(self, rowNumber, columnNumber):
        Feld = QtWidgets.QPushButton(self.ui.frame_5)
        Feld.setMinimumSize(QtCore.QSize(100, 40))
        Feld.setStyleSheet("background-color: rgb(255,0,0);")
        Feld.setObjectName("Feld"+ str(rowNumber) + str(columnNumber))
        self.ui.gridLayout.addWidget(Feld, rowNumber, columnNumber, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        return Feld


if __name__ =="__main__":
    app= QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())






# app= QtWidgets.QApplication(sys.argv)
# window = QtWidgets.QMainWindow()



# #ui_window = Ui_MasterMind()
# ui_window.setupUi(window)
# window.setWindowTitle("MasterMind")
# window.show()
# self.ui_window.createNewButtons(0,0)
# # for y in range(0,8):
# #     for y in range(0,10):
# #         createnewButtons
# def createNewButtons(self, rowNumber, columnNumber):
#     self.Feld = QtWidgets.QPushButton(self.ui.frame_5)
#     self.Feld.setMinimumSize(QtCore.QSize(40, 40))
#     self.Feld.setStyleSheet("background-color: rgb(255, 0, 0);")
#     self.Feld.setObjectName("Feld")
#     self.ui.gridLayout.addWidget(self.Feld, rowNumber, columnNumber, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)

# sys.exit(app.exec())
