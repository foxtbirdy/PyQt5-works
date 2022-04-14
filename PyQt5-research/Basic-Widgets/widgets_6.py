# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2021-10-19 22:25:41
# @Last Modified by:   Climax
# @Last Modified time: 2022-01-24 05:50:21


import sys

from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widget 5")

        widget = QLineEdit()
        widget.setPlaceholderText("Type something")


        widget.returnPressed.connect(self.return_passed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)


        self.setCentralWidget(widget)

    def return_passed(self):
        print("return pressed")
        self.centralWidget().setText("Nice Gen Z joke")

    def selection_changed(self):
        print("Selection Changed")
        print(self.centralWidget().selectedText())

    def text_edited(self, txt):
        print('Edited text : ', txt)

    def text_changed(self, str):
        print(str)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
