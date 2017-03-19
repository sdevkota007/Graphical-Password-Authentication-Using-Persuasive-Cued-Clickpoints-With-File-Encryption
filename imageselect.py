from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import mysql.connector
from mysql.connector import *
from mysql.connector import MySQLConnection,Error
from registration_2_ui import *
from image_retrieve import *
import sys
import os

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


class Ui_imageselect(QMainWindow):
    def __init__(self,num ):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.currentbutton = 0
        self.num = num         ####                                   #get number of images ie 'num' from registration 2
        self.status = []       ####                                  #list of click status of 12 buttons
        self.clicks = 0
        self.imageRetrieve = imageRetrieve()

        for i in range(12):
            self.status.append(False)



    def setupUi(self, imageselect):
        imageselect.setObjectName(_fromUtf8("imageselect"))
        imageselect.resize(617, 594)
        imageselect.setWindowModality(QtCore.Qt.ApplicationModal)


        #********************************extracting 12 images from Database and saving them in a list**************************

        #*****************************************fetching address from db*********************************************************************
        # self.imageList = []
        # try:
        #     self.db=mysql.connector.connect(host="localhost", database="python_mysql",user="root",password="2864")
        #     self.cursor=self.db.cursor()
        #     for i in range(12):
        #         self.cursor.execute("select * from image_data where img_id=%s",(i+1,))
        #         rows=self.cursor.fetchone()
        #         #print(rows[1])
        #         self.imageList.append(rows[1])
        #         #print(self.imageList[i])
        #     imageList = self.imageList
        # except Error as e:
        #     print(e)
        #
        # finally:
        #     self.cursor.close()
        #     self.db.close()

        #*****************************************retrieving images from db and using the address*****************************
        #create images here.
        self.imageList = []
        for i in range(12):
            self.imageList.append(str(i+1)+".png")

        #****************************************************creating 12 icons for 12 push buttons****************************
        iconList = []
        for i in range(12):
            iconList.append(QtGui.QIcon())
            iconList[i].addPixmap(QtGui.QPixmap(_fromUtf8(self.imageList[i])), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        #****************************************************creating 12 push buttons*****************************************
        self.imageButton = []
        shiftx=0                                       #difference between the positions on x-direction for buttons on 1st row
        shifty=0                                       #difference between the positions on x-direction for buttons on 2nd row
        shiftz=0                                       #difference between the positions on x-direction for buttons on 3rd row
        shiftu=0                                       #difference between the positions on x-direction for buttons on 4th row

        for i in range(12):
            self.img = QtGui.QPushButton(imageselect)
            if ((i==0) or (i==1) or (i==2)):                                    #setting geometry for 3 pushbuttons img[0],img[1] and img[2]
                self.img.setGeometry(QtCore.QRect(10+shiftx, 20, 170, 120))
                shiftx=shiftx+185
            if ((i==3) or (i==4) or (i==5)):                                    #setting geometry for 3 pushbuttons img[3],img[4] and img[5]
                self.img.setGeometry(QtCore.QRect(10+shifty, 150, 170, 120))
                shifty=shifty+185
            if ((i==6) or (i==7) or (i==8)):                                    #setting geometry for 3 pushbuttons img[6],img[7] and img[8]
                self.img.setGeometry(QtCore.QRect(10+shiftz, 280, 170, 120))
                shiftz=shiftz+185
            if ((i==9) or (i==10) or (i==11)):                                  #setting geometry for 3 pushbuttons img[9],img[10] and img[11]
                self.img.setGeometry(QtCore.QRect(10+shiftu, 410, 170, 120))
                shiftu=shiftu+185
            self.img.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.img.setText(_fromUtf8(""))
            self.img.setIcon(iconList[i])
            self.img.setIconSize(QtCore.QSize(180, 100))
            self.img.setCheckable(True)
            self.img.setFlat(True)
            self.img.setObjectName(_fromUtf8("img1"))
            self.imageButton.append(self.img)
        #----------------------------------------------------------------------------------------------------------------------#


        self.open = QtGui.QPushButton(imageselect)
        self.open.setGeometry(QtCore.QRect(390, 540, 101, 31))
        self.open.setDisabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.open.setFont(font)
        self.open.setObjectName(_fromUtf8("open"))
        self.verticalScrollBar = QtGui.QScrollBar(imageselect)
        self.verticalScrollBar.setGeometry(QtCore.QRect(600, 0, 20, 591))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        self.retranslateUi(imageselect)

        self.open.clicked['bool'].connect(self.closeImageSelect)

        #**************try button clicked option using loop or something similar********************
        # for j in range(12):
        #     print(j)
        #     self.currentbutton = j
        #     self.imageButton[j].clicked['bool'].connect(self.updateState)

        self.imageButton[0].clicked['bool'].connect(self.updateStatus0)
        self.imageButton[1].clicked['bool'].connect(self.updateStatus1)
        self.imageButton[2].clicked['bool'].connect(self.updateStatus2)
        self.imageButton[3].clicked['bool'].connect(self.updateStatus3)
        self.imageButton[4].clicked['bool'].connect(self.updateStatus4)
        self.imageButton[5].clicked['bool'].connect(self.updateStatus5)
        self.imageButton[6].clicked['bool'].connect(self.updateStatus6)
        self.imageButton[7].clicked['bool'].connect(self.updateStatus7)
        self.imageButton[8].clicked['bool'].connect(self.updateStatus8)
        self.imageButton[9].clicked['bool'].connect(self.updateStatus9)
        self.imageButton[10].clicked['bool'].connect(self.updateStatus10)
        self.imageButton[11].clicked['bool'].connect(self.updateStatus11)


        QtCore.QMetaObject.connectSlotsByName(imageselect)

    #******************updateStatus changes the status of the button,true if clicked and false if double clicked************
    def updateStatus0(self,stat):
        self.status[0] = stat
        self.check(stat)

    def updateStatus1(self,stat):
        self.status[1] = stat
        self.check(stat)

    def updateStatus2(self,stat):
        self.status[2] = stat
        self.check(stat)

    def updateStatus3(self,stat):
        self.status[3] = stat
        self.check(stat)

    def updateStatus4(self,stat):
        self.status[4] = stat
        self.check(stat)

    def updateStatus5(self,stat):
        self.status[5] = stat
        self.check(stat)

    def updateStatus6(self,stat):
        self.status[6] = stat
        self.check(stat)

    def updateStatus7(self,stat):
        self.status[7] = stat
        self.check(stat)

    def updateStatus8(self,stat):
        self.status[8] = stat
        self.check(stat)

    def updateStatus9(self,stat):
        self.status[9] = stat
        self.check(stat)

    def updateStatus10(self,stat):
        self.status[10] = stat
        self.check(stat)

    def updateStatus11(self,stat):
        self.status[11] = stat
        self.check(stat)

    #*********check func increases 'clicks' if button is single clicked, decreases 'clicks' if button is double ckicked*****
    def check(self,stat):
        if stat==True:
            self.clicks = self.clicks+1
        else:
            self.clicks = self.clicks-1
        if self.clicks == self.num:
            self.disableUnckecked(True)
        else:
            self.disableUnckecked(False)

    #*************************************if image limit is reached, disable unckecked images*******************************
    def disableUnckecked(self,bl):
        for k in range(12):
            if self.status[k]==False:
                self.imageButton[k].setDisabled(bl)
                self.open.setEnabled(bl)

    def retranslateUi(self, imageselect):
        imageselect.setWindowTitle(_translate("imageselect", "Form", None))
        self.open.setText(_translate("imageselect", "Open", None))

    def closeImageSelect(self):
        self.close()



