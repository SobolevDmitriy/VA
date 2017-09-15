import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget
from Front import Ui_Form


class MainWindow(Ui_Form):
    def __init__(self, form):
        self.setupUi(form)
        self.calc_btn.clicked.connect(self.calcslot)

    def readdata(self):
        try:
            j = int(self.j_le.text())
            a = int(self.a_le.text())
            h = int(self.h_le.text())
            n = int(self.n_le.text())
        except ValueError:
            print('Only numbers required')

    def drawplots(self):
        x = [i for i in range(1000)]
        y = [i**2 for i in range(1000)]
        self.phi_pw.plot(x, y)

    def calcslot(self):
        self.readdata()
        self.drawplots()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    ui = MainWindow(window)
    window.show()
    sys.exit(app.exec_())