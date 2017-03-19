# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration_2.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication, QDialog, QWidget, QMainWindow
from random import *
from registration_ui import *

from imageselect import *
import sys
import json
from mysql.connector import Error, MySQLConnection
import mysql.connector
import image_retrieve
from image_retrieve import *

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


class Ui_Registration_2(QMainWindow):
    ax=randint(0,240)                    #generating random values for button 1 and storing final coodinate positions
    ay=randint(0,215)
    posax = 20+ax
    posay = 170+ay

    bx=randint(0,240)                    #generating random values for button 2 and storing final coodinate positions
    by=randint(0,215)
    posbx = 320+bx
    posby = 170+by

    cx=randint(0,540)                    #generating random values for button 3 and storing final coodinate positions
    cy=randint(0,65)
    poscx = 20+cx
    poscy = 445+cy

    imagenum = 0                         #nth image in 'num' number of images
    tvalue = 40                          #tolerance value
    num = 3                              #number of images to be selected (default 3)
    userImages = []                                #list of images selected by the user



    def __init__(self,uname):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.uname = uname
        self.imgList = []
        self.imgRetrieve = imageRetrieve()
        self.imgRetrieve.main()


    def setupUi(self, Registration_2):
        Registration_2.setObjectName("Registration_2")
        Registration_2.resize(800, 600)
        Registration_2.setMinimumSize(QtCore.QSize(800, 600))
        Registration_2.setMaximumSize(QtCore.QSize(800, 600))
        #Registration_2.setWindowModality(QtCore.Qt.ApplicationModal)
        self.databaseRadio = QtGui.QRadioButton(Registration_2)
        self.databaseRadio.setGeometry(QtCore.QRect(40, 80, 261, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.databaseRadio.setFont(font)
        self.databaseRadio.setObjectName("databaseRadio")
        self.galleryRadio = QtGui.QRadioButton(Registration_2)
        self.galleryRadio.setGeometry(QtCore.QRect(430, 80, 261, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.galleryRadio.setFont(font)
        self.galleryRadio.setObjectName("galleryRadio")
        self.shuffleButton = QtGui.QPushButton(Registration_2)
        self.shuffleButton.setGeometry(QtCore.QRect(630, 460, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.shuffleButton.setFont(font)
        self.shuffleButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.shuffleButton.setMouseTracking(False)
        self.shuffleButton.setObjectName("shuffleButton")

        self.uselessbutton=QtGui.QPushButton(Registration_2)
        self.uselessbutton.setGeometry(QtCore.QRect(250,340,151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.uselessbutton.setFont(font)
        self.uselessbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.numberOfImages = QtGui.QLabel(Registration_2)
        self.numberOfImages.setGeometry(QtCore.QRect(40, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.numberOfImages.setFont(font)
        self.numberOfImages.setObjectName("numberOfImages")
        self.comboBox = QtGui.QComboBox(Registration_2)
        self.comboBox.setGeometry(QtCore.QRect(170, 30, 41, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        # self.comboBox.addItem("")
        # self.comboBox.addItem("")
        # self.comboBox.addItem("")
        self.regImage = QtGui.QLabel(Registration_2)
        self.regImage.setGeometry(QtCore.QRect(20, 170, 600, 400))
        self.regImage.setAutoFillBackground(False)
        self.regImage.setFrameShape(QtGui.QFrame.WinPanel)
        self.regImage.setFrameShadow(QtGui.QFrame.Sunken)
        self.regImage.setLineWidth(5)
        self.regImage.setText("")
        self.regImage.setObjectName("regImage")
        self.regImage.setScaledContents(True)
        self.selectImage = QtGui.QLabel(Registration_2)
        self.selectImage.setGeometry(QtCore.QRect(90, 110, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectImage.setFont(font)
        self.selectImage.setObjectName("selectImage")
        self.selectImage.setDisabled(True)
        self.selectButton = QtGui.QToolButton(Registration_2)
        self.selectButton.setGeometry(QtCore.QRect(190, 110, 25, 19))
        self.selectButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selectButton.setObjectName("selectButton")
        self.selectButton.setDisabled(True)
        self.groupBox = QtGui.QGroupBox(Registration_2)
        self.groupBox.setGeometry(QtCore.QRect(630, 180, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.toleranceSlider = QtGui.QSlider(self.groupBox)
        self.toleranceSlider.setGeometry(QtCore.QRect(0, 20, 149, 22))
        self.toleranceSlider.setMinimum(20)
        self.toleranceSlider.setMaximum(60)
        self.toleranceSlider.setSliderPosition(40)
        self.toleranceSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toleranceSlider.setOrientation(QtCore.Qt.Horizontal)
        self.toleranceSlider.setObjectName("toleranceSlider")
        self.browseImage = QtGui.QLabel(Registration_2)
        self.browseImage.setGeometry(QtCore.QRect(470, 110, 111, 21))
        self.browseImage.setDisabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.browseImage.setFont(font)
        self.browseImage.setObjectName("browseImage")
        self.browseButton = QtGui.QToolButton(Registration_2)
        self.browseButton.setGeometry(QtCore.QRect(580, 110, 25, 19))
        self.browseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browseButton.setObjectName("browseButton")
        self.browseButton.setDisabled(True)


        #click button 1
        self.clickpoint1 = QtGui.QPushButton(Registration_2)
        self.clickpoint1.setGeometry(QtCore.QRect(self.posax,self.posay,self.tvalue,self.tvalue))
        self.clickpoint1.setMinimumSize(QtCore.QSize(20, 20))
        self.clickpoint1.setMaximumSize(QtCore.QSize(60, 60))
        self.clickpoint1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.clickpoint1.setMouseTracking(True)
        self.clickpoint1.setText("")
        self.clickpoint1.setObjectName("clickpoint1")
        self.clickpoint1.setStyleSheet(_fromUtf8("\n"
                                        "background-color: rgb(0, 0, 255,80);\n"
                                        "\n"
                                        "border: 2px solid red;"))

        #click button 2
        self.clickpoint2 = QtGui.QPushButton(Registration_2)
        self.clickpoint2.setGeometry(QtCore.QRect(320+self.bx,170+self.by,self.tvalue,self.tvalue))
        self.clickpoint2.setMinimumSize(QtCore.QSize(20, 20))
        self.clickpoint2.setMaximumSize(QtCore.QSize(60, 60))
        self.clickpoint2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.clickpoint2.setMouseTracking(True)
        self.clickpoint2.setText("")
        self.clickpoint2.setObjectName("clickpoint2")
        self.clickpoint2.setStyleSheet(_fromUtf8("\n"
                                        "background-color: rgb(255, 255, 0,80);\n"
                                        "\n"
                                        "border: 2px solid red;"))

        #click button 3
        self.clickpoint3 = QtGui.QPushButton(Registration_2)
        self.clickpoint3.setGeometry(QtCore.QRect(20+self.cx,445+self.cy,self.tvalue,self.tvalue))
        self.clickpoint3.setMinimumSize(QtCore.QSize(20, 20))
        self.clickpoint3.setMaximumSize(QtCore.QSize(60, 60))
        self.clickpoint3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.clickpoint3.setMouseTracking(True)
        self.clickpoint3.setText("")
        self.clickpoint3.setObjectName("clickpoint3")
        self.finishButton = QtGui.QPushButton(Registration_2)
        self.finishButton.setGeometry(QtCore.QRect(630, 530, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.finishButton.setFont(font)
        self.finishButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.finishButton.setObjectName("finishButton")
        self.clickpoint3.setStyleSheet(_fromUtf8("\n"
                                        "background-color: rgb(255, 255, 0,80);\n"
                                        "\n"
                                        "border: 2px solid red;"))


#*******initially the clickpoints and the clickarea(label) are disabled***********************************
        self.clickpoint1.hide()
        self.clickpoint2.hide()
        self.clickpoint3.hide()
        self.regImage.setDisabled(True)
        self.uselessbutton.hide()


        self.databaseRadio.raise_()
        self.galleryRadio.raise_()
        self.shuffleButton.raise_()
        self.numberOfImages.raise_()
        self.comboBox.raise_()
        self.regImage.raise_()
        self.selectImage.raise_()
        self.selectButton.raise_()
        self.finishButton.raise_()
        self.groupBox.raise_()
        self.browseImage.raise_()
        self.browseButton.raise_()
        self.clickpoint1.raise_()
        self.clickpoint2.raise_()
        self.clickpoint3.raise_()
        self.finishButton.raise_()
        self.uselessbutton.raise_()

        self.retranslateUi(Registration_2)
        self.uselessbutton.clicked['bool'].connect(self.enableClickArea)
        self.databaseRadio.clicked['bool'].connect(self.selectImage.setEnabled)
        self.databaseRadio.clicked['bool'].connect(self.selectButton.setEnabled)
        self.galleryRadio.clicked['bool'].connect(self.browseImage.setEnabled)
        self.galleryRadio.clicked['bool'].connect(self.browseButton.setEnabled)
        self.databaseRadio.clicked['bool'].connect(self.browseImage.setDisabled)
        self.databaseRadio.clicked['bool'].connect(self.browseButton.setDisabled)
        self.galleryRadio.clicked['bool'].connect(self.selectImage.setDisabled)
        self.galleryRadio.clicked['bool'].connect(self.selectButton.setDisabled)
        self.shuffleButton.clicked['bool'].connect(self.clickpointsshuffle)
        QtCore.QObject.connect(self.finishButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.registrationClose)
        self.toleranceSlider.valueChanged['int'].connect(self.settolerance)
        self.clickpoint1.clicked['bool'].connect(self.saveclickpoint1)
        self.clickpoint2.clicked['bool'].connect(self.saveclickpoint2)
        self.clickpoint3.clicked['bool'].connect(self.saveclickpoint3)
        self.comboBox.activated['int'].connect(self.getNumber)

        QtCore.QMetaObject.connectSlotsByName(Registration_2)

    def retranslateUi(self, Registration_2):
        _translate = QtCore.QCoreApplication.translate
        Registration_2.setWindowTitle(_translate("Registration_2", "Registration (step 2 of 2)"))
        self.databaseRadio.setText(_translate("Registration_2", "Choose Images from system database"))
        self.galleryRadio.setText(_translate("Registration_2", "Browse Images from gallery"))
        self.shuffleButton.setText(_translate("Registration_2", "Shuffle Click-points"))
        self.numberOfImages.setText(_translate("Registration_2", "Number of Images : "))
        self.comboBox.setItemText(0, _translate("Registration_2", "3"))
        self.comboBox.setItemText(1, _translate("Registration_2", "4"))
        self.comboBox.setItemText(2, _translate("Registration_2", "5"))
        # self.comboBox.setItemText(3, _translate("Registration_2", "6"))
        # self.comboBox.setItemText(4, _translate("Registration_2", "7"))
        # self.comboBox.setItemText(5, _translate("Registration_2", "8"))
        self.selectImage.setText(_translate("Registration_2", "Select Images : "))
        self.selectButton.setText(_translate("Registration_2", "..."))
        self.groupBox.setTitle(_translate("Registration_2", "Click-point Tolerance"))
        self.browseImage.setText(_translate("Registration_2", "Browse Images :"))
        self.browseButton.setText(_translate("Registration_2", "..."))
        self.finishButton.setText(_translate("Registration_2", "Finish"))
        self.uselessbutton.setText(_translate("Registration_2", "Show Images"))


    def getNumber(self,a):
        self.num=a+3                                                   #num is the number of images selected by the user

    # def disableClickArea(self):
    #     self.clickpoint1.hide()
    #     self.clickpoint2.hide()
    #     self.clickpoint3.hide()
    #     self.regImage.setDisabled(True)

    def enableClickArea(self):
        if self.num==self.imageselect.clicks:
            self.clickpoint1.show()
            self.clickpoint2.show()
            self.clickpoint3.show()
            self.regImage.setEnabled(True)
            #self.uselessbutton.show()
            self.nextimage()
        else:
            QtGui.QMessageBox.warning(self, 'Sorry!', 'Select '+str(self.num)+' images first.')

    def mysqlData(self):
        try:
            if self.imagenum==1:
                self.query=("UPDATE registration set img1=%s,Nimages=%s, tolerance = %s where Username=%s")
            if self.imagenum==2:
                self.query=("UPDATE registration set img2=%s,Nimages=%s, tolerance = %s where Username=%s")
            if self.imagenum==3:
                self.query=("UPDATE registration set img3=%s,Nimages=%s, tolerance = %s where Username=%s")
            if self.imagenum==4:
                self.query=("UPDATE registration set img4=%s,Nimages=%s, tolerance = %s where Username=%s")
            if self.imagenum==5:
                self.query=("UPDATE registration set img5=%s,Nimages=%s, tolerance = %s where Username=%s")
            if self.imagenum==6:
                self.query=("UPDATE registration set img6=%s,Nimages=%s, tolerance = %s where Username=%s")
            if self.imagenum==7:
                self.query=("UPDATE registration set img7=%s,Nimages=%s, tolerance = %s where Username=%s")
            if self.imagenum==8:
                self.query=("UPDATE registration set img8=%s,Nimages=%s, tolerance = %s where Username=%s")


            self.db=mysql.connector.connect(host="localhost", database="python_mysql",user="root",password="2864")
            self.cursor=self.db.cursor()
            self.args=json.dumps([self.imgList[self.imagenum-1],self.val,self.val2])
            self.temp=(self.args,self.num,self.tvalue,self.uname)
            self.cursor=self.db.cursor()
            self.cursor.execute(self.query,self.temp)
            self.db.commit()

        except Error as e:
            print(e)

        finally:
            self.cursor.close()
            self.db.close()


    def saveclickpoint1(self,token):
        #save position of button 1 to database
        self.val=self.posax-20
        self.val2=self.posay-170
        self.mysqlData()
        self.nextimage()
        self.toleranceSlider.setDisabled(True)
        self.groupBox.setDisabled(True)

    def saveclickpoint2(self,token):
        #save position of button 2 to database
        self.val=self.posbx-20
        self.val2=self.posby-170
        self.mysqlData()
        self.nextimage()
        self.toleranceSlider.setDisabled(True)
        self.groupBox.setDisabled(True)

    def saveclickpoint3(self,token):
        #save position of button 3 to database
        self.val=self.poscx-20
        self.val2=self.poscy-170
        self.mysqlData()
        self.nextimage()
        self.toleranceSlider.setDisabled(True)
        self.groupBox.setDisabled(True)

    def nextimage(self):
        for i in range(12):
            if self.status[i] == True:
                self.userImages.append(self.imageList[i])
                self.imgList.append(i+1)                                # example : imagelist = [2,4,5]


        if self.imagenum <self.num:
            self.regImage.setPixmap(QtGui.QPixmap(self.userImages[self.imagenum]))
            self.imagenum = self.imagenum + 1
        else:
            self.clickpoint1.hide()
            self.clickpoint2.hide()
            self.clickpoint3.hide()
        self.clickpointsshuffle()
        self.shutdown()

        # try:
        #     self.db=mysql.connector.connect(host="localhost", database="python_mysql",user="root",password="2864")
        #     self.cursor=self.db.cursor()
        #
        #     self.cursor.execute("SELECT * from registration where Username = %s",(self.uname,))
        #     rows=self.cursor.fetchone()
        #     print(rows)
        #     for i in range(self.num):
        #          name = (rows[7+i])
        #          print(name[0])
        # except Error as e:
        #      print(e)
        #
        # finally:
        #     print('x')
        #      # self.cursor.close()
        #      # self.db.close()

        # for i in range(self.num):
        #     self.cursor.execute("select * from image_data where img_id=%s",(i+1,))
        #     rows=self.cursor.fetchone()
        #     print(rows[1])
        #     self.imgstr.append(rows[1])
        #     print(self.imgstr[i])

    def settolerance(self,a):
        self.tvalue = a
        self.clickpoint1.setGeometry(QtCore.QRect(self.posax,self.posay,self.tvalue,self.tvalue))
        self.clickpoint2.setGeometry(QtCore.QRect(self.posbx,self.posby,self.tvalue,self.tvalue))
        self.clickpoint3.setGeometry(QtCore.QRect(self.poscx,self.poscy,self.tvalue,self.tvalue))

    def clickpointsshuffle(self):
        self.ax=randint(0,240)
        self.ay=randint(0,215)
        self.posax = 20+self.ax
        self.posay = 170+self.ay
        self.clickpoint1.setGeometry(QtCore.QRect(20+self.ax,170+self.ay,self.tvalue,self.tvalue))
        self.bx=randint(0,240)
        self.by=randint(0,215)
        self.posbx = 320+self.bx
        self.posby = 170+self.by
        self.clickpoint2.setGeometry(QtCore.QRect(320+self.bx,170+self.by,self.tvalue,self.tvalue))
        self.cx=randint(0,540)
        self.cy=randint(0,65)
        self.poscx = 20+self.cx
        self.poscy = 445+self.cy
        self.clickpoint3.setGeometry(QtCore.QRect(20+self.cx,445+self.cy,self.tvalue,self.tvalue))
        #print(self.posax,self.posay)

    def shutdown(self):
        self.comboBox.setDisabled(True)
        self.selectImage.setDisabled(True)
        self.databaseRadio.setDisabled(True)
        self.galleryRadio.setDisabled(True)
        self.browseButton.setDisabled(True)
        self.browseImage.setDisabled(True)
        self.selectButton.setDisabled(True)
        self.numberOfImages.setDisabled(True)
        self.uselessbutton.hide()


    @QtCore.pyqtSignature("on_selectButton_clicked()")
    def open_reg_window1(self):
        self.imageselect = Ui_imageselect(self.num)
        self.imageselect.show()
        self.status=self.imageselect.status
        self.imageList = self.imageselect.imageList
        #self.click = self.imageselect.clicks
        self.uselessbutton.show()

    def registrationClose(self):
            self.imgRetrieve.remove_images()
            self.close()

