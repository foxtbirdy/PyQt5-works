# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-07-08 18:43:46
# @Last Modified by:   Climax
# @Last Modified time: 2022-07-08 21:11:52



import sys
from random import randint  
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget)


app = QApplication(sys.argv)


class MainWindow(QMainWindow):
	"""
	this is the main window
	"""



	def __init__(self):
		super().__init__()
		self.button = QPushButton("Click me for a widget to appear")
		self.button.clicked.connect(self.create_window)
		self.setCentralWidget(self.button)

	def create_window(self, clicked):
		print(clicked)
		self.w = AnotherWindow()
		self.w.show()



class AnotherWindow(QWidget):

	"""
	This is the window where there are no parents. it is a standalone widget of a sort
	"""
	def __init__(self):
		super().__init__()


		layout = QVBoxLayout()
		self.label = QLabel(f"Another Window with a random number {randint(0,100)}")

		self.button_exit = QPushButton("Click me to exit")
		self.button_exit.clicked.connect(self.exit_program)

		layout.addWidget(self.label)
		layout.addWidget(self.button_exit)
		
		self.setLayout(layout)


	def exit_program(self):
		app.quit()



central = MainWindow()
central.show()
app.exec_()


"""

If you want to see if there is any kind of program that is running or not, be sure to use this codeline 
-> 
if self.w is None:
	self.w = AnotherWindow()
	self.w.show()


"""


