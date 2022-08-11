# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-07-08 18:43:46
# @Last Modified by:   Climax
# @Last Modified time: 2022-08-10 15:04:29



import sys
from PyQt5.QtWidgets import (QApplication, QAction, QMenu, QMainWindow)
from PyQt5.Qt import *

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
	"""
	this is the main window
	"""
	def __init__(self):
		super().__init__()
		self.show()

	def ContextMenuEvent(self, e):	
		context = QMenu(self) # be sure to also use "variable = QMenu(self)" for the same output
		context.addAction(QAction("test 1", self))
		context.addAction(QAction("test 2", self))
		context.addAction(QAction("test 3", self))
		context.exec_(self.mapToGlobal(e))


	def mousePressEvent(self, event):
		print("Mouse Pressed")
		super(self, MainWindow).contextMenuEvent(event)

"""

		note- THIS CODE DOESN'T WORK YET


"""



central = MainWindow()
central.show()
app.exec_()



