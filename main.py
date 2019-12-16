# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'u.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 800)
        self.img_holder = QtWidgets.QLabel(Dialog)
        self.img_holder.setGeometry(QtCore.QRect(0, 0, 1281, 811))
        self.img_holder.setText("")
        self.img_holder.setPixmap(QtGui.QPixmap("lion-4k-artistic-colorful-lf-1280x800.jpg"))
        self.img_holder.setScaledContents(True)
        self.img_holder.setObjectName("img_holder")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.speed = QtWidgets.QLCDNumber(self.centralwidget)
        self.speed.setGeometry(QtCore.QRect(500, 250, 291, 141))
        self.speed.setObjectName("speed")
        self.batterylvl = QtWidgets.QLCDNumber(self.centralwidget)
        self.batterylvl.setGeometry(QtCore.QRect(1040, 50, 221, 71))
        self.batterylvl.setObjectName("batterylvl")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(600, 210, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1040, 30, 111, 16))
        self.label_2.setObjectName("label_2")
        self.lighton = QtWidgets.QPushButton(self.centralwidget)
        self.lighton.setGeometry(QtCore.QRect(310, 410, 141, 61))
        self.lighton.setObjectName("lighton")
        self.lightoff = QtWidgets.QPushButton(self.centralwidget)
        self.lightoff.setGeometry(QtCore.QRect(860, 400, 141, 61))
        self.lightoff.setObjectName("lightoff")
        self.killswitch = QtWidgets.QCheckBox(self.centralwidget)
        self.killswitch.setGeometry(QtCore.QRect(1150, 180, 101, 21))
        self.killswitch.setObjectName("killswitch")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(30, 700, 93, 28))
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(160, 700, 93, 28))
        self.stop.setObjectName("stop")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 201, 16))
        self.label_3.setObjectName("label_3")
        self.totalrun = QtWidgets.QLCDNumber(self.centralwidget)
        self.totalrun.setGeometry(QtCore.QRect(10, 70, 221, 71))
        self.totalrun.setObjectName("totalrun")
        self.Horn = QtWidgets.QPushButton(self.centralwidget)
        self.Horn.setGeometry(QtCore.QRect(580, 480, 141, 61))
        self.Horn.setObjectName("Horn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.start.clicked.connect(self.clicked)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SPEED (KM/H):"))
        self.label_2.setText(_translate("MainWindow", "BATTERY LVL (%):"))
        self.lighton.setText(_translate("MainWindow", "Light ON"))
        self.lightoff.setText(_translate("MainWindow", "Light Off"))
        self.killswitch.setText(_translate("MainWindow", "Kill Switch"))
        self.start.setText(_translate("MainWindow", "START"))
        self.stop.setText(_translate("MainWindow", "STOP"))
        self.label_3.setText(_translate("MainWindow", "TOTAL DISTANCE COVERED (KM):"))
        self.Horn.setText(_translate("MainWindow", "Horn"))



    def clicked(self):
        if self.killswitch.isChecked():
            print('Checked')
            msg_c = QMessageBox()
            QMessageBox.about(msg_c, "START!", "Engine is powered on")
            #msg_c = QMessageBox()

        else:
             QMessageBox.about(widget, "ALERT!", "Check the killswitch it might be off")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    MainWindow.show()
    Dialog.show()
    sys.exit(app.exec_())
