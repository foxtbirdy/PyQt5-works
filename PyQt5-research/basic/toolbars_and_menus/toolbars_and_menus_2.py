# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-04-30 01:51:14
# @Last Modified by:   Climax
# @Last Modified time: 2022-04-30 02:24:33

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QAction


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("QToolBar Demo")


		label = QLabel("Hello")
		label.setAlignment(Qt.AlignCenter)

		self.setCentralWidget(label)

		toolBar = QToolBar("ToolBar")
		self.addToolBar(toolBar)

		button_action = QAction("Button", self)
		button_action.setStatusTip("This is your button")
		button_action.triggered.connect(self.toolbarClick)

		toolBar.addAction(button_action)

	def toolbarClick(self, s):
		print("clicked", s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
