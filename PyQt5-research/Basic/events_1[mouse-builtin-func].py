# Events related to mouse movement and mouse behavior

import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow)


app = QApplication(sys.argv)


class MainWindow(QMainWindow):
	"""
	this is the main window.
	"""
 
	def __init__(self):
		super().__init__()
		self.label = QLabel("Click in this window")
		self.setCentralWidget(self.label)
		self.setMouseTracking(True) # default = False


# below are default function names for the mouse features.
	def mouseMoveEvent(self, e):
		self.label.setText("Mouse was Moved")

	def mousePressEvent(self, e):
		self.label.setText("Mouse was pressed")

	def mouseReleaseEvent(self, e):
		self.label.setText("Mouse was released")

	def mouseDoubleClickEvent(self, e):
		self.label.setText("Mouse was double clicked")





central = MainWindow()
central.show()
app.exec_()



