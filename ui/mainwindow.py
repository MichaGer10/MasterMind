# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(823, 683)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.game_window = QtWidgets.QFrame(self.centralwidget)
        self.game_window.setMinimumSize(QtCore.QSize(550, 600))
        self.game_window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.game_window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.game_window.setObjectName("game_window")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.game_window)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.game_window)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.game_window)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.game_window, 0, QtCore.Qt.AlignLeft)
        self.feedback_window = QtWidgets.QFrame(self.centralwidget)
        self.feedback_window.setMinimumSize(QtCore.QSize(250, 600))
        self.feedback_window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.feedback_window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.feedback_window.setObjectName("feedback_window")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.feedback_window)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout.addWidget(self.feedback_window)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
