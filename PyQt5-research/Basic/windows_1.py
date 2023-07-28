# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-07-08 18:43:46
# @Last Modified by:   Climax
# @Last Modified time: 2022-07-08 21:10:48



import sys

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
		self.label = QLabel("Another Window")

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

Please note that if you try to create another window that is not the MainWindow then the Anotherwindow will exit immediately because it has no parent window.
That means, once the code is ran the program will exit immedidately due to it has no purpose making it be cleaned by python and then well.....destroyed.

to fix this, be sure to add like self.w = AnotherWindow() instead of w.AnotherWindow to chain its connection to the main application.

"""

