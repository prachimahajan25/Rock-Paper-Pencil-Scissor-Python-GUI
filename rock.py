# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rock.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import random
import time
from insc import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 542)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-6, 9, 851, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(85, 170, 255);\n"
                                 "font: 75 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 130, 231, 41))
        self.label_2.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 230, 111, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.buttonrock = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonrock.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.buttonrock.setObjectName("buttonrock")
        self.verticalLayout.addWidget(self.buttonrock)
        self.buttonrock.setEnabled(False)
        self.buttonrock.clicked.connect(self.brock)
        self.buttonpaper = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonpaper.setStyleSheet("background-color: rgb(255, 85, 255);")
        self.buttonpaper.setObjectName("buttonpaper")
        self.verticalLayout.addWidget(self.buttonpaper)
        self.buttonpaper.setEnabled(False)
        self.buttonpaper.clicked.connect(self.bpaper)
        self.buttonpencil = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonpencil.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.buttonpencil.setObjectName("buttonpencil")
        self.verticalLayout.addWidget(self.buttonpencil)
        self.buttonpencil.setEnabled(False)
        self.buttonpencil.clicked.connect(self.bpencil)
        self.buttonscissor = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonscissor.setStyleSheet("background-color: rgb(255, 85, 255);")
        self.buttonscissor.setObjectName("buttonscissor")
        self.verticalLayout.addWidget(self.buttonscissor)
        self.buttonscissor.setEnabled(False)
        self.buttonscissor.clicked.connect(self.bscissor)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 180, 231, 41))
        self.label_4.setStyleSheet("background-color: rgb(255, 85, 255);")
        self.label_4.setObjectName("label_4")
        self.labelcomp = QtWidgets.QLabel(self.centralwidget)
        self.labelcomp.setGeometry(QtCore.QRect(590, 225, 251, 181))
        self.labelcomp.setStyleSheet("background-color: rgb(255, 85, 255);\n"
                                     "font: 75 italic 12pt \"MS Sans Serif\";\n"
                                     "background-color: rgb(85, 170, 255);")
        self.labelcomp.setText("")
        self.labelcomp.setObjectName("labelcomp")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(590, 130, 251, 41))
        self.label_3.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(590, 180, 251, 41))
        self.label_5.setStyleSheet("background-color: rgb(255, 85, 255);")
        self.label_5.setObjectName("label_5")
        self.scoreplayer = QtWidgets.QLabel(self.centralwidget)
        self.scoreplayer.setGeometry(QtCore.QRect(270, 330, 141, 81))
        self.scoreplayer.setStyleSheet("background-color: rgb(255, 85, 255);")
        self.scoreplayer.setText("")
        self.scoreplayer.setObjectName("scoreplayer")
        self.scorecomp = QtWidgets.QLabel(self.centralwidget)
        self.scorecomp.setGeometry(QtCore.QRect(430, 330, 141, 81))
        self.scorecomp.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.scorecomp.setText("")
        self.scorecomp.setObjectName("scorecomp")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(430, 230, 141, 101))
        self.label_8.setStyleSheet("background-color: rgb(255, 85, 255);\n"
                                   "font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(270, 230, 141, 101))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_9.setPalette(palette)
        self.label_9.setStyleSheet("background-color: rgb(85, 170, 255);\n"
                                   "font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.labeltimer = QtWidgets.QLabel(self.centralwidget)
        self.labeltimer.setGeometry(QtCore.QRect(270, 130, 141, 91))
        self.labeltimer.setStyleSheet("background-color: rgb(255, 85, 255);")
        self.labeltimer.setText("30")
        self.labeltimer.setAlignment(QtCore.Qt.AlignCenter)
        self.labeltimer.setObjectName("labeltimer")
        self.labelplayer = QtWidgets.QLabel(self.centralwidget)
        self.labelplayer.setGeometry(QtCore.QRect(114, 235, 121, 171))
        self.labelplayer.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.labelplayer.setText("")
        self.labelplayer.setObjectName("labelplayer")
        # self.label_6 = QtWidgets.QLabel(self.centralwidget)
        # self.label_6.setGeometry(QtCore.QRect(134, 480, 51, 20))
        # self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(4, 420, 401, 61))
        self.label_7.setStyleSheet("background-color: rgb(255, 85, 255);")
        self.label_7.setObjectName("label_7")
        self.start = False
        self.pushButtonstart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonstart.setGeometry(QtCore.QRect(432, 127, 141, 91))
        self.pushButtonstart.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButtonstart.setObjectName("pushButtonstart")
        self.pushButtonstart.clicked.connect(self.startaction)
        self.resetbutton = QtWidgets.QPushButton(self.centralwidget)
        self.resetbutton.setGeometry(QtCore.QRect(430,420,141,61))
        self.resetbutton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.resetbutton.setText("Reset")
        self.resetbutton.clicked.connect(self.reset)
        self.insbutton = QtWidgets.QPushButton(self.centralwidget)
        self.insbutton.setGeometry(QtCore.QRect(630, 420, 141, 61))
        self.insbutton.setStyleSheet("background-color: rgb(255, 85, 255);")
        self.insbutton.setText("Instructions")
        self.insbutton.clicked.connect(self.inst)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.score_comp = 0
        self.score_player = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(1000)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def inst(self):
        self.ins = QtWidgets.QMainWindow()
        self.ui = Ui_ins()
        self.ui.setupUi(self.ins)
        self.ins.show()
    def startaction(self):
        self.start = True
        self.en()

    def handleTimer(self):
        if (self.start == True):

            value = int(self.labeltimer.text())
            if (value) > 0:
                (value) = (value) - 1
                self.labeltimer.setText(str(value))
                self.labeltimer.setAlignment(QtCore.Qt.AlignCenter)
            else:
                self.timer.stop()
                self.dis()

        self.check1()

    def reset(self):
        self.start = False
        self.labeltimer.setText("30")
        self.scoreplayer.setText("")
        self.scorecomp.setText("")
        self.labelplayer.setText("")
        self.labelcomp.setText("")
        self.label_7.setText("CLICK ON START TO PLAY!!!!")
        self.score_comp = 0
        self.score_player = 0
        self.pushButtonstart.setEnabled(True)
        self.buttonpaper.setEnabled(False)
        self.buttonrock.setEnabled(False)
        self.buttonpencil.setEnabled(False)
        self.buttonscissor.setEnabled(False)
        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(1000)

    def en(self):
        self.buttonrock.setEnabled(True)
        self.buttonpaper.setEnabled(True)
        self.buttonpencil.setEnabled(True)
        self.buttonscissor.setEnabled(True)

    def dis(self):
        self.buttonpaper.setEnabled(False)
        self.buttonrock.setEnabled(False)
        self.buttonpencil.setEnabled(False)
        self.buttonscissor.setEnabled(False)
        self.pushButtonstart.setEnabled(False)

    def check1(self):
        text = self.labeltimer.text()
        p1 = self.scoreplayer.text()
        p2 = self.scorecomp.text()
        if (text == "0"):

            if (int(p1) > int(p2)):
                self.label_7.setText("HURRAH!!!YOU WON")
                self.label_7.setAlignment(QtCore.Qt.AlignCenter)
            elif (int(p1) == int(p2)):
                self.label_7.setText("TIE!!!!!!")
                self.label_7.setAlignment(QtCore.Qt.AlignCenter)

            else:
                self.label_7.setText("BAD LUCK YOU LOOSE")
                self.label_7.setAlignment(QtCore.Qt.AlignCenter)

    def check(self):
        player = self.labelplayer.text()
        computer = self.labelcomp.text()

        if (player == "Rock"):
            if (computer == "Paper"):
                self.score_comp += 1
                self.scorecomp.setText(str(self.score_comp))
                self.scoreplayer.setText(str(self.score_player))
            else:
                if (computer == "Rock"):
                    self.scorecomp.setText(str(self.score_comp))
                    self.scoreplayer.setText(str(self.score_player))
                else:

                    self.score_player += 1
                    self.scorecomp.setText(str(self.score_comp))
                    self.scoreplayer.setText(str(self.score_player))

        if (player == "Paper"):
            if (computer == "Rock"):
                self.score_player += 1
                self.scorecomp.setText(str(self.score_comp))
                self.scoreplayer.setText(str(self.score_player))
            else:
                if (computer == "Paper"):
                    self.scorecomp.setText(str(self.score_comp))
                    self.scoreplayer.setText(str(self.score_player))
                else:

                    self.score_comp += 1
                    self.scorecomp.setText(str(self.score_comp))
                    self.scoreplayer.setText(str(self.score_player))
        if (player == "Pencil"):
            if (computer == "Paper"):
                self.score_player += 1
                self.scorecomp.setText(str(self.score_comp))
                self.scoreplayer.setText(str(self.score_player))
            else:
                if (computer == "Pencil"):
                    self.scorecomp.setText(str(self.score_comp))
                    self.scoreplayer.setText(str(self.score_player))
                else:

                    self.score_comp += 1
                    self.scorecomp.setText(str(self.score_comp))
                    self.scoreplayer.setText(str(self.score_player))
        if (player == "Scissor"):
            if (computer == "Rock"):
                self.score_comp += 1
                self.scorecomp.setText(str(self.score_comp))
                self.scoreplayer.setText(str(self.score_player))
            else:
                if (computer == "Scissor"):
                    self.scorecomp.setText(str(self.score_comp))
                    self.scoreplayer.setText(str(self.score_player))
                else:

                    self.score_player += 1
                    self.scorecomp.setText(str(self.score_comp))
                    self.scoreplayer.setText(str(self.score_player))

    def brock(self):
        self.labelplayer.setText("Rock")
        self.labelplayer.setAlignment(QtCore.Qt.AlignCenter)
        choices = ["Rock", "Paper", "Pencil", "Scissor"]
        comp = random.choice(choices)
        self.labelcomp.setText(comp)
        self.check()

    def bpaper(self):
        self.labelplayer.setText("Paper")
        self.labelplayer.setAlignment(QtCore.Qt.AlignCenter)
        choices = ["Rock", "Paper", "Pencil", "Scissor"]
        comp = random.choice(choices)
        self.labelcomp.setText(comp)
        self.check()

    def bpencil(self):
        self.labelplayer.setText("Pencil")
        self.labelplayer.setAlignment(QtCore.Qt.AlignCenter)
        choices = ["Rock", "Paper", "Pencil", "Scissor"]
        comp = random.choice(choices)
        self.labelcomp.setText(comp)
        self.check()

    def bscissor(self):
        self.labelplayer.setText("Scissor")
        self.labelplayer.setAlignment(QtCore.Qt.AlignCenter)
        choices = ["Rock", "Paper", "Pencil", "Scissor"]
        comp = random.choice(choices)
        self.labelcomp.setText(comp)
        self.check()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "                  Rock Paper Pencil Scissor Game"))
        self.label_2.setText(_translate("MainWindow", "              Player"))
        self.buttonrock.setText(_translate("MainWindow", "Rock"))
        self.buttonpaper.setText(_translate("MainWindow", "Paper"))
        self.buttonpencil.setText(_translate("MainWindow", "Pencil"))
        self.buttonscissor.setText(_translate("MainWindow", "Scissor"))
        self.label_4.setText(_translate("MainWindow", "   Player\'s Choice"))
        self.label_3.setText(_translate("MainWindow", "            Computer"))
        self.label_5.setText(_translate("MainWindow", "   Computer\'s Choice"))
        self.label_8.setText(_translate("MainWindow", "Computer\'s Score"))
        self.label_9.setText(_translate("MainWindow", "Player\'s Score"))
        # self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "CLICK ON START TO PLAY!!!!"))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButtonstart.setText(_translate("MainWindow", "Start"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
