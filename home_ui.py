
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
import sys
import random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

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

class Ui_Home(QMainWindow):
    def __init__(self,cpx,cpy):
        self.cpx = cpx
        self.cpy = cpy
        self.passkey = self.genPasskey(self.cpx,self.cpy)
        QMainWindow.__init__(self)
        self.setupUi(self)

    def setupUi(self, Home):
        Home.setObjectName(_fromUtf8("Home"))
        Home.resize(300, 200)
        Home.setMinimumSize(QtCore.QSize(300, 200))
        Home.setMaximumSize(QtCore.QSize(300, 200))
        self.groupBoxE = QtGui.QGroupBox(Home)
        self.groupBoxE.setGeometry(QtCore.QRect(10, 10, 281, 71))
        self.groupBoxE.setTitle(_fromUtf8(""))
        self.groupBoxE.setObjectName(_fromUtf8("groupBoxE"))
        self.labelLock = QtGui.QLabel(self.groupBoxE)
        self.labelLock.setGeometry(QtCore.QRect(10, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelLock.setFont(font)
        self.labelLock.setObjectName(_fromUtf8("labelLock"))
        self.lineEditLock = QtGui.QLineEdit(self.groupBoxE)
        self.lineEditLock.setGeometry(QtCore.QRect(110, 10, 161, 20))
        self.lineEditLock.setReadOnly(False)
        self.lineEditLock.setObjectName(_fromUtf8("lineEditLock"))
        self.lockButton = QtGui.QPushButton(self.groupBoxE)
        self.lockButton.setGeometry(QtCore.QRect(240, 40, 31, 23))
        self.lockButton.setObjectName(_fromUtf8("lockButton"))
        self.groupBoxD = QtGui.QGroupBox(Home)
        self.groupBoxD.setGeometry(QtCore.QRect(10, 90, 281, 71))
        self.groupBoxD.setTitle(_fromUtf8(""))
        self.groupBoxD.setObjectName(_fromUtf8("groupBoxD"))
        self.labelUnlock = QtGui.QLabel(self.groupBoxD)
        self.labelUnlock.setGeometry(QtCore.QRect(10, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelUnlock.setFont(font)
        self.labelUnlock.setObjectName(_fromUtf8("labelUnlock"))
        self.lineEditUnlock = QtGui.QLineEdit(self.groupBoxD)
        self.lineEditUnlock.setGeometry(QtCore.QRect(110, 10, 161, 20))
        self.lineEditUnlock.setObjectName(_fromUtf8("lineEditUnlock"))
        self.unlockButton = QtGui.QPushButton(self.groupBoxD)
        self.unlockButton.setGeometry(QtCore.QRect(240, 40, 31, 23))
        self.unlockButton.setObjectName(_fromUtf8("unlockButton"))
        self.logoutButton = QtGui.QPushButton(Home)
        self.logoutButton.setGeometry(QtCore.QRect(110, 170, 75, 23))
        self.logoutButton.setObjectName(_fromUtf8("logoutButton"))

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)
        Home.setTabOrder(self.logoutButton, self.lineEditLock)
        Home.setTabOrder(self.lineEditLock, self.lockButton)
        Home.setTabOrder(self.lockButton, self.lineEditUnlock)
        Home.setTabOrder(self.lineEditUnlock, self.unlockButton)
        self.lockButton.clicked['bool'].connect(self.getFileforEnc)
        self.unlockButton.clicked['bool'].connect(self.getFileforDec)
        self.logoutButton.clicked['bool'].connect(self.close)


    def retranslateUi(self, Home):
        Home.setWindowTitle(_translate("Home", "Home", None))
        self.labelLock.setText(_translate("Home", "File to lock :", None))
        self.lineEditLock.setPlaceholderText(_translate("Home", "Enter filename with extension", None))
        self.lockButton.setText(_translate("Home", "OK", None))
        self.labelUnlock.setText(_translate("Home", "File to unlock :", None))
        self.lineEditUnlock.setPlaceholderText(_translate("Home", "Enter filename with extension", None))
        self.unlockButton.setText(_translate("Home", "OK", None))
        self.logoutButton.setText(_translate("Home", "Log Out", None))


    #a passkey is generated using the user's clickpoints
    '''example: if number of images is 3
                    clickpoints on x-cordinates , cpx = [168,193, 69]
                and clickpoints on y-cordinates , cpy = [185,120,151]
                then, passkey="16819369185120151"                  '''
    def genPasskey(self,cpx,cpy):
        passkey=""
        cplist = cpx+cpy                #cplist : list of clickpoints
        for i in cplist:
            passkey += str(i)
        return passkey


    #gets the filename and calls the encrypt function
    def getFileforEnc(self):
        try:
            self.filename = str(self.lineEditLock.text())
            self.encrypt(self.getKey(str(self.passkey)), self.filename)
            QMessageBox.information(self, 'Done','File Encrypted')
        except IOError as e:
            errorstr = str(e)
            QtGui.QMessageBox.warning(self, 'Sorry!', errorstr)
        finally:
            pass

    #gets the filename and calls the decrypt function
    def getFileforDec(self):
        try:
            self.filename = str(self.lineEditUnlock.text())
            self.decrypt(self.getKey(str(self.passkey)), self.filename)
            QMessageBox.information(self, 'Done','File Decrypted')
        except IOError as e:
            errorstr = str(e)
            QtGui.QMessageBox.warning(self, 'Sorry!', errorstr)
        finally:
            pass


    #encrypts the file if it exists
    def encrypt(self, key, filename):
        chunksize = 64*1024
        outputFile = "(encrypted)"+filename
        filesize = str(os.path.getsize(filename)).zfill(16)
        IV = Random.new().read(16)                     #initialization vector

        encryptor = AES.new(key, AES.MODE_CBC, IV)     #AES.MODE_CBC is the chain block cipher mode of AES encryption

        with open(filename, 'rb') as infile:
            with open(outputFile, 'wb') as outfile:
                outfile.write(filesize.encode('utf-8'))
                outfile.write(IV)

                while True:
                    chunk = infile.read(chunksize)

                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b' ' * (16 - (len(chunk) % 16))

                    outfile.write(encryptor.encrypt(chunk))


    #decrypts the file if it exists
    def decrypt(self, key, filename):
        chunksize = 64*1024
        outputFile = filename[11:]         #[11:] is to strip the "(encrypted)" characters at the front of the filename

        with open(filename, 'rb') as infile:
            filesize = int(infile.read(16))
            IV = infile.read(16)

            decryptor = AES.new(key, AES.MODE_CBC, IV)

            with open(outputFile, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunksize)

                    if len(chunk) == 0:
                        break

                    outfile.write(decryptor.decrypt(chunk))
                outfile.truncate(filesize)


    #generates a haskey from the passkey
    #SHA-256 is used for cryptographic hash algorithm (SHA : Secure Hash Algorithm)
    def getKey(self, passkey):
        hasher = SHA256.new(passkey.encode('utf-8'))
        return hasher.digest()


    #prompts the user when the logout button or the close button is pressed
    def closeEvent(self, event):
        quit_msg = "Are you sure you want to logout and exit?"
        reply = QtGui.QMessageBox.question(self, 'Message',
                         quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else :
            event.ignore()


# if __name__ == '__main__':
#     app = QtGui.QApplication(sys.argv)
#     mainWindow = Ui_Home([1,2,3],[4,5,6])
#     mainWindow.show()
#     sys.exit(app.exec())