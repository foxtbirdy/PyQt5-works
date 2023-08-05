# Creating a new dialog window from QMainWindow
# To use dialogs, use QDialog

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog

class MainWindow(QMainWindow):

	def __init__(self):
		super().__init__()
		self.setWindowTitle("Hello 1")

		# QPushButton init
		button = QPushButton("Press me, get a dialog!")
		button.clicked.connect(self.button_clicked)
		self.setCentralWidget(button)
  
  
	def button_clicked(self, s):
		print('click', s)
  
		# QDialog init
		dlg = QDialog(self)
		dlg.setWindowTitle("Hello 2")
		dlg.exec_()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
