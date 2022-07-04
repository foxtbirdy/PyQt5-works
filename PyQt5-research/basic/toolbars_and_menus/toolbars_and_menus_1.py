# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-04-30 01:51:14
# @Last Modified by:   Climax
# @Last Modified time: 2022-04-30 02:04:09

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("QToolBar Demo")


		label = QLabel("Hello")
		label.setAlignment(Qt.AlignCenter)

		self.setCentralWidget(label)

		toolBar = QToolBar("ToolBar")
		self.addToolBar(toolBar)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
