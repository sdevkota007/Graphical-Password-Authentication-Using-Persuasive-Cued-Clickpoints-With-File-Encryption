from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication, QDialog, QWidget, QMainWindow
from registration_2_ui import *
import sys

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

class Ui_Recovery(QMainWindow):
    def __init__(self,uname,rcode):
        self.uname = uname
        self.rcode = rcode          #rcode:recovery code
        QMainWindow.__init__(self)
        self.setupUi(self)


    def setupUi(self, Recovery):
        Recovery.setObjectName(_fromUtf8("Recovery"))
        Recovery.resize(393, 57)
        font = QtGui.QFont()
        font.setPointSize(12)
        Recovery.setFont(font)
        self.lineEdit = QtGui.QLineEdit(Recovery)
        self.lineEdit.setGeometry(QtCore.QRect(170, 20, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.recoveryLabel = QtGui.QLabel(Recovery)
        self.recoveryLabel.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.recoveryLabel.setObjectName(_fromUtf8("recoveryLabel"))
        self.submitButton = QtGui.QPushButton(Recovery)
        self.submitButton.setGeometry(QtCore.QRect(300, 20, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName(_fromUtf8("submitButton"))
        self.submitButton.clicked['bool'].connect(self.openRegistration)

        self.retranslateUi(Recovery)
        QtCore.QMetaObject.connectSlotsByName(Recovery)

    def retranslateUi(self, Recovery):
        Recovery.setWindowTitle(_translate("Recovery", "Form", None))
        self.recoveryLabel.setText(_translate("Recovery", "Enter recovery text : ", None))
        self.submitButton.setText(_translate("Recovery", "Submit", None))


#compares the user entered recovery text vs database recovery text
#successful comparision opens registration_2 allowing the user to select the images again
    def openRegistration(self):
        if self.lineEdit.text()==self.rcode:
            self.registration2 = Ui_Registration_2(self.uname)
            self.registration2.show()
            self.close()
        else:
            QMessageBox.information(self, 'Incorrect recovery text!','Please check your recovery text again.')



