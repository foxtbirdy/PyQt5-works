# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-04-27 23:02:15
# @Last Modified by:   Climax
# @Last Modified time: 2022-04-28 00:52:44
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout

from layout_colorwidget import Color

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("QStackedLayout DEMO")

		layout = QStackedLayout()
		layout.addWidget(Color("red"))
		layout.addWidget(Color("green"))
		layout.addWidget(Color("blue"))
		layout.addWidget(Color("yellow"))

		layout.setCurrentIndex(0) # set current index



		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()