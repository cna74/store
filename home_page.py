# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cna/home_page.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(606, 492)
        self.storage = QtWidgets.QPushButton(Dialog)
        self.storage.setGeometry(QtCore.QRect(340, 230, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.storage.setFont(font)
        self.storage.setIconSize(QtCore.QSize(16, 16))
        self.storage.setObjectName("storage")
        self.new_rent = QtWidgets.QPushButton(Dialog)
        self.new_rent.setGeometry(QtCore.QRect(180, 230, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.new_rent.setFont(font)
        self.new_rent.setIconSize(QtCore.QSize(16, 16))
        self.new_rent.setObjectName("new_rent")
        self.sell = QtWidgets.QPushButton(Dialog)
        self.sell.setGeometry(QtCore.QRect(440, 230, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sell.setFont(font)
        self.sell.setIconSize(QtCore.QSize(16, 16))
        self.sell.setObjectName("sell")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 90, 211, 231))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setWordWrap(False)
        self.label.setIndent(50)
        self.label.setObjectName("label")
        self.history = QtWidgets.QPushButton(Dialog)
        self.history.setGeometry(QtCore.QRect(80, 230, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.history.setFont(font)
        self.history.setIconSize(QtCore.QSize(16, 16))
        self.history.setObjectName("history")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(330, 90, 211, 231))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(False)
        self.label_2.setIndent(50)
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.history.raise_()
        self.new_rent.raise_()
        self.label_2.raise_()
        self.storage.raise_()
        self.sell.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.storage.setText(_translate("Dialog", "مشاهده"))
        self.new_rent.setText(_translate("Dialog", "جدید"))
        self.sell.setText(_translate("Dialog", "فروش"))
        self.label.setText(_translate("Dialog", "اجاره"))
        self.history.setText(_translate("Dialog", "سوابق"))
        self.label_2.setText(_translate("Dialog", "انبار"))

