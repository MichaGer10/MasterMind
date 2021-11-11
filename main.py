import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets

from ui.mainwindow import Ui_MainWindow

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Master Mind")
        self.pushButtons = []

        
        self.addMove(0)
       
       
        

        # self.pushButtons[0][0].setStyleSheet("background-color: green")
        # self.pushButtons[5][0].setStyleSheet("background-color: blue")

        # self.frame_move = QtWidgets.QFrame(self.ui.game_window)
        # self.frame_move.setMinimumSize(QtCore.QSize(550, 60))
        # self.frame_move.setObjectName("move1")

        # self.pButton = QtWidgets.QPushButton(self.frame_move)
        # self.pButton2 = QtWidgets.QPushButton(self.frame_move)
        # self.pButton.setObjectName("pushButton1")
        # self.pButton2.setObjectName("pushButton2")
        # self.testHLayout = QtWidgets.QHBoxLayout(self.frame_move)
        # self.testHLayout.setObjectName("testHLayout")
        # self.testHLayout.addWidget(self.pButton)
        # self.testHLayout.addWidget(self.pButton2)
        

    def addMove(self, moveNumber):
        # frame_move = QtWidgets.QFrame(self.ui.game_window)
        # frame_move.setMinimumSize(QtCore.QSize(550, 60))
        # frame_move.setObjectName("move" + str(moveNumber))
        # testHLayout = QtWidgets.QHBoxLayout(frame_move)
        # testHLayout.setObjectName("testHLayout" + str(moveNumber))
        # self.ui.verticalLayout.addWidget(frame_move, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        pushButtonsmove = []

        for pbNumber in range(0, 5):
            pButton = QtWidgets.QPushButton(self.ui.frame)
            pButton.setObjectName("pushButton" + str(moveNumber) + "_" + str(pbNumber))
            self.ui.gridLayout.addWidget(pButton, moveNumber, pbNumber, 0, 0)
            pushButtonsmove.append(pButton)
        
        self.pushButtons.append(pushButtonsmove)



window = MainWindow()

window.show()

sys.exit(app.exec())
