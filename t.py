# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'u.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.forward.pressed.connect(self.forward.showMenu)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
