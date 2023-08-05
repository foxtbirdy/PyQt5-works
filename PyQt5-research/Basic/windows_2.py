# To not recreate a new window if the current second window is
# still running

import sys
from random import randint  
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget)




class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.w = None
		self.button = QPushButton("Click me for a widget to appear")
		self.button.clicked.connect(self.show_new_window)
		self.setCentralWidget(self.button)

	def create_window(self, clicked):
		print(clicked)
		self.w = AnotherWindow()
		self.w.show()


	def show_new_window(self, checked):
		print(checked)
		if self.w is None:
			self.w = AnotherWindow()
			self.w.show()




class AnotherWindow(QWidget):

	"""
	This is the window where there are no parents. it is a standalone widget of a sort
	"""
	def __init__(self):
		super().__init__()


		layout = QVBoxLayout()
		self.label = QLabel(
      f"Another Window with a random number: {randint(0,100)}"
      )

		self.button_exit = QPushButton("Click me to exit")
		self.button_exit.clicked.connect(self.exit_program)

		layout.addWidget(self.label)
		layout.addWidget(self.button_exit)
		
		self.setLayout(layout)


	def exit_program(self):
		app.quit()



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()


"""

If you want to see if there is any kind of program that is running or not, be sure to use this codeline 
-> 
if self.w is None:
	self.w = AnotherWindow()
	self.w.show()

A log was created for this case.

PyQt5-research\logs\Checking if a second window is running.md
"""


