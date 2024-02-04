import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic.properties import QtWidgets


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ui.ui', self) # Load the .ui file
        self.show() # Show the GUI
        var = self.me


app = QApplication(sys.argv)

window = Ui()
window.show()

app.exec()