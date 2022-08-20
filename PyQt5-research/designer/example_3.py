# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass




import sys

import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, label

from MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



        f = self.label.font()
        f.setPointSize(25)
        self.label.setAlignment(Qt.AlighHCenter | Qt.AlignVCenter)
        self.label.setFont(f)
        self.pushButton.pressed.connect(self.update_label)

    def update_label(self):
        n = random.randint(1,6)
        self.label.setText("%d" , n)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
