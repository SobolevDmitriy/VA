import sys
import math
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from front import Ui_Form


class MainWindow(Ui_Form):
    '''

    MainWidow class inherits appearance of the window from UI_Form
    and realizes behavior all widgets, Heune's method
    '''

    def __init__(self, form):
        self.setupUi(form)
        self.calc_btn.clicked.connect(self.calcslot)

    def readdata(self):
        try:
            self.j = float(self.j_le.text())
            self.a = float(self.a_le.text())
            self.h = float(self.h_le.text())
            self.n = int(self.n_le.text())
        except ValueError:
            print('Only numbers required')


    def heune(self):
        self.phi = np.zeros(self.n, dtype='float64')
        self.ksi = np.zeros(self.n, dtype='float64')
        for i in range(self.n-1):

            phi_star = self.phi[i] + self.h*self.ksi[i]
            ksi_star = self.ksi[i] + self.h*self.f(self.phi[i], self.ksi[i])

            phi_expr = (phi_star + self.phi[i])/2
            ksi_expr = (ksi_star + self.ksi[i])/2

            self.ksi[i+1] = self.ksi[i] + self.h*self.f(phi_expr, ksi_expr)
            self.phi[i+1] = self.phi[i] + self.h*ksi_expr

    def f(self, phi, ksi):
        return -self.a * ksi - math.sin(phi) + self.j

    def drawplots(self):
        self.heune()
        self.time = np.arange(0, self.n*self.h, self.h)

        self.phi_pw.getPlotItem().clear()
        self.phi_pw.getPlotItem().setTitle("Phi graph")
        self.phi_pw.getPlotItem().plot(self.time, self.phi)
        self.phi_pw.getPlotItem().showGrid(x=True, y=True)
        self.phi_pw.getPlotItem().setLabel('left', 'Phi', units='t')
        self.phi_pw.getPlotItem().setLabel('bottom', 't')

        self.ksi_pw.getPlotItem().clear()
        self.ksi_pw.getPlotItem().setTitle("Phi' graph")
        self.ksi_pw.getPlotItem().plot(self.time, self.ksi)
        self.ksi_pw.getPlotItem().showGrid(x=True, y=True)
        self.ksi_pw.getPlotItem().setLabel('left', "Phi'", units='t')
        self.ksi_pw.getPlotItem().setLabel('bottom', 't')
        a = self.phi_pw.plotItem

    def drawtable(self):
        self.table_tw.setRowCount(self.n)
        self.table_tw.setColumnCount(3)
        self.table_tw.setHorizontalHeaderLabels(('t', 'phi(t)', "phi'(t)"))
        for row in range(self.n):
            self.table_tw.setItem(row, 0, QTableWidgetItem(str(self.time[row])))
            self.table_tw.setItem(row, 1, QTableWidgetItem(str(self.phi[row])))
            self.table_tw.setItem(row, 2, QTableWidgetItem(str(self.ksi[row])))

    def calcslot(self):
        self.readdata()
        self.drawplots()
        self.drawtable()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    ui = MainWindow(window)
    window.show()
    sys.exit(app.exec_())