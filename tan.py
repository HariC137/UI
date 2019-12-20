# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'u.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QMessageBox
import RPi.GPIO as GPIO
import time
import serial
#from firebase import firebase
import random

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 500)
        Dialog.setWindowIcon(QtGui.QIcon("electric-car.png"))
        Dialog.setWindowTitle("E-TRAC Start-up")
        self.img_holder = QtWidgets.QLabel(Dialog)
        self.img_holder.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.img_holder.setText("")
        self.img_holder.setPixmap(QtGui.QPixmap("car-vehicle-white-sports-car-86993.jpg"))
        self.img_holder.setScaledContents(True)
        self.img_holder.setObjectName("img_holder")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(200, 290, 441, 71))
        self.progressBar.setProperty("value", 50)
        self.progressBar.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.TEXT = QtWidgets.QLabel(Dialog)
        self.TEXT.setGeometry(QtCore.QRect(200, 240, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.TEXT.setFont(font)
        self.TEXT.setObjectName("TEXT")
        self.TEXT.setStyleSheet('color : white')
        self.S = QtWidgets.QPushButton(Dialog)
        self.S.setGeometry(QtCore.QRect(370, 370, 121, 41))
        self.S.setObjectName("S")
        self.S.clicked.connect(self.click)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.TEXT.setText(_translate("Dialog", "E-TRAC LOADING.... : "))
        self.S.setText(_translate("Dialog", "START"))


    def boot(self):
        self.completed = 0
        while self.completed <100:
            self.completed += 0.0001
            #time.sleep(1)
            self.progressBar.setValue(self.completed)
            #time.sleep(1)
        self.S.setGeometry(QtCore.QRect(370, 370, 121, 41))
        self.S.setObjectName("S")


    def click(self):
        Dialog.close()
        MainWindow.show()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        self.timer = QTimer()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.speed = QtWidgets.QLCDNumber(self.centralwidget)
        self.speed.setGeometry(QtCore.QRect(240, 190, 291, 71))
        self.speed.setObjectName("speed")
        self.batterylvl = QtWidgets.QLCDNumber(self.centralwidget)
        self.batterylvl.setGeometry(QtCore.QRect(500, 50, 221, 71))
        self.batterylvl.setObjectName("batterylvl")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 140, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 30, 211, 16))
        self.label_2.setObjectName("label_2")
        self.lighton = QtWidgets.QPushButton(self.centralwidget)
        self.lighton.setGeometry(QtCore.QRect(240, 270, 141, 61))
        self.lighton.setObjectName("lighton")
        self.lightoff = QtWidgets.QPushButton(self.centralwidget)
        self.lightoff.setGeometry(QtCore.QRect(390, 270, 141, 61))
        self.lightoff.setObjectName("lightoff")
        self.killswitch = QtWidgets.QCheckBox(self.centralwidget)
        self.killswitch.setGeometry(QtCore.QRect(680, 140, 101, 21))
        self.killswitch.setObjectName("killswitch")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(20, 420, 93, 28))
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(150, 420, 93, 28))
        self.stop.setObjectName("stop")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 441, 16))
        self.label_3.setObjectName("label_3")
        self.totalrun = QtWidgets.QLCDNumber(self.centralwidget)
        self.totalrun.setGeometry(QtCore.QRect(10, 50, 221, 71))
        self.totalrun.setObjectName("totalrun")
        self.Horn = QtWidgets.QPushButton(self.centralwidget)
        self.Horn.setGeometry(QtCore.QRect(310, 340, 141, 61))
        self.Horn.setObjectName("Horn")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 50, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(540, 190, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(730, 50, 61, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setWindowIcon(QtGui.QIcon("electric-car.png"))
        self.forward = QtWidgets.QPushButton(self.centralwidget)
        self.forward.setGeometry(QtCore.QRect(620, 300, 93, 28))
        self.forward.setObjectName("forward")
        self.left = QtWidgets.QPushButton(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(570, 330, 93, 28))
        self.left.setObjectName("left")
        self.right = QtWidgets.QPushButton(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(670, 330, 93, 28))
        self.right.setObjectName("right")
        self.reverse = QtWidgets.QPushButton(self.centralwidget)
        self.reverse.setGeometry(QtCore.QRect(620, 360, 93, 28))
        self.reverse.setObjectName("reverse")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 190, 191, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # self.forward.pressed.connect(self.on_press)
        # self.forward.released.connect(self.on_release)
        self.start.pressed.connect(self.clicked)
        #self.timer.timeout.connect(self.every_second_while_pressed)
        #self.start.released.connect(self.loop)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SPEED :"))
        self.label_2.setText(_translate("MainWindow", "BATTERY LVL :"))
        self.lighton.setText(_translate("MainWindow", "Light ON"))
        self.lightoff.setText(_translate("MainWindow", "Light Off"))
        self.killswitch.setText(_translate("MainWindow", "Kill Switch"))
        self.start.setText(_translate("MainWindow", "START"))
        self.stop.setText(_translate("MainWindow", "STOP"))
        self.label_3.setText(_translate("MainWindow", "TOTAL DISTANCE COVERED :"))
        self.Horn.setText(_translate("MainWindow", "Horn"))
        self.label_4.setText(_translate("MainWindow", "KM"))
        self.label_5.setText(_translate("MainWindow", "KM/H"))
        self.label_6.setText(_translate("MainWindow", "%"))
        self.forward.setText(_translate("MainWindow", "FORWARD"))
        self.left.setText(_translate("MainWindow", "LEFT"))
        self.right.setText(_translate("MainWindow", "RIGHT"))
        self.reverse.setText(_translate("MainWindow", "REVERSE"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Manual"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Remote"))

    def on_release(self):
        self.timer.stop()

    def on_press(self):
        self.timer.start(100)


    def every_second_while_pressed(self):
        print('click')
        #self.loop()

    def loop(self):
        data = GPIO.input(23)
        print(data)
        # while GPIO.input(18) :
        #   ser = serial.Serial ("/dev/ttyS0",9600)
        #   data = ser.readline(3)
        #   d = int(data)
        #   d = d / 10
        #   d = d / 3.2
        #   d = int(d)
        #   self.speed.display(d)
        #   time.sleep(1)
        #   ser.close()
        #   #self.speed.display(random.randint(0,100))


    def clicked(self):
        if self.killswitch.isChecked():
            print('Checked')
            msg_1 = QMessageBox()
            msg_1.setIcon(QMessageBox.Information)
            msg_1.setWindowIcon(QtGui.QIcon("electric-car.png"))
            msg_1.setWindowTitle("ALERT!!")
            msg_1.setText("The engine has started")
            print(self.comboBox.currentText())

            x = msg_1.exec_()
            self.loop()

        else:
            msg_2 = QMessageBox()
            msg_2.setIcon(QMessageBox.Warning)
            msg_2.setWindowIcon(QtGui.QIcon("electric-car.png"))
            msg_2.setWindowTitle("ALERT!!")
            msg_2.setText("The killswitch might be off!")

            x = msg_2.exec_()

if __name__ == "__main__":
    import sys

    #firebase = firebase.FirebaseApplication('https://e-trac-5d530.firebaseio.com/', None)
    app = QtWidgets.QApplication(sys.argv)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.IN)
    Dialog = QtWidgets.QDialog()
    u_i = Ui_Dialog()
    u_i.setupUi(Dialog)
    Dialog.show()
    u_i.boot()

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    sys.exit(app.exec_())
    #app = QtWidgets.QApplication(sys.argv)
