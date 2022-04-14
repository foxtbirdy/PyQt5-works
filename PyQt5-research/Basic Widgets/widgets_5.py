# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2021-10-19 22:25:41
# @Last Modified by:   Climax
# @Last Modified time: 2021-10-19 22:58:32


import sys

from PyQt5.QtWidgets import QApplication, QListWidget, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widget 5")

        widget = QListWidget()
        widget.addItems(["1", "2", "3"])

        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    # print if index
    def index_changed(self, int):
        print(int)

    # print if str
    def text_changed(self, str):
        print(str)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
