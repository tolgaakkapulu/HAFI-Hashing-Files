#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################################################################
# Writer    #  Tolga AKKAPULU                                     #
# Web       #  https://www.tolgaakkapulu.com                      #
#           #  https://www.parolaanalizi.com                      #
# LinkedIN  #  https://tr.linkedin.com/in/tolgaakkapulu           #
# GitHub    #  https://github.com/tolgaakkapulu                   #
###################################################################

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
import webbrowser
import os
import hashlib
import time
BLOCKSIZE = 2048

class MyThread(QThread):
    progress = pyqtSignal(int)

    def __init__(self, k):
        super().__init__()
        self.k = k

    def run(self):
        for i in range(self.k * 1001):
            sum([i * i for i in range(10)])
            ex = i // (self.k * 2)
            self.progress.emit(ex)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 430)
        MainWindow.setMinimumSize(QtCore.QSize(620, 430))
        MainWindow.setMaximumSize(QtCore.QSize(620, 430))
        app_icon = QtGui.QIcon()
        app_icon.addFile('HAFI.png', QtCore.QSize(32, 32))
        app.setWindowIcon(app_icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 621, 392))
        self.layoutWidget.setMinimumSize(QtCore.QSize(95, 0))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.textEdit_2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setMinimumSize(QtCore.QSize(350, 60))
        self.textEdit_2.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_8.addWidget(self.textEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(85, 55))
        self.pushButton.setMaximumSize(QtCore.QSize(85, 55))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setStyleSheet("color: rgb(153, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_8.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_8, 7, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setMinimumSize(QtCore.QSize(95, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.gridLayout.addLayout(self.verticalLayout_3, 7, 1, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.layoutWidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout.addWidget(self.line_10, 9, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 3, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_10.addWidget(self.line_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(-1, 1, 8, 5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.toolButton = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButton.setMinimumSize(QtCore.QSize(90, 22))
        self.toolButton.setMaximumSize(QtCore.QSize(90, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.toolButton.setFont(font)
        self.toolButton.setStyleSheet("color: rgb(153, 0, 0);")
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_6.addWidget(self.toolButton)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout_10, 1, 1, 1, 2)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_14.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(95, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_14.addWidget(self.label_5)
        self.gridLayout.addLayout(self.verticalLayout_14, 4, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 10, 1, 1, 2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(95, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.gridLayout.addLayout(self.verticalLayout_4, 3, 1, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setCheckable(True)
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_11.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_3.setEnabled(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_11.addWidget(self.radioButton_3)
        self.radioButton_1 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_1.setEnabled(False)
        self.radioButton_1.setObjectName("radioButton_1")
        self.horizontalLayout_11.addWidget(self.radioButton_1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_4.setEnabled(False)
        self.radioButton_4.setChecked(False)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_11.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_5.setEnabled(False)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout_11.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_6.setEnabled(False)
        self.radioButton_6.setObjectName("radioButton_6")
        self.horizontalLayout_11.addWidget(self.radioButton_6)
        self.gridLayout.addLayout(self.horizontalLayout_11, 5, 2, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(350, 30))
        self.progressBar.setMaximumSize(QtCore.QSize(350, 30))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_4.addWidget(self.progressBar)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setMinimumSize(QtCore.QSize(85, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(85, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(153, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 8, 2, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setMinimumSize(QtCore.QSize(95, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.gridLayout.addLayout(self.verticalLayout_5, 8, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setStyleSheet("color: rgb(9, 145, 6);")
        self.label_12.setText("")
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(95, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setStyleSheet("color: rgb(153, 0, 0);")
        self.label_13.setText("")
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        self.gridLayout.addLayout(self.horizontalLayout_9, 4, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setEnabled(False)
        self.textEdit.setMinimumSize(QtCore.QSize(350, 60))
        self.textEdit.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(85, 55))
        self.pushButton_2.setMaximumSize(QtCore.QSize(85, 55))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_2.setStyleSheet("color: rgb(153, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(95, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.label_3.linkActivated.connect(self.open_URL)
        self.toolButton.clicked.connect(self.get_file)
        self.pushButton_2.clicked.connect(self.save_hash)
        self.pushButton.clicked.connect(self.compare_hash)
        self.pushButton_3.clicked.connect(self.clear)

        self.radioButton_2.toggled.connect(lambda: self.btnstate(self.radioButton_2))
        self.radioButton_3.toggled.connect(lambda: self.btnstate(self.radioButton_3))
        self.radioButton_1.toggled.connect(lambda: self.btnstate(self.radioButton_1))
        self.radioButton_4.toggled.connect(lambda: self.btnstate(self.radioButton_4))
        self.radioButton_5.toggled.connect(lambda: self.btnstate(self.radioButton_5))
        self.radioButton_6.toggled.connect(lambda: self.btnstate(self.radioButton_6))

    def clear(self, MainWindow):
        Ui_MainWindow._translate = QtCore.QCoreApplication.translate
        self.label_8.setText("No File Selected")
        self.label_9.setText("0 bytes / Max: 4GB")
        self.radioDisable()
        self.toolButton.setEnabled(True)
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.textEdit.setText("")
        self.textEdit_2.setText("")
        self.textEdit.setEnabled(False)
        self.textEdit_2.setEnabled(False)
        self.progressBar.setValue(0)
        self.label_13.setText(Ui_MainWindow._translate("MainWindow",
                                                       "<html><head/><body><p><span style=\" font-weight:600;\"></span><span style=\" font-weight:600; color:#099106;\">All information was cleared.</span></p></body></html>"))

    def compare_hash(self, MainWindow):
        Ui_MainWindow._translate = QtCore.QCoreApplication.translate
        if self.textEdit.toPlainText() == self.textEdit_2.toPlainText().upper():
            self.label_13.setText(Ui_MainWindow._translate("MainWindow",
                                                           "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\"></span><span style=\" font-weight:600; color:#099106;\">Excellent, hash values are the same.</span></p></body></html>"))
        else:
            self.label_13.setText(Ui_MainWindow._translate("MainWindow",
                                                           "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\"></span><span style=\" font-weight:600; color:#990000;\">Unfortunately, hash values are not the same.</span></p></body></html>"))

    def save_hash(self, MainWindow):
        self.pushButton_2.setEnabled(False)
        Ui_MainWindow._translate = QtCore.QCoreApplication.translate
        file = open("HAFI.txt", 'a')
        file.write("----------HAFI - Hashing Files----------\n")
        file.write("Date & Time\t :  %s" % str(time.strftime("%c")))
        file.write("\nFile Path\t :  %s" % str(Ui_MainWindow.filePath))
        file.write("\nType of Hash\t :  %s" % str(Ui_MainWindow.hashtype))
        file.write("\nHash value\t :  %s\n" % str(Ui_MainWindow.hasher.hexdigest().upper()))
        file.close()
        self.label_13.setText(Ui_MainWindow._translate("MainWindow",
                                                       "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\"></span><span style=\" font-weight:600; color:#099106;\">Hash value was saved in the file \"HAFI.txt\".</span></p></body></html>"))

    def action(self):
        self.thread1 = MyThread(1)
        self.thread1.progress.connect(self.setFirstPbar)
        self.thread1.start()

    def setFirstPbar(self, value):
        self.firstStep = value
        self.progressBar.setValue(value)

    def radioEnable(self):
        self.radioButton_2.setEnabled(True)
        self.radioButton_3.setEnabled(True)
        self.radioButton_1.setEnabled(True)
        self.radioButton_4.setEnabled(True)
        self.radioButton_5.setEnabled(True)
        self.radioButton_6.setEnabled(True)

    def radioDisable(self):
        self.radioButton_2.setEnabled(False)
        self.radioButton_3.setEnabled(False)
        self.radioButton_1.setEnabled(False)
        self.radioButton_4.setEnabled(False)
        self.radioButton_5.setEnabled(False)
        self.radioButton_6.setEnabled(False)

    def get_file(self):
        self.radioEnable()
        self.textEdit.clear()
        self.textEdit.setText("")
        self.textEdit_2.setText("")
        self.toolButton.setEnabled(False)
        self.pushButton_3.setEnabled(True)
        self.label_13.setText("Please, choose a type of hash")

        filePath = str(QFileDialog.getOpenFileName(options=QFileDialog.ShowDirsOnly))
        Ui_MainWindow.filePath = filePath[2:-19]
        Ui_MainWindow.fileName = filePath[2:-19].split("/")
        self.label_8.setText(Ui_MainWindow.fileName[-1])
        digits = []
        value = int(os.path.getsize(Ui_MainWindow.filePath))
        while value: value, b = divmod(value, 1000); digits.insert(0, b)

        if int(os.path.getsize(Ui_MainWindow.filePath)) > 4294967296:
            self.label_13.setText("Ooops. File size is over 4GB.")
            self.textEdit.setEnabled(False)
            self.textEdit_2.setEnabled(False)
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(False)
            self.radioDisable()

        number = ""
        for i in range(len(digits)):
            number = number + str(digits[i]) + "."
        self.label_9.setText(number[0:-1] + " bytes")

    def btnstate(self, b):
        self.label_13.setText("")
        self.progressBar.setValue(0)
        self.pushButton_2.setEnabled(True)
        self.textEdit.setEnabled(True)
        self.textEdit_2.setEnabled(True)
        self.pushButton.setEnabled(True)

        if b.text() == "MD5":
            if b.isChecked() == True:
                Ui_MainWindow.hasher = hashlib.md5()
                self.action()
                self.hashing()
                Ui_MainWindow.hashtype = "MD5"
                time.sleep(1)
                self.textEdit.setText(Ui_MainWindow.hasher.hexdigest().upper())

        if b.text() == "SHA1":
            if b.isChecked() == True:
                Ui_MainWindow.hasher = hashlib.sha1()
                self.action()
                self.hashing()
                Ui_MainWindow.hashtype = "SHA1"
                time.sleep(1)
                self.textEdit.setText(Ui_MainWindow.hasher.hexdigest().upper())

        if b.text() == "SHA224":
            if b.isChecked() == True:
                Ui_MainWindow.hasher = hashlib.sha224()
                self.action()
                self.hashing()
                Ui_MainWindow.hashtype = "SHA224"
                time.sleep(1)
                self.textEdit.setText(Ui_MainWindow.hasher.hexdigest().upper())

        if b.text() == "SHA256":
            if b.isChecked() == True:
                Ui_MainWindow.hasher = hashlib.sha256()
                self.action()
                self.hashing()
                Ui_MainWindow.hashtype = "SHA256"
                time.sleep(1)
                self.textEdit.setText(Ui_MainWindow.hasher.hexdigest().upper())

        if b.text() == "SHA384":
            if b.isChecked() == True:
                Ui_MainWindow.hasher = hashlib.sha384()
                self.action()
                self.hashing()
                Ui_MainWindow.hashtype = "SHA384"
                time.sleep(1)
                self.textEdit.setText(Ui_MainWindow.hasher.hexdigest().upper())

        if b.text() == "SHA512":
            if b.isChecked() == True:
                Ui_MainWindow.hasher = hashlib.sha512()
                self.action()
                self.hashing()
                Ui_MainWindow.hashtype = "SHA512"
                time.sleep(1)
                self.textEdit.setText(Ui_MainWindow.hasher.hexdigest().upper())

    def hashing(self):
        self.textEdit_2.setText("")
        with open(Ui_MainWindow.filePath, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                Ui_MainWindow.hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        self.textEdit.setText(Ui_MainWindow.hasher.hexdigest().upper())

    def open_URL(self):
        webbrowser.open("https://www.tolgaakkapulu.com")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HAFI - Hashing Files"))
        self.pushButton.setText(_translate("MainWindow", "Compare"))
        self.label_10.setText(_translate("MainWindow", "Compare with"))
        self.label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#990000;\">Hashing Files with HAFI</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Generate and verify the MD5/SHA1/SHA224/SHA256/SHA384/SHA512 hash of a file it."))
        self.toolButton.setText(_translate("MainWindow", "Choose..."))
        self.label_5.setText(_translate("MainWindow", "File Size"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">HAFI v1.0 - </span><a href=\"https://www.tolgaakkapulu.com\"><span style=\" font-weight:600; text-decoration: underline; color:#990000;\">https://www.tolgaakkapulu.com</span></a><span style=\" font-weight:600;\"> - Tolga Akkapulu - 2017</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "File Name"))
        self.radioButton_2.setText(_translate("MainWindow", "MD5"))
        self.radioButton_3.setText(_translate("MainWindow", "SHA1"))
        self.radioButton_1.setText(_translate("MainWindow", "SHA224"))
        self.radioButton_4.setText(_translate("MainWindow", "SHA256"))
        self.radioButton_5.setText(_translate("MainWindow", "SHA384"))
        self.radioButton_6.setText(_translate("MainWindow", "SHA512"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.label_11.setText(_translate("MainWindow", "Process"))
        self.label_8.setText(_translate("MainWindow", "No File Selected"))
        self.label_6.setText(_translate("MainWindow", "Type of Hash"))
        self.label_9.setText(_translate("MainWindow", "0 bytes / Max: 4GB"))
        self.pushButton_2.setText(_translate("MainWindow", "Save"))
        self.label_7.setText(_translate("MainWindow", "Hash of File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
