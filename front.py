# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(615, 551)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.table_tw = QtWidgets.QTableWidget(Form)
        self.table_tw.setMinimumSize(QtCore.QSize(201, 0))
        self.table_tw.setObjectName("table_tw")
        self.table_tw.setColumnCount(0)
        self.table_tw.setRowCount(0)
        self.gridLayout_3.addWidget(self.table_tw, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.n_lbl = QtWidgets.QLabel(Form)
        self.n_lbl.setObjectName("n_lbl")
        self.gridLayout.addWidget(self.n_lbl, 2, 0, 1, 1)
        self.a_le = QtWidgets.QLineEdit(Form)
        self.a_le.setObjectName("a_le")
        self.gridLayout.addWidget(self.a_le, 0, 1, 1, 1)
        self.n_le = QtWidgets.QLineEdit(Form)
        self.n_le.setObjectName("n_le")
        self.gridLayout.addWidget(self.n_le, 2, 1, 1, 1)
        self.h_lbl = QtWidgets.QLabel(Form)
        self.h_lbl.setObjectName("h_lbl")
        self.gridLayout.addWidget(self.h_lbl, 1, 0, 1, 1)
        self.a_lbl = QtWidgets.QLabel(Form)
        self.a_lbl.setObjectName("a_lbl")
        self.gridLayout.addWidget(self.a_lbl, 0, 0, 1, 1)
        self.h_le = QtWidgets.QLineEdit(Form)
        self.h_le.setObjectName("h_le")
        self.gridLayout.addWidget(self.h_le, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.calc_btn = QtWidgets.QPushButton(Form)
        self.calc_btn.setObjectName("calc_btn")
        self.gridLayout_2.addWidget(self.calc_btn, 1, 0, 1, 1)
        self.va_pw = PlotWidget(Form)
        self.va_pw.setObjectName("va_pw")
        self.gridLayout_2.addWidget(self.va_pw, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.n_lbl.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-size:14pt; font-style:italic;\">N =</span></p></body></html>"))
        self.h_lbl.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-size:14pt; font-style:italic;\">h =</span></p></body></html>"))
        self.a_lbl.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-size:14pt; font-style:italic;\">a =</span></p></body></html>"))
        self.calc_btn.setText(_translate("Form", "Calculate"))

from pyqtgraph import PlotWidget
