
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("Gui.ui", self)

    #def port_scanner(self):




app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()