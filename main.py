import sys
import math
import numpy as np
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTableWidgetItem, QMessageBox)
from front import Ui_Form


class MainWindow(Ui_Form):
    '''

    MainWidow class inherits appearance of the window from UI_Form
    and realizes behavior all widgets, Heune's method
    '''

    def __init__(self, form):
        self.setupUi(form)
        self.calc_btn.clicked.connect(self.calcslot)

    def heune(self, j):
        self.phi = np.zeros(self.n, dtype='float64')
        self.ksi = np.zeros(self.n, dtype='float64')
        for i in range(self.n-1):
            phi_star = self.phi[i] + self.h*self.ksi[i]
            ksi_star = self.ksi[i] + self.h*self.f(self.phi[i], self.ksi[i], j)
            phi_expr = (phi_star + self.phi[i])/2
            ksi_expr = (ksi_star + self.ksi[i])/2
            self.ksi[i+1] = self.ksi[i] + self.h*self.f(phi_expr, ksi_expr, j)
            self.phi[i+1] = self.phi[i] + self.h*ksi_expr
        avarage_ksi = ((self.phi[self.n-1] - self.phi[self.n//2])/
                       (self.time[self.n-1] - self.time[self.n//2]))
        return avarage_ksi

    def va(self):
        self.START = 0
        self.END = 3
        self.STEP = 0.01
        self.avarage_ksi = np.zeros(int((self.END-self.START)/self.STEP))
        self.j = np.arange(self.START, self.END,self.STEP)
        for i, j in enumerate(self.j):
            self.avarage_ksi[i] = self.heune(j)

    def f(self, phi, ksi, j):
        return -self.a * ksi - math.sin(phi) + j

    def drawplots(self):
        self.va()

        self.va_pw.getPlotItem().clear()
        self.va_pw.getPlotItem().setTitle("Volt-ampere characteristics graph")
        self.va_pw.getPlotItem().plot(self.j, self.avarage_ksi)
        self.va_pw.getPlotItem().showGrid(x=True, y=True)
        self.va_pw.getPlotItem().setLabel('left', "V'", units='j')
        self.va_pw.getPlotItem().setLabel('bottom', 'j')

    def drawtable(self):
        self.table_tw.setRowCount(self.j.size)
        self.table_tw.setColumnCount(2)
        self.table_tw.setHorizontalHeaderLabels(('j', 'V(j)'))
        for row in range(self.j.size):
            self.table_tw.setItem(row, 0, QTableWidgetItem(str(self.j[row])))
            self.table_tw.setItem(row, 1, QTableWidgetItem(str(self.avarage_ksi[row])))

    def calcslot(self):
        # reading data from lines
        while True:
            try:
                self.a = float(self.a_le.text())
                self.h = float(self.h_le.text())
                self.n = int(self.n_le.text())
                break
            except ValueError:
                err_msg = QMessageBox()
                err_msg.setWindowTitle('Error message')
                err_msg.setText('Only numbers required')
                err_msg.setStandardButtons(QMessageBox.Ok)
                err_msg.exec_()
                return
        self.time = np.arange(0, self.n * self.h, self.h)

        self.drawplots()
        self.drawtable()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    ui = MainWindow(window)
    window.show()
    sys.exit(app.exec_())