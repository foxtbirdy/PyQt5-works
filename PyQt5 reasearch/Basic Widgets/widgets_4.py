# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2021-10-17 23:14:27
# @Last Modified by:   Climax
# @Last Modified time: 2021-10-19 22:24:07


import sys


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QComboBox, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app")

        widget = QComboBox()

        # font
        font = widget.font()
        font.setPointSize(10)
        widget.setFont(font)

        # set if the number of tabs are changed.
        widget.currentIndexChanged.connect(self.index_changed)
        # set if the text of the tabs are changed.
        widget.currentTextChanged.connect(self.text_changed)

        # set editable - bool
        widget.setEditable(True)
        widget.setInsertPolicy(QComboBox.InsertAlphabetically)

        # set widget policy - IF EXISTS
        self.setCentralWidget(widget)

    def index_changed(self, i):
        print(i)

    def text_changed(self, s):
        print(s)


# Excuete
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
