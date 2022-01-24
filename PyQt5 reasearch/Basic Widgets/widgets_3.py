# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2021-10-17 23:14:27
# @Last Modified by:   Climax
# @Last Modified time: 2021-10-27 22:51:56


import sys


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QCheckBox, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app")

        widget = QCheckBox("This is a checkbox")
        widget.setCheckState(Qt.PartiallyChecked)

        widget.stateChanged.connect(self.show_state)
        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s)
        if s == 1:
            print("What are you doing??")


app = QApplication(sys.argv)


window = MainWindow()
window.show()


app.exec_()
