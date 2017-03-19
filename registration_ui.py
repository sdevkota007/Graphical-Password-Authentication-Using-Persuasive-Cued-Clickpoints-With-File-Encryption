
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication, QDialog, QWidget, QMainWindow
from registration_2_ui import *
from mysql.connector import MySQLConnection, Error
import mysql.connector
from mysql.connector import *

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



class Ui_Registration(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def setupUi(self, Registration):
        Registration.setObjectName(_fromUtf8("Registration"))
        Registration.resize(370, 400)
        Registration.setMinimumSize(QtCore.QSize(370, 400))
        Registration.setMaximumSize(QtCore.QSize(370, 400))
       # Registration.setWindowModality(QApplication.ApplicationModal)      # self.setWindowModality(QtCore.Qt.WindowModal)
        self.userDetails = QtGui.QLabel(Registration)
        self.userDetails.setGeometry(QtCore.QRect(9, 70, 156, 24))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.userDetails.setFont(font)
        self.userDetails.setObjectName(_fromUtf8("userDetails"))
        self.label_first_name = QtGui.QLabel(Registration)
        self.label_first_name.setGeometry(QtCore.QRect(30, 146, 92, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_first_name.setFont(font)
        self.label_first_name.setObjectName(_fromUtf8("label_first_name"))
        self.lastName = QtGui.QLineEdit(Registration)
        self.lastName.setGeometry(QtCore.QRect(160, 174, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lastName.setFont(font)
        self.lastName.setText(_fromUtf8(""))
        self.lastName.setObjectName(_fromUtf8("lastName"))
        self.label_username = QtGui.QLabel(Registration)
        self.label_username.setGeometry(QtCore.QRect(30, 202, 87, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_username.setFont(font)
        self.label_username.setObjectName(_fromUtf8("label_username"))
        self.userName = QtGui.QLineEdit(Registration)
        self.userName.setGeometry(QtCore.QRect(160, 202, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.userName.setFont(font)
        self.userName.setText(_fromUtf8(""))
        self.userName.setEchoMode(QtGui.QLineEdit.Normal)
        self.userName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.userName.setReadOnly(False)
        self.userName.setObjectName(_fromUtf8("userName"))
        self.label_last_name = QtGui.QLabel(Registration)
        self.label_last_name.setGeometry(QtCore.QRect(30, 174, 90, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_last_name.setFont(font)
        self.label_last_name.setObjectName(_fromUtf8("label_last_name"))
        self.label_email_id = QtGui.QLabel(Registration)
        self.label_email_id.setGeometry(QtCore.QRect(30, 230, 77, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_email_id.setFont(font)
        self.label_email_id.setObjectName(_fromUtf8("label_email_id"))
        self.email = QtGui.QLineEdit(Registration)
        self.email.setGeometry(QtCore.QRect(160, 230, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.email.setFont(font)
        self.email.setText(_fromUtf8(""))
        self.email.setObjectName(_fromUtf8("email"))
        self.firstName = QtGui.QLineEdit(Registration)
        self.firstName.setGeometry(QtCore.QRect(160, 146, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.firstName.setFont(font)
        self.firstName.setText(_fromUtf8(""))
        self.firstName.setObjectName(_fromUtf8("firstName"))
        self.pushCancel = QtGui.QPushButton(Registration)
        self.pushCancel.setGeometry(QtCore.QRect(170, 308, 75, 23))
        self.pushCancel.setObjectName(_fromUtf8("pushCancel"))
        self.pushNext = QtGui.QPushButton(Registration)
        self.pushNext.setGeometry(QtCore.QRect(260, 308, 75, 23))
        self.pushNext.setObjectName(_fromUtf8("pushNext"))

        self.retranslateUi(Registration)
        QtCore.QObject.connect(self.pushCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Registration.close)
        QtCore.QMetaObject.connectSlotsByName(Registration)
        Registration.setTabOrder(self.firstName, self.lastName)
        Registration.setTabOrder(self.lastName, self.userName)
        Registration.setTabOrder(self.userName, self.email)
        Registration.setTabOrder(self.email, self.pushCancel)
        Registration.setTabOrder(self.pushCancel, self.pushNext)

    def retranslateUi(self, Registration):
        Registration.setWindowTitle(_translate("Registration", "Registration (step 1 of 2)", None))
        self.userDetails.setText(_translate("Registration", "Enter user details", None))
        self.label_first_name.setText(_translate("Registration", "First Name : ", None))
        self.label_username.setText(_translate("Registration", "Username : ", None))
        self.userName.setPlaceholderText(_translate("Registration", "choose a unique username", None))
        self.label_last_name.setText(_translate("Registration", "Last Name : ", None))
        self.label_email_id.setText(_translate("Registration", "Email ID : ", None))
        self.pushCancel.setText(_translate("Registration", "Cancel", None))
        self.pushNext.setText(_translate("Registration", "Next ->", None))


    @QtCore.pyqtSignature("on_pushNext_clicked()")
    def open_reg_window2(self):
        self.err = ""
        self.fname = str(self.firstName.text())
        self.lname = str(self.lastName.text())
        self.uname = str(self.userName.text())
        self.emailid = str(self.email.text())

        try:
            self.db = mysql.connector.connect(host="localhost", database = "python_mysql", user = "root", password = "2864")
            self.cursor = self.db.cursor()
            self.query = "INSERT into registration(Fname, Lname, Username, Email)""VALUES (%s,%s,%s,%s)"
            self.value = (self.fname, self.lname, self.uname, self.emailid)
            self.cursor.execute(self.query,self.value)
            self.db.commit()

        except Error as e:
            self.err = e

        finally:
            self.cursor.close()
            self.db.close()


        if not self.fname:
            QtGui.QMessageBox.warning(self, 'Dang it!', 'First Name Missing')
        elif not self.lname:
            QtGui.QMessageBox.warning(self, 'Dang it!', 'Last Name Missing')
        elif not self.uname:
            QtGui.QMessageBox.warning(self, 'Dang it!', 'Username Missing')
        elif not self.emailid:
            QtGui.QMessageBox.warning(self, 'Dang it!', 'Email ID Missing')
        elif self.err!="":
            QtGui.QMessageBox.information(self, 'Sorry!', 'Username not available!')
        else:
            QtGui.QMessageBox.information(self, 'Awesome!!', 'User Added SUCCESSFULLY!')
            self.close()
            self.registration_2 = Ui_Registration_2(self.uname)                              #"uname" is used to access database in registration 2
            self.registration_2.show()