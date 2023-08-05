# Adding more functionality to QDialogs

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


class CustomDialog(QDialog):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Visit my Github Page!")
		self.setFixedSize(400,200)

		# QDialogButton init
		# Note that QDialogButtons have a fixed set of available button types 
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

