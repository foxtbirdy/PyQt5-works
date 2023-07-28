# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-07-08 18:43:46
# @Last Modified by:   Climax
# @Last Modified time: 2022-08-10 14:41:55



import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow)
from PyQt5.Qt import *

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
	"""
	this is the main window
	"""



	def __init__(self):
		super().__init__()
		self.label = QLabel("Click in this window")
		self.setCentralWidget(self.label)
		self.setMouseTracking(True) # default = False?


# below are default function names for the mouse features.
	def mouseMoveEvent(self, e):
		self.label.setText("Mouse was Moved")

	def mousePressEvent(self, e):
		if e.button() == Qt.LeftButton:
			self.label.setText("mousePressEvent Left")


	def mouseReleaseEvent(self, e):
		self.label.setText("Mouse was released")

	def mouseDoubleClickEvent(self, e):
		self.label.setText("Mouse was double clicked")



"""

Note

Qt can return either 0,1,2,4.


Be sure to import everything of Qt. Because I don't even know which one is the actual. lolol
it means that 1 is leftButton click and the 2 is RightButton click.
Also, 0 means no button or Qt.NoButton and 4 means Qt.MiddleButton
"""



central = MainWindow()
central.show()
app.exec_()



