# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-07-06 22:02:52
# @Last Modified by:   Climax
# @Last Modified time: 2022-07-08 18:38:28



# Fixed version of the Dialog_1.py


import sys
import webbrowser

from PyQt5.QtWidgets import QApplication,QMainWindow, QVBoxLayout, QPushButton, QDialog, QDialogButtonBox, QLabel 

url = "https://github.com/Code-Blender-7"
app = QApplication(sys.argv)

class MainWindow(QMainWindow):



	def __init__(self):
		super().__init__()
		self.setWindowTitle("App")


		# functionality
		button = QPushButton("Press me, get a dialog!")
		button.clicked.connect(self.button_clicked)
		self.setCentralWidget(button)

	def button_clicked(self, s):
		print('click', s)

		dlg = CustomDialog()

		if dlg.exec_():
			webbrowser.open(url)
		else:
			print("Redirection Cancelled.")
			app.quit() # exit the program


class CustomDialog(QDialog):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Visit my Github Page!")
		self.setFixedSize(400,200)


		QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

		self.buttonBox = QDialogButtonBox(QBtn)
		self.buttonBox.accepted.connect(self.accept)
		self.buttonBox.rejected.connect(self.reject)

		self.layout = QVBoxLayout()
		message = QLabel("Visit me on my Github Page? \nClick Yes and the Webbrowser shall give you a ride!")
		self.layout.addWidget(message)
		self.layout.addWidget(self.buttonBox)
		self.setLayout(self.layout)


window = MainWindow()
window.show()
app.exec_()

