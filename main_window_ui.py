# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication, QDialog, QWidget, QMainWindow
from registration_ui import *
from login import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


#----------------------------------------------------------------------------------------
#*******************************MAIN WINDOW USER INTERFACE*******************************
#----------------------------------------------------------------------------------------


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        #QtGui.QWidget.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(300, 350)
        MainWindow.setMouseTracking(True)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 60, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.pushLogin = QtGui.QPushButton(self.centralwidget)
        self.pushLogin.setObjectName(_fromUtf8("pushLogin"))
        self.gridLayout.addWidget(self.pushLogin, 1, 1, 1, 1)
        self.pushReg = QtGui.QPushButton(self.centralwidget)
        self.pushReg.setObjectName(_fromUtf8("pushReg"))
        self.gridLayout.addWidget(self.pushReg, 3, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 3)
        self.pushLogin.raise_()
        self.pushReg.raise_()
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Window", None))
        self.pushLogin.setText(_translate("MainWindow", "Login", None))
        self.pushReg.setText(_translate("MainWindow", "Registration", None))


#------------------------------PyQT signatures for login button and registartion button---------------------------------

    @QtCore.pyqtSignature("on_pushReg_clicked()")                                                                                          #opening Registration window 1st
    def open_reg_window1(self):
        self.registration = Ui_Registration()
        self.registration.show()

    @QtCore.pyqtSignature("on_pushLogin_clicked()")                                                                                          #opening Registration window 1st
    def open_login_window(self):
        self.login = Ui_Login()
        self.login.show()








