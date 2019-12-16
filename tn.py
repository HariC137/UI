# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'un.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 800)
        self.img_holder = QtWidgets.QLabel(Dialog)
        self.img_holder.setGeometry(QtCore.QRect(0, 0, 1281, 811))
        self.img_holder.setText("")
        self.img_holder.setPixmap(QtGui.QPixmap("car-vehicle-white-sports-car-86993.jpg"))
        self.img_holder.setScaledContents(True)
        self.img_holder.setObjectName("img_holder")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(400, 490, 441, 71))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.TEXT = QtWidgets.QLabel(Dialog)
        self.TEXT.setGeometry(QtCore.QRect(400, 420, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.TEXT.setFont(font)
        self.TEXT.setObjectName("TEXT")
        self.TEXT.setStyleSheet('color : white')
        self.S = QtWidgets.QPushButton(Dialog)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.S.clicked.connect(self.click)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.TEXT.setText(_translate("Dialog", "E-TRAC LOADING.... :"))
        self.S.setText(_translate("Dialog", "START"))
        self.S.setText(_translate("Dialog", "START"))

    def boot(self):
        self.completed = 0
        while self.completed <100:
            self.completed += 0.0001
            self.progressBar.setValue(self.completed)
        self.S.setGeometry(QtCore.QRect(560, 590, 121, 41))
        self.S.setObjectName("S")


    def click(self):
        Dialog.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    ui.boot()
    sys.exit(app.exec_())
