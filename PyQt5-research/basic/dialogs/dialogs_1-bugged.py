# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-07-06 16:25:20
# @Last Modified by:   Climax
# @Last Modified time: 2022-07-06 22:04:58



import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QDialog, QLabel

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

		dlg = CustomDialog(QDialog)
		if dlg.exec_():
			print("success")
		else:
			print('cancelled')



class CustomDialog(QDialog):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Vist my Github!")

		
		QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
		self.buttonBox = QDialogButtonBox(QBtn)
		self.buttonBox.accepted.connect(self.accept)
		self.buttonBox.rejected.connect(self.reject)


		messsage = Qlabel("Do you want to go to my Github Account?")


		self.layout = QVBoxLayout()
		self.layout.addWidget(message)
		self.layout.addWidget(self.buttonBox)
		self.setLayout(self.layout)



app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()




## THIS IS BUGGED.
## The fixed version is located on the Dialog_2.py

