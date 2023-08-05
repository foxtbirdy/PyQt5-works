# Creating another window beside the QMainWindow
# QWidget is used for that

import sys

from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QWidget, QVBoxLayout)




class MainWindow(QMainWindow):
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
	This window is a QWidget. 
 	If unliked to a parent, it will appear as a free floating window
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


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()




# Please note that if you try to create another window that is not the MainWindow 
# then the Anotherwindow will exit immediately because it has no parent window.
# That means, once the code is ran the program will exit immedidately due to it has no purpose making,
# it be cleaned by python and then well.....destroyed.

# to fix this, be sure to add like self.w = AnotherWindow() instead of w.AnotherWindow to create a reference to the main application.


