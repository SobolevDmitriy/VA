# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Front.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(464, 525)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.j_lbl = QtWidgets.QLabel(Form)
        self.j_lbl.setObjectName("j_lbl")
        self.gridLayout.addWidget(self.j_lbl, 0, 0, 1, 1)
        self.j_le = QtWidgets.QLineEdit(Form)
        self.j_le.setObjectName("j_le")
        self.gridLayout.addWidget(self.j_le, 0, 1, 1, 1)
        self.a_lbl = QtWidgets.QLabel(Form)
        self.a_lbl.setObjectName("a_lbl")
        self.gridLayout.addWidget(self.a_lbl, 1, 0, 1, 1)
        self.a_le = QtWidgets.QLineEdit(Form)
        self.a_le.setObjectName("a_le")
        self.gridLayout.addWidget(self.a_le, 1, 1, 1, 1)
        self.h_lbl = QtWidgets.QLabel(Form)
        self.h_lbl.setObjectName("h_lbl")
        self.gridLayout.addWidget(self.h_lbl, 2, 0, 1, 1)
        self.h_le = QtWidgets.QLineEdit(Form)
        self.h_le.setObjectName("h_le")
        self.gridLayout.addWidget(self.h_le, 2, 1, 1, 1)
        self.n_lbl = QtWidgets.QLabel(Form)
        self.n_lbl.setObjectName("n_lbl")
        self.gridLayout.addWidget(self.n_lbl, 3, 0, 1, 1)
        self.n_le = QtWidgets.QLineEdit(Form)
        self.n_le.setObjectName("n_le")
        self.gridLayout.addWidget(self.n_le, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.calc_btn = QtWidgets.QPushButton(Form)
        self.calc_btn.setObjectName("calc_btn")
        self.gridLayout_2.addWidget(self.calc_btn, 1, 0, 1, 1)
        self.phi_pw = PlotWidget(Form)
        self.phi_pw.setObjectName("phi_pw")
        self.gridLayout_2.addWidget(self.phi_pw, 2, 0, 1, 1)
        self.phiDer_pw = PlotWidget(Form)
        self.phiDer_pw.setObjectName("phiDer_pw")
        self.gridLayout_2.addWidget(self.phiDer_pw, 3, 0, 1, 1)
        self.buildGraphs_btn = QtWidgets.QPushButton(Form)
        self.buildGraphs_btn.setObjectName("buildGraphs_btn")
        self.gridLayout_2.addWidget(self.buildGraphs_btn, 4, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.table_tw = QtWidgets.QTableWidget(Form)
        self.table_tw.setObjectName("table_tw")
        self.table_tw.setColumnCount(0)
        self.table_tw.setRowCount(0)
        self.gridLayout_3.addWidget(self.table_tw, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.j_lbl.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-size:14pt; font-style:italic;\">J =</span></p></body></html>"))
        self.a_lbl.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-size:14pt; font-style:italic;\">a =</span></p></body></html>"))
        self.h_lbl.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-size:14pt; font-style:italic;\">h =</span></p></body></html>"))
        self.n_lbl.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-size:14pt; font-style:italic;\">N =</span></p></body></html>"))
        self.calc_btn.setText(_translate("Form", "Calculate"))
        self.buildGraphs_btn.setText(_translate("Form", "Build graphs"))

from pyqtgraph import PlotWidget
