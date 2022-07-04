# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-04-26 19:43:45
# @Last Modified by:   Climax
# @Last Modified time: 2022-04-26 21:22:10


import sys

from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (
	QApplication,
	QHBoxLayout,
	QLabel,
	QMainWindow,
	QVBoxLayout,
	QWidget
	)


from layout_colorwidget import Color



class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("a0")
		self.setFixedSize(500,300)
		


		layout1 = QHBoxLayout()
		layout2 = QVBoxLayout()
		layout3 = QVBoxLayout()

		layout2.addWidget(Color("red"))
		layout2.addWidget(Color("purple"))
		layout2.addWidget(Color("green"))

		layout3.addWidget(Color("red"))
		layout3.addWidget(Color("black"))
		layout3.addWidget(Color("green"))

		layout1.addLayout(layout2)
		layout1.addLayout(layout3)
		layout1.addWidget(Color("green"))
		layout1.setContentsMargins(0,0,0,0)
		layout1.setSpacing(20)

		widget = QWidget()
		widget.setLayout(layout1)

		self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
