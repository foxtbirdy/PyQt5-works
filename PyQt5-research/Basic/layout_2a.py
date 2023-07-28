# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-04-14 21:16:14
# @Last Modified by:   Climax
# @Last Modified time: 2022-04-16 05:59:01



import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

# import from local files
from layout_colorwidget import Color


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("QColor demo")

		layout = QVBoxLayout()
		layout.addWidget(Color("red"))

		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()